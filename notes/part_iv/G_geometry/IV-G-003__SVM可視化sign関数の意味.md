# SVM可視化：sign関数の意味

## Tags
- dom/ml
- obj/compare
- shape/geometry

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：sign(f(x))
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- 判別関数f(x)の符号でクラス決定
- Assume：linear

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：sign(f(x)) ∈ {+1, -1}
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
