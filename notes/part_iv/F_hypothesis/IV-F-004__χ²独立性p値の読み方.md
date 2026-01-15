# χ²独立性：p値の読み方

## Tags
- dom/stat
- obj/test
- shape/hypothesis
- tool/chi_square

## Spec
- （必要に応じて Ω, E を定義）

## Query
- 問：p値
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- χ²とdfから上側確率
- Assume：none

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：P(χ² > val) (upper tail)
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
