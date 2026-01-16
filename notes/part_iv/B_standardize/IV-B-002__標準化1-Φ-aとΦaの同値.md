# 標準化：1-Φ(-a)とΦ(a)の同値

## Tags
- dom/stat
- obj/compare
- shape/standardize
- tool/zscore

## Spec
- 変数：x（実数）
- 全体：Ω := ℝ
- 標準化：Z := (x-μ)/σ

## Query
- 問：1-Φ(-u)=?
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- Φは標準正規の分布関数
- Assume：normal

## Decompose
（ここは不要、または問題に応じて記述）

## Compute
- 答（最終形）：1-Φ(-u)=Φ(u)
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
