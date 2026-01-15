# 一般更新：q(θ|E)=L(E|θ)q0(θ)/Σ

## Tags
- dom/prob
- obj/post
- shape/latent_obs
- etype/intersection
- dec/sum_partition
- tool/update_q

## Spec
- 潜在ラベル：θ ∈ Θ（例：{感,非}）
- 観測：rᵢ ∈ ℛ（例：{陽,陰}）
- 回数：T（例：1,2,…）
- 全体：Ω := Θ × ℛ^T,  ω=(θ,r₁,…,r_T)

（記法憲法：積/∩の並びは **左=新、右=旧** で統一）

## Query
- 問：q(θ*):=P(θ*|E)
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- θ∈Θ, E⊂Ω, q0(θ)=P(θ), L(E|θ)=P(E|θ)
- Assume：none

## Decompose
排反分割（和）で全体を作る：
- 例：E = ⋃_{θ∈Θ} (E∩{θ})（排反）
- よって P(E)=Σ_θ P(E|θ)P(θ)

## Compute
- 答（最終形）：q(θ)=L(E|θ)q0(θ)/Σ_{θ'}L(E|θ')q0(θ')
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
