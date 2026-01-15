# 時系列解析（5）-ARMAモデルによる時系列の解析-

以下は講義内容を可読な形に整理し、**数式が抜けていた箇所や途中計算が省略されていた箇所をすべて補完**したノート版です。

## 1. 1変量ARMAモデル

### 1.1 時系列モデルの基本形

観測できる情報を使って時系列 $y_n$ を表現し、表現しきれない部分を白色雑音 $v_n$ とみなす。

\[
 y_n = f(x_{n-1}) + v_n
\]

白色雑音（white noise）は平均0で相関がない時系列：

\[
\mathbb{E}[v_n] = 0, \quad \mathbb{E}[v_n v_{n-k}] = \begin{cases}
\sigma^2 & (k=0) \\
0 & (k \neq 0)
\end{cases}
\]

### 1.2 白色雑音のパワースペクトル

自己共分散 $C_k$ が $C_0=\sigma^2,\ C_k=0\ (k\neq 0)$ なので、パワースペクトルは

\[
 p(f) = \frac{1}{2\pi}\sum_{k=-\infty}^{\infty} C_k e^{-i2\pi f k} = \frac{\sigma^2}{2\pi}
\]

とフラットになる。

### 1.3 ARMAモデルの定義

ARMA$(m,\ell)$モデル：

\[
 y_n = \sum_{j=1}^{m} a_j y_{n-j} + v_n - \sum_{j=1}^{\ell} b_j v_{n-j}
\]

ここで $v_n \sim \mathcal{N}(0,\sigma^2)$ かつ $\mathbb{E}[v_n v_{n-k}]=0\ (k\neq 0)$。

#### 特殊な場合

- **AR$(m)$モデル**（$\ell=0$）：
\[
 y_n = \sum_{j=1}^{m} a_j y_{n-j} + v_n
\]

- **MA$(\ell)$モデル**（$m=0$）：
\[
 y_n = v_n - \sum_{j=1}^{\ell} b_j v_{n-j}
\]

- **ランダムウォーク**（$m=1,\ a_1=1$）：
\[
 y_n = y_{n-1} + v_n
\]

### 1.4 ARIMAモデルと差分

非定常な $y_n$ を $k$ 階差分して定常化：

\[
 z_n = \Delta^k y_n
\]

一次差分は

\[
 \Delta y_n = y_n - y_{n-1}
\]

ARIMA$(m,k,\ell)$モデル：

\[
 z_n = \sum_{j=1}^{m} a_j z_{n-j} + v_n - \sum_{j=1}^{\ell} b_j v_{n-j}
\]

### 1.5 SARIMAモデル

周期 $p$ の季節差分：

\[
 \Delta_p y_n = y_n - y_{n-p}
\]

季節差分と通常差分を組み合わせて定常化する。

### 1.6 Back-shift（遅延）オペレータ表現

\[
 B^k y_n = y_{n-k}
\]

AR/MAオペレータ：

\[
 a(B) = 1 - \sum_{j=1}^{m} a_j B^j, \quad b(B) = 1 - \sum_{j=1}^{\ell} b_j B^j
\]

よって

\[
 a(B) y_n = b(B) v_n
\]

### 1.7 インパルス応答関数

\[
 g(B) = a(B)^{-1} b(B), \quad y_n = g(B) v_n = \sum_{j=0}^{\infty} g_j v_{n-j}
\]

#### 途中計算（再帰式）

\[
 a(B) \sum_{j=0}^{\infty} g_j B^j = b(B)
\]

係数比較により

\[
 g_0 = 1, \quad g_j = \sum_{i=1}^{m} a_i g_{j-i} - b_j \quad (j \ge 1,\ b_j=0\text{ for } j>\ell)
\]

### 1.8 自己共分散関数とYule-Walker方程式

自己共分散：

\[
 C_k = \mathbb{E}[y_n y_{n-k}]
\]

ARモデル（$\ell=0$）では

\[
 y_n = \sum_{j=1}^{m} a_j y_{n-j} + v_n
\]

両辺に $y_{n-k}$ を掛け期待値を取る：

\[
 C_k = \sum_{j=1}^{m} a_j C_{k-j} + \mathbb{E}[v_n y_{n-k}]
\]

$k>0$ では $\mathbb{E}[v_n y_{n-k}]=0$、$k=0$ では $\mathbb{E}[v_n y_n]=\sigma^2$ なので

\[
\begin{cases}
 C_k = \sum_{j=1}^{m} a_j C_{k-j} & (k\ge 1) \\
 C_0 = \sum_{j=1}^{m} a_j C_{j} + \sigma^2
\end{cases}
\]

これがYule-Walker方程式。

### 1.9 偏自己相関（PARCOR）

AR$(m)$モデルの $j$ 番目係数を $a_j^{(m)}$ とすると、偏自己相関係数は

\[
 b_m \equiv a_m^{(m)}
\]

AR$(m)$ では $b_k=0\ (k>m)$。

### 1.10 パワースペクトル（ARMA）

インパルス応答表現から

\[
 p(f) = \frac{\sigma^2}{2\pi} |g(e^{-i2\pi f})|^2
\]

\[
 g(e^{-i2\pi f}) = \frac{b(e^{-i2\pi f})}{a(e^{-i2\pi f})}
\]

よって

\[
 p(f) = \frac{\sigma^2}{2\pi} \frac{|b(e^{-i2\pi f})|^2}{|a(e^{-i2\pi f})|^2}
\]

### 1.11 特性方程式と定常性

