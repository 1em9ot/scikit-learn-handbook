#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iv_manifest.tsv から Part IV の雛形(md)を量産する。
- 1行=1ページ
- "問＋答"が揃ってる話題の機械化に特化
"""
from __future__ import annotations
import csv, re
from pathlib import Path

def _slug(s:str)->str:
  s=s.strip()
  s=re.sub(r"[^\w\u3040-\u30ff\u4e00-\u9fff\- ]","",s)
  s=re.sub(r"\s+","_",s)
  return s[:60] if s else "untitled"

def _mkdir(p:Path)->None:
  p.mkdir(parents=True, exist_ok=True)

def _shape_dir(sh:str)->str:
  m={
    "shape/latent_obs":"A_latent_obs",
    "shape/standardize":"B_standardize",
    "shape/sampling":"C_sampling",
    "shape/sequence":"D_sequence",
    "shape/estimation":"E_estimation",
    "shape/hypothesis":"F_hypothesis",
    "shape/geometry":"G_geometry",
  }
  return m.get(sh,"Z_misc")

def _tags(r:dict)->str:
  xs=[r["dom"],r["obj"],r["shape"]]
  for k in ["etype","dec","dep","tool"]:
    v=r.get(k,"").strip()
    if not v or v=="none":
      continue
    if k=="tool":
      xs += [f"tool/{t.strip()}" for t in v.split(",") if t.strip()]
    else:
      xs.append(f"{k}/{v}")
  return "\n".join(f"- {x}" for x in xs)

def _spec_block(r:dict)->str:
  sh=r["shape"]
  if sh=="shape/latent_obs":
    return "\n".join([
      "- 潜在ラベル：θ ∈ Θ（例：{感,非}）",
      "- 観測：rᵢ ∈ ℛ（例：{陽,陰}）",
      "- 回数：T（例：1,2,…）",
      "- 全体：Ω := Θ × ℛ^T,  ω=(θ,r₁,…,r_T)",
      "",
      "（記法憲法：積/∩の並びは **左=新、右=旧** で統一）",
    ])
  if sh=="shape/standardize":
    return "\n".join([
      "- 変数：x（実数）",
      "- 全体：Ω := ℝ",
      "- 標準化：Z := (x-μ)/σ",
    ])
  if sh=="shape/sampling":
    return "\n".join([
      "- 母集団：U={1,…,N}",
      "- 非復元抽出：i₁,…,i_n（全て相異）",
      "- 観測：r_k := v_{i_k}",
      "- 全体：Ω := { (i₁,…,i_n) : 相異 }",
    ])
  if sh=="shape/sequence":
    return "\n".join([
      "- 時系列：r₁,…,r_T",
      "- 全体：Ω := ℛ^T（状態があるなら Θ×ℛ^T）",
      "- E_{1:i} := Eᵢ ∩ … ∩ E₁（左=新、右=旧）",
    ])
  return "- （必要に応じて Ω, E を定義）"

def _decomp_hint(r:dict)->str:
  dec=r.get("dec","").strip()
  if dec=="sum_partition":
    return "\n".join([
      "排反分割（和）で全体を作る：",
      "- 例：E = ⋃_{θ∈Θ} (E∩{θ})（排反）",
      "- よって P(E)=Σ_θ P(E|θ)P(θ)",
    ])
  if dec=="prod_step":
    return "\n".join([
      "逐次積（新→旧）で積む：",
      "- 例：P(Eᵢ∩E_{1:i-1}|…)=P(Eᵢ|E_{1:i-1},…)*P(E_{1:i-1}|…)",
    ])
  if dec=="both":
    return "\n".join([
      "和（排反分割）＋積（逐次）の両方を使う：",
      "- まず θ などで割って Σ",
      "- 各項の中で E を新→旧で ∏ へ",
    ])
  return "（ここは不要、または問題に応じて記述）"

def gen(tsv:Path, outdir:Path)->None:
  with tsv.open("r",encoding="utf-8") as f:
    rd=csv.DictReader(f, delimiter="\t")
    for r in rd:
      if not r.get("id","").strip():
        continue
      sid=r["id"].strip()
      ttl=r.get("title","").strip()
      sh=r.get("shape","").strip()
      d=_shape_dir(sh)
      pdir=outdir/d
      _mkdir(pdir)
      fn=f"{sid}__{_slug(ttl)}.md"
      p=pdir/fn

      body=f"""# {ttl}

## Tags
{_tags(r)}

## Spec
{_spec_block(r)}

## Query
- 問：{r.get("q","").strip()}
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- {r.get("given","").strip()}
- Assume：{r.get("assume","").strip()}

## Decompose
{_decomp_hint(r)}

## Compute
- 答（最終形）：{r.get("a","").strip()}
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算

"""
      p.write_text(body, encoding="utf-8")
      print("gen:", p)

if __name__=="__main__":
  root=Path(__file__).resolve().parent
  gen(root/"iv_manifest.tsv", root/"part_iv")
