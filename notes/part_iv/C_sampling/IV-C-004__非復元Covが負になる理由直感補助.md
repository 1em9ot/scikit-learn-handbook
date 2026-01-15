# 非復元：Covが負になる理由（直感補助）

## Tags
- dom/stat
- obj/compare
- shape/sampling
- dep/dep

## Spec
- 母集団：U={1,…,N}
- 非復元抽出：i₁,…,i_n（全て相異）
- 観測：r_k := v_{i_k}
- 全体：Ω := { (i₁,…,i_n) : 相異 }

## Query
- 問：Cov<0 の説明
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- i≠j
- Assume：dep

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：同じ個体を2回引けない→片方が成功だと他方成功が減る
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
