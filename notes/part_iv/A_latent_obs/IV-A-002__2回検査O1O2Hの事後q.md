# 2回検査：O1=+,O2=+→Hの事後q

## Tags
- dom/prob
- obj/post
- shape/latent_obs
- etype/intersection
- dec/both
- dep/indep
- tool/update_q

## Spec
- 潜在ラベル：θ ∈ Θ（例：{感,非}）
- 観測：rᵢ ∈ ℛ（例：{陽,陰}）
- 回数：T（例：1,2,…）
- 全体：Ω := Θ × ℛ^T,  ω=(θ,r₁,…,r_T)

（記法憲法：積/∩の並びは **左=新、右=旧** で統一）

## Query
- 問：q:=P(H=h+ | E2), E2={O2=+}∩{O1=+}
- 求：（q(…)=P(…|E) / P(E) / Var(…) 等、目的量をここに固定）

## E（事象）
- E := （ここを1行で。intersection/sequence は **左=新、右=旧**）

## Given
- t1:=P(O1=+|H=h+), f1:=P(O1=+|H=h-), t2:=P(O2=+|O1=+,H=h+), f2:=P(O2=+|O1=+,H=h-)
- Assume：（2回目はO1=+で条件付け）

## Decompose
和（排反分割）＋積（逐次）の両方を使う：
- まず θ などで割って Σ
- 各項の中で E を新→旧で ∏ へ

## Compute
- 答（最終形）：q=(p t1 t2)/(p t1 t2 + p̄ f1 f2)
- （ここに“係数漏れ防止”のため、分母=全体を一度だけ排反和で書く）

## Check
- 極限/範囲/単位の1行検算
