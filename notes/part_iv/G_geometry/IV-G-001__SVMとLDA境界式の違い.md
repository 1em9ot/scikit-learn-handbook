# SVMとLDA：境界式の違い

## Tags
- dom/ml
- obj/compare
- shape/geometry

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：境界の式
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- μ0,μ1,Σ,w,b
- Assume：linear

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：LDA: w∝Σ^{-1}(μ1-μ0), SVM: margin最大でSVが効く
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
