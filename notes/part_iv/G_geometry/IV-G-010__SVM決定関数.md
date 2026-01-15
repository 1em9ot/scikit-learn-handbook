# SVM決定関数

## Tags
- dom/ml
- obj/compare
- shape/geometry

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：g(x),ŷ
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- α_i,y_i,k,b
- Assume：linear/kernel

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：g(x)=Σ α_i y_i k(x_i,x)+b, ŷ=sign(g(x))
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
