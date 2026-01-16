# BernoulliのMLE：p̂=x/n

## Tags
- dom/stat
- obj/est
- shape/estimation
- dec/prod_step
- dep/indep
- tool/likelihood

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：pのMLE
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- x=成功回数, n=試行回数, L(p)=p^x(1-p)^{n-x}
- Assume：indep

## Decompose
逐次積（新→旧）で積む：
- 例：P(Eᵢ∩E_{1:i-1}|…)=P(Eᵢ|E_{1:i-1},…)*P(E_{1:i-1}|…)

## Compute
- 答（最終形）：p̂=x/n
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
