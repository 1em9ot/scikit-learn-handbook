# 非復元抽出：ΣΣCov の非対角の項数

## Tags
- dom/stat
- obj/cov
- shape/sampling
- dec/sum_partition
- dep/dep
- tool/cov_expand

## Spec
- 母集団：U={1,…,N}
- 非復元抽出：i₁,…,i_n（全て相異）
- 観測：r_k := v_{i_k}
- 全体：Ω := { (i₁,…,i_n) : 相異 }

## Query
- 問：非対角(i≠j)の項数
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- 対称性で(i,j)と(j,i)が同じ、対角はn個
- Assume：dep

## Decompose
排反分割（和）で全体を作る：
- 例：E = ⋃_{θ∈Θ} (E∩{θ})（排反）
- よって P(E)=Σ_θ P(E|θ)P(θ)

## Compute
- 答（最終形）：2*C(n,2)=n(n-1)
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