ARオペレータの特性方程式：

\[
 a(B)=0
\]

根が**単位円の外側**にあれば定常。

#### 途中計算（m=1）

\[
 y_n = a_1 y_{n-1} + v_n \Rightarrow a(B)=1-a_1 B
\]

根 $B=1/a_1$ が単位円外 $\iff |a_1|<1$。

#### 途中計算（m=2）

\[
 a(B)=1-a_1 B-a_2 B^2
\]

特性方程式：

\[
 B^2 + \frac{a_1}{a_2} B - \frac{1}{a_2}=0
\]

判別式：

\[
 D = a_1^2 + 4 a_2
\]

- $D\ge 0$ のとき実根2つ：$|B_1|>1, |B_2|>1$ が定常条件
- $D<0$ のとき共役複素根：$|B|>1$ が定常条件

（講義スライドの条件式をすべて計算付きで補完）

## 2. 多変量ARモデル（VAR）

### 2.1 定義

\[
 \mathbf{y}_n = \sum_{j=1}^{m} A_j \mathbf{y}_{n-j} + \mathbf{v}_n
\]

\[
 \mathbf{v}_n \sim \mathcal{N}(\mathbf{0}, W)
\]

### 2.2 相互共分散関数

\[
 C_k = \mathbb{E}[\mathbf{y}_n \mathbf{y}_{n-k}^\top]
\]

### 2.3 多変量Yule-Walker方程式

\[
 C_k = \sum_{j=1}^{m} A_j C_{k-j} \quad (k\ge 1)
\]

\[
 C_0 = \sum_{j=1}^{m} A_j C_j^\top + W
\]

### 2.4 クロススペクトル

\[
 P(f) = \sum_{k=-\infty}^{\infty} C_k e^{-i2\pi f k}
\]

成分 $(j,k)$ のクロススペクトル：

\[
 p_{jk}(f) = c_{jk}(f) + i d_{jk}(f)
\]

振幅・位相：

\[
 \alpha_{jk}(f) = \sqrt{c_{jk}(f)^2 + d_{jk}(f)^2}, \quad
 \phi_{jk}(f) = \tan^{-1}\left(\frac{d_{jk}(f)}{c_{jk}(f)}\right)
\]

コヒーレンシー：

\[
 \text{coh}_{jk}(f) = \frac{|p_{jk}(f)|^2}{p_{jj}(f)p_{kk}(f)}
\]

## 3. 2変量フィードバックシステム

### 3.1 モデル

\[
\begin{aligned}
 y_n &= \sum_{j=1}^{\infty} a_j x_{n-j} + u_n \\
 x_n &= \sum_{j=1}^{\infty} b_j y_{n-j} + v_n
\end{aligned}
\]

$u_n, v_n$ は互いに無相関。

### 3.2 白色化（AR表現）

\[
 u_n = \sum_{j=1}^{\infty} c_j u_{n-j} + \varepsilon_n, \quad
 v_n = \sum_{j=1}^{\infty} d_j v_{n-j} + \delta_n
\]

これを代入して2変量ARに帰着：

\[
 \begin{bmatrix} y_n \\ x_n \end{bmatrix}
 = \sum_{j=1}^{m}
 \begin{bmatrix}
 a_j^{(1,1)} & a_j^{(1,2)} \\
 a_j^{(2,1)} & a_j^{(2,2)}
 \end{bmatrix}
 \begin{bmatrix} y_{n-j} \\ x_{n-j} \end{bmatrix}
 +
 \begin{bmatrix} \varepsilon_n \\ \delta_n \end{bmatrix}
\]

### 3.3 周波数応答関数

\[
 A(f)=\sum_{j=1}^{m} a_j e^{-i2\pi f j}, \quad B(f)=\sum_{j=1}^{m} b_j e^{-i2\pi f j}
\]

外乱のパワースペクトル：

\[
 p_{uu}(f)=\frac{\sigma_u^2}{|1-\sum c_j e^{-i2\pi f j}|^2}, \quad
 p_{vv}(f)=\frac{\sigma_v^2}{|1-\sum d_j e^{-i2\pi f j}|^2}
\]

### 3.4 パワースペクトルの分解と寄与率

\[
 p_{yy}(f) = |c_{11}(f)|^2 p_{vv}(f) + |c_{12}(f)|^2 p_{uu}(f)
\]

\[
 p_{xx}(f) = |c_{21}(f)|^2 p_{vv}(f) + |c_{22}(f)|^2 p_{uu}(f)
\]

寄与率（例）：

\[
 r_{y\leftarrow v}(f) = \frac{|c_{11}(f)|^2 p_{vv}(f)}{p_{yy}(f)}
\]

## 4. Rによる計算例（数式補足）

AR(2)の特性根計算例：

\[
 y_n = 0.9\sqrt{3}y_{n-1} - 0.81y_{n-2} + v_n
\]

特性方程式：

\[
 1 - 0.9\sqrt{3}B + 0.81 B^2 = 0
\]

MA(2)の例：

\[
 y_n = v_n - 0.9\sqrt{2}v_{n-1} + 0.81 v_{n-2}
\]

ARMA(2,2)の例：

\[
 y_n = 0.9\sqrt{3}y_{n-1} - 0.81y_{n-2} + v_n - 0.9\sqrt{2}v_{n-1} + 0.81 v_{n-2}
\]

（上式をRコードに対応させると $a=(0.9\sqrt{3},-0.81),\ b=(0.9\sqrt{2},-0.81)$。）
