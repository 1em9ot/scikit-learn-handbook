# MLE：argmaxとmaxの区別（答案用）

## Tags
- dom/stat
- obj/compare
- shape/estimation
- tool/likelihood

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：argmaxの意味
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- L(p)は尤度
- Assume：none

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：p̂=argmax_p L(p),  max_p L(p)=L(p̂)
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
