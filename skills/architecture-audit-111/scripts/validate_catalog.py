#!/usr/bin/env python3
"""Valida a integridade do catálogo e, opcionalmente, a matriz de resultados.

Uso:
  python scripts/validate_catalog.py
  python scripts/validate_catalog.py --matrix matriz.xlsx            # template assets/evidence-matrix-template.xlsx
  python scripts/validate_catalog.py --matrix matriz.csv [--id-col id] [--status-col status]

Catálogo: exige 111 IDs únicos ARC-001..ARC-111, em sequência, com a distribuição
24/26/16/14/10/13/8 por grupo.
Matriz (.xlsx lê a aba "Matriz"; .csv lê o arquivo): exige 111 linhas, um ID por controle,
nome igual ao do catálogo (quando a coluna "Controle" existir), status válidos e soma dos
cinco status igual a 111. Linhas com alerta na coluna "Checagem" são relatadas como aviso.
Saída com código 1 se algo falhar.
"""
import argparse, csv, re, sys, collections
from pathlib import Path

EXPECTED_GROUPS = [24, 26, 16, 14, 10, 13, 8]
VALID_STATUS = {"PASS_VERIFIED", "PARTIAL", "FAIL", "NOT_VERIFIED", "NOT_APPLICABLE"}
CATALOG = Path(__file__).resolve().parent.parent / "references" / "controls.md"


def load_catalog():
    text = CATALOG.read_text(encoding="utf-8")
    items = re.findall(r"^### (ARC-\d{3}) — (.+)$", text, re.M)
    return text, items


def check_catalog():
    text, items = load_catalog()
    ids = [i for i, _ in items]
    errors = []
    if ids != [f"ARC-{n:03d}" for n in range(1, 112)]:
        errors.append(f"IDs fora do esperado: {len(ids)} encontrados, únicos={len(set(ids))}")
    parts = re.split(r"^## \d\d\. ", text, flags=re.M)[1:]
    counts = [len(re.findall(r"^### ARC-", p, re.M)) for p in parts]
    if counts != EXPECTED_GROUPS:
        errors.append(f"Distribuição por grupo {counts} != {EXPECTED_GROUPS}")
    return errors


def read_rows(path, id_col, status_col):
    """Devolve lista de dicts com chaves normalizadas: id, status, controle, checagem."""
    p = Path(path)
    rows = []
    if p.suffix.lower() == ".xlsx":
        from openpyxl import load_workbook
        wb = load_workbook(p, data_only=True)
        if "Matriz" not in wb.sheetnames:
            raise SystemExit('Aba "Matriz" não encontrada no arquivo .xlsx')
        ws = wb["Matriz"]
        header = [str(c.value).strip().lower() if c.value is not None else "" for c in ws[1]]
        idx = {h: i for i, h in enumerate(header)}
        icol, scol = idx.get(id_col.lower()), idx.get(status_col.lower())
        if icol is None or scol is None:
            raise SystemExit(f"Colunas '{id_col}'/'{status_col}' não encontradas na aba Matriz: {header}")
        ccol, kcol = idx.get("controle"), idx.get("checagem")
        for r in ws.iter_rows(min_row=2, values_only=True):
            if r[icol] in (None, ""):
                continue
            rows.append({"id": str(r[icol]).strip(),
                         "status": str(r[scol]).strip() if r[scol] else "",
                         "controle": str(r[ccol]).strip() if ccol is not None and r[ccol] else None,
                         "checagem": r[kcol] if kcol is not None else None})
    else:
        with open(p, newline="", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                low = {k.strip().lower(): v for k, v in r.items()}
                rows.append({"id": low[id_col.lower()].strip(), "status": (low[status_col.lower()] or "").strip(),
                             "controle": (low.get("controle") or None), "checagem": low.get("checagem")})
    return rows


def check_matrix(path, id_col, status_col):
    errors, warnings = [], []
    rows = read_rows(path, id_col, status_col)
    ids = [r["id"] for r in rows]
    if len(rows) != 111:
        errors.append(f"Matriz tem {len(rows)} linhas, esperado 111")
    dup = [i for i, c in collections.Counter(ids).items() if c > 1]
    missing = sorted(set(f"ARC-{n:03d}" for n in range(1, 112)) - set(ids))
    if dup:
        errors.append(f"IDs duplicados: {dup}")
    if missing:
        errors.append(f"IDs ausentes: {missing}")
    _, items = load_catalog()
    names = dict(items)
    renamed = [r["id"] for r in rows if r["controle"] and names.get(r["id"]) not in (None, r["controle"])]
    if renamed:
        errors.append(f"Nome do controle diferente do catálogo em: {renamed}")
    status = [r["status"] for r in rows]
    bad = sorted(set(status) - VALID_STATUS - {""})
    if bad:
        errors.append(f"Status inválidos: {bad}")
    totals = collections.Counter(status)
    print("Totais por status:", {k: totals[k] for k in VALID_STATUS if totals[k]}, "| sem status =", totals[""],
          "| soma dos 5 status =", sum(totals[s] for s in VALID_STATUS))
    if sum(totals[s] for s in VALID_STATUS) != 111:
        errors.append("A soma dos cinco status válidos não é 111 (há controles sem status ou status inválido)")
    flagged = [r["id"] for r in rows if r["checagem"] not in (None, "", "OK", "Sem status")]
    if flagged:
        warnings.append(f"{len(flagged)} linha(s) com alerta de consistência na coluna Checagem: {flagged[:15]}"
                        + (" ..." if len(flagged) > 15 else ""))
    return errors, warnings


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix")
    ap.add_argument("--id-col", default="id")
    ap.add_argument("--status-col", default="status")
    a = ap.parse_args()
    errs = check_catalog()
    print("Catálogo:", "OK (111 controles, 24/26/16/14/10/13/8)" if not errs else "FALHOU")
    warns = []
    if a.matrix:
        m, warns = check_matrix(a.matrix, a.id_col, a.status_col)
        print("Matriz:", "OK" if not m else "FALHOU")
        errs += m
    for e in errs:
        print(" ERRO:", e)
    for w in warns:
        print(" AVISO:", w)
    sys.exit(1 if errs else 0)
