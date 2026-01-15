# χ²独立性：期待度数E_ij

## Tags
- dom/stat
- obj/test
- shape/hypothesis
- dec/sum_partition
- tool/chi_square

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：E_ijの式
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- O_ij観測度数, n総数
- Assume：none

## Decompose
排反分割（和）で全体を作る：
- 例：E = ⋃_{θ∈Θ} (E∩{θ})（排反）
- よって P(E)=Σ_θ P(E|θ)P(θ)

## Compute
- 答（最終形）：E_ij=(行i合計)(列j合計)/n
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
