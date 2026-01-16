# 漸近正規：スコア/情報量/Taylor

## Tags
- dom/stat
- obj/est
- shape/estimation
- dep/indep
- tool/likelihood

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：MLEの漸近
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- スコアU(θ)=∂ℓ/∂θ, 情報量I(θ)=-E[∂²ℓ/∂θ²]
- Assume：indep

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：√n(θ̂-θ0)→N(0, I(θ0)^{-1})
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
