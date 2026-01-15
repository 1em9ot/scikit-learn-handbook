#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iv_manifest.tsv を簡易lintする。
狙い：TBD/空欄/型の矛盾を早期に炙って、該当チャットに戻る量を最小化。
"""
from __future__ import annotations
import csv, re, sys
from pathlib import Path

def die(msg:str)->None:
  print(msg, file=sys.stderr)

def ok_id(s:str)->bool:
  return bool(re.fullmatch(r"IV-[A-Z]-\d{3}", (s or "").strip()))

def has_tbd(s:str)->bool:
  return "TBD" in (s or "")

def main(p:Path)->int:
  if not p.exists():
    die(f"missing: {p}")
    return 2

  bad=0
  with p.open("r",encoding="utf-8") as f:
    rd=csv.DictReader(f, delimiter="\t")
    for i,r in enumerate(rd, start=2):  # header=1
      e=[]
      rid=r.get("id","").strip()
      if not ok_id(rid): e.append("id")
      for k in ["dom","obj","shape","title","q","a","given"]:
        v=r.get(k,"").strip()
        if not v or has_tbd(v): e.append(k)

      sh=r.get("shape","").strip()
      obj=r.get("obj","").strip()
      et=r.get("etype","").strip()
      dec=r.get("dec","").strip()
      dep=r.get("dep","").strip()
      tool=r.get("tool","").strip()

      # ルール：post/prob は E-type が none だと事故りやすい
      if obj in {"obj/post","obj/prob"} and (not et or et=="none"):
        e.append("etype(req)")

      # ルール：sequence は prod_step/both 推奨
      if sh=="shape/sequence" and dec not in {"prod_step","both"}:
        e.append("dec(seq)")

      # ルール：sampling + dep + var/cov は cov_expand 推奨
      if sh=="shape/sampling" and dep=="dep" and obj in {"obj/var","obj/cov"}:
        if "cov_expand" not in tool:
          e.append("tool(cov_expand)")

      # ルール：test は tool が欲しい（chi_squareなど）
      if obj=="obj/test" and (not tool or tool=="none"):
        e.append("tool(test)")

      if e:
        bad+=1
        die(f"L{i} {rid} :: " + ", ".join(e))

  if bad:
    die(f"\nFAIL: {bad} row(s)")
    return 1
  print("OK")
  return 0

if __name__=="__main__":
  sys.exit(main(Path(__file__).resolve().parent/"iv_manifest.tsv"))
