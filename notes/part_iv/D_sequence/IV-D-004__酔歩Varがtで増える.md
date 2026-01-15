# 酔歩：Varがtで増える

## Tags
- dom/ts
- obj/compare
- shape/sequence
- etype/sequence
- dec/prod_step
- dep/markov

## Spec
- 時系列：r₁,…,r_T
- 全体：Ω := ℛ^T（状態があるなら Θ×ℛ^T）
- E_{1:i} := Eᵢ ∩ … ∩ E₁（左=新、右=旧）

## Query
- 問：Var(x_t)
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- x_t=x_{t-1}+ε_t
- Assume：markov

## Decompose
逐次積（新→旧）で積む：
- 例：P(Eᵢ∩E_{1:i-1}|…)=P(Eᵢ|E_{1:i-1},…)*P(E_{1:i-1}|…)

## Compute
- 答（最終形）：Var(x_t)=t Var(ε)（典型）
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
