# 時系列解析（5）-ARMAモデルによる時系列の解析-

以下、指定いただいた講義資料の内容をそのまま反映しています。

```
東京⼤学 数理・情報教育研究センター
北川 源四郎
時系列解析（５）
−ARMAモデルによる時系列の解析−
概 要
2
1. １変量ARMAモデル
1. インパルス応答関数
2. ⾃⼰共分散関数
3. 偏⾃⼰相関係数
4. パワースペクトル
5. 特性⽅程式
2. 多変量ARモデル
1. 相互共分散関数
2. クロススペクトル
3. パワー寄与率
時系列モデル
3
“情報” 時系列モデル 時系列
n y n 1 x  1 ( ,) n nn y fx v  
• 時系列モデルでは⽩⾊雑⾳が重要
• 過去の利⽤できる情報 xn-1をできるだけ活⽤して
ynを表現し，表現しきれない残りが⽩⾊雑⾳と⾒
なせるようにすることを⽬指す
⽩⾊雑⾳ n v
⽩⾊雑⾳（white noise）
相関がない（独⽴な）時系列
⾃⼰共分散関数
C
k
k
k 





 2 0
0 0
パワースペクトル
2
1
0 ( ) 2 cos( 2 )



  

k 
k p f C C kf
4
1 1
2 2
   f
⽩⾊雑⾳
Ck
k
f
p( f ) スペクトル
⾃⼰共分散 ⽩⾊雑⾳の例
5
2 
2 
w <- as.ts(rnorm(800))
plot(w,ylim=c(-3,3))
plot(as.ts(w[1:200]),ylim=c(-3,3))
⾃⼰回帰移動平均 (ARMA)モデル
y a y v bv n j
j
m
nj n jnj
j
    

 
1 1

n
j
y
m
a
１変量時系列
AR次数
AR係数
n
j
v
b

⽩⾊雑⾳
MA次数
MA係数
6
2 ~ (0, )
[ ]0
[ ]0 0
n
n k
n nj
v N
E vv n k
E vy j


 


ARMA(AutoRegressive Moving Average)モデル
あるいはARMA(m,
）と表現する
正規分布
無相関
過去の時系列と無相関

ARMA モデルの特殊な場合
7
= 0
0
0
m
m

 


ARモデル
MAモデル
⽩⾊雑⾳
1
1
m
n j nj n
j
n n jnj
j
n n
y a y v
y v bv
y v




 
 




AR(m), MA( ) と表現する
y a y v bv n j
j
m
nj n jnj
j
 

 

 
1 1

さらに特殊な場合
マルコフ過程
m   1, 0 
1 m a   1, 0, 1 
ランダムウォーク
n nn 1 1 y ay v   
nn n 1 y y v   
8
注：マルコフ過程とは、1期前の値だけに依存する確率過程
注：AR(m)はm次元の（ベクトル）マルコフ過程になる
ARIMAモデル
n y （平均）⾮定常時系列
k 階差分 ほぼ定常
z a z v bv n jnj
j
m
n jnj
j
 




 
1 1

時系列 差分による定常化 ARMAモデル
9
n nn 1
k
n n
yyy
z y
 

 
Box-Jenkins法
AutoRegressive Integrated Moving Average （ARIMA) model
SARIMAモデル
n
y （平均）⾮定常時系列
z a z v bv n jnj
j
m
n jnj
j
  



 
1 1

10
1 : p
p
n p n n np
B p
z yyy


  
１周期の⻑さ
Seasonal ARIMA（SARIMA) model
Back-shift operatorによる表現
y a y v bv n j
j
m
nj n jnj
j
    

 
1 1

1
k
B n n n nk y y By y   

11
1 1
1 1
m
j j
j j
j j
n n aB y bB v
 
 
           
B: Back-shift operator
L: Lag operatorと呼ぶこともある
1
1
() 1
() 1
m
j
j
j
j
j
j
aB aB
bB bB


 
 


オペレータ
オペレータ

AR
MA
() () n n aB y bBv 
インパルス応答関数
12
1
1
1
0
0
() ()
() () () , 0
( )
n n
j
j
j
n n jnj
j
y aB bBv
gB aB bB gB g
y gBv gv








 
 


{ : 0,1, } j g j


インパルス応答関数
() () n n aB y bBv 
インパルス応答関数
13
0
1
( )
() () ()
n n j nj
j
y gBv g y
gB aB bB




 


{ : 0,1, } j g j


• 時刻
n=0 に加わったノイズが
j 期後に時系列に及ぼす影響
• ARMAモデルは無限次のMAモデルで表現できる
インパルス応答関数（例）
1
1 22 ( ) (1 ) 1
n nn
j
j
y ay v
g B aB aB a B
g a


 
    


14
0
1
1
( 1, 2, )
i
i j ij i
j
g
g ag b i 


  

インパルス応答関数の計算法
インパルス応答関数
15
AR(2) MA(2) ARMA(2,2)
1 2
1 2
1 2 12
( ) 0.9 3 0.81
(2) 0.9 2 0.81
(3) 0.9 3 0.81 0.9 2 0.81
n n nn
nn n n
n n nn n n
y y yv
yv v v
y y yv v v
 
 
  
 
 
   
１
⾃⼰共分散関数
y a y v bv n j
j
m
nj n jnj
j
 

 

 
1 1

16
1 1
2
1 1
( ) ( )( ) ( )
0
()( ) ( )
m
n nk j n j nk n nk j n j nk
j j
n k n jkj j nkj
j j k n
E y y aE y y Ev y bEv y
n k
Ev y Ev gv gEvv
 g nk
   
 
 
 
 

 
  
  
 
 

  2 0 1 1
2
1
1
1
m
j j jj j
j
m
k j k j j jk j
j
C aC bg
C aC bg




 


 
 
 
 


2
1 01 ,, , , , , , , m ab g g CC j j     
2
0
1
1
m
j j
j
m
k j kj
j
C aC
C aC




 



Yule-Walker⽅程式
（ARモデルの場合）
1
n jnj
j
y gv




yn-k と vn をかけ期待値
をとる
⾃⼰共分散関数
17
1 2
1 2
1 2 12
( ) 0.9 3 0.81
(2) 0.9 2 0.81
(3) 0.9 3 0.81 0.9 2 0.81
n n nn
nn n n
n n nn n n
y y yv
yv v v
y y yv v v
 
 
  
 
 
   
１
• MA( )では  Ck=0 （k> のとき） 
18
偏⾃⼰相関係数（PARCOR)
1
m
m
n j nj n
j
y ay v 

  
m
j a 次数 m のARモデルの j 番⽬の係数
m
m m b a  偏⾃⼰相関係数（PARCOR, Partial Autocorrelation)
• 直交化されているので便利
• ⾳声分析、⾳声合成でも重要
19
偏⾃⼰相関係数（PARCOR)
• AR(
m)では
b
k=0 （
k
>
m のとき）
20
AR, MA, ARMAモデルの特徴
( )
( )
( ,)
R b k k
m m
m


 
 

AR
M A
ARMA
⾮零な⾃⼰相関，偏⾃⼰相関の⻑さ
AR係数とPARCORの関係
21
1 1 ( 1, , 1) m m mm i i m mi a a aa i m  
   

1
1
2 2
1 2
333
1 23
4444
1 234
a
a a
aaa
aaaa


 



1 1 {, , } { , , } m m m m bb a a   
1 1
1 1 ( )
m m mm
i i m mi
m m m mm
i m mi m i
a a aa
a a a aa
 

 

 
 
1 1
11 1 { ,, } {,,} m m m mm mm m a a a aa     
と

1 1
1 11 {,,} { ,, } mm m m m m aa a a 

  

1
1
2 1( )
m mm
m i m mi
i m
m
a aa
a
a






21 1 (1 ( ) ) m m m mm m i i m mi a a a aa 

 

パワースペクトル
y a y v bv n j
j
m
nj n jnj
j
    

 
1 1

22
1
( ) n n jnj
j
y gBv gv



 

2
2
2
0 0
2
0 0
( )
( )
( )
[ ]
ikf
k
k
ikf
n nk
k
ikf
j n j p nk p
kj p
ikf
j p n j nk p
k jp
p f Ce
Eyy e
E gv gv e
gg Ev v e











 

 
  
 

 
  






 
 
2
0
n j nk p
jkp
Ev v

 


     


 otherwise
パワースペクトル
23
2 2
0
2 2 2( )
0
2 22
0 0
2 22
0
( )
| |
ikf
j jk
k j
j
ijf i k j f
j jk
j k
ijf ipf
j p
j p
ijf
j
j
p f gg e
ge g e
ge ge
g e

 
 





 


 

 

 
 

 







 
 
 

1
22 2
01 1
2
2
1 2
2
2
1
1 1
1
( )
1
m ijf ijf ijf
jj j
jj j
ijf
j
j
m ijf
j
j
ge ae be
b e
p f
a e
 





 
 




  
       



 




2 2( )
2 2( )
ikf i j k j f
ijf i k j f
e e
e e
jk p
 
 
  
 


 
1
2 2 12
() () ()
( ) ( )( ) ikf ijf ijf
gB aB bB
ge ae be  

  


パワースペクトル
24
AR: ⼭を表現するモデル
MA: ⾕を表現するモデル
ARMA: ⼭と⾕を表現するモデル
1 2
1 2
1 2 12
( ) 0.9 3 0.81
(2) 0.9 2 0.81
(3) 0.9 3 0.81 0.9 2 0.81
n n nn
nn n n
n n nn n n
y y yv
yv v v
y y yv v v
 
 
  
 
 
   
１
AR・MA次数とパワースペクトルの⼭⾕の関係
y a y v bv n j
j
m
nj n jnj
j
    

 
1 1

25
2 2
22 2
1 1
2
2
1
2
2
1
log ( ) log 2 log 1 2 log 1
1
1
2
2
0
m ijf ijf
j j j j
m ijf
j
j
ijf
j
j
p f ae be
a e
b e
k k
k k
f
 



 
 




 
 
 
 
 

 




1
2
AR
MA
スペクトルの⼭ の極⼩点
スペクトルの⾕ の極⼩点
・⼀組の複素数に２次が必要
個の⼭ 次
数
個の⾕ 次
数
・実根：  または の⼭か⾕
2
2
1 2
2
2
1
1
( )
1
ijf
j
j
m ijf
j
j
b e
p f
a e













特性⽅程式
y a y v bv n j
j
m
nj n jnj
j
 

 

 
1 1

26
ARオペレータの特性⽅程式
MAオペレータの特性⽅程式
1
1
() 1 0
() 1 0
m
j
j
j
j
j
j
aB aB
bB bB


  
  



a(B)=0の根がすべて単位円外 定常
b(B)=0の根がすべて単位円外 反転可能
0 j g 
1
0
1
0 () i j i i
n i ni n i
b b B bB
y by v






 
 


特性⽅程式
27
の根がすべて単位円内 定常
の根がすべて単位円内 反転可能
2
i i re f    

   
1
0
m
m mj
j
j
  a 

  
に関する⽅程式の⽅が便利
本講義ではこちらを特性⽅程式とよぶ
1
1
0
0
m
m mj
j
j
m j
j
j
a
b
 
 




 
 





r
特性⽅程式
28
2
i i re f    

   

r
1 2
1 2
1 2 12
( ) 0.9 3 0.81
(2) 0.9 2 0.81
(3) 0.9 3 0.81 0.9 2 0.81
n n nn
nn n n
n n nn n n
y y yv
yv v v
y yy v vv
 
 
  
 
 
   
１
定常性の条件
特性⽅程式
n n m n m n y  a y   a y   1 1  
0 1  1     m n n  a y  a
a(B)に関する特性⽅程式
の根がすべて単位円内
29
定常性の条件： 例
m

1
m

2
| | 1
0
1
1
1






a
a
a


2
1 2
2
11 2
0
4
2
a a
aaa
 

 
 

30
共役複素数の場合
実数２個の場合
定常性の条件：例
m  2
2
4 2 2 a1  a1  a  
2
1 2 a a   4 0 のとき
2 4 2 2 2   a1  a1  a 
2 1 2 1
2
2 1
2
1 1 a  a  4a  2  a  4a  2  a  a  1  a
2 1 2 1
2
2 1
2
1 1 a  a  4a  2  a  4a  a  2  a  1  a
2
1 2 a a   4 0 のとき
| | 1 ( 4 ) 4 1 2 2 21 2    a1  a  a   a  
31
定常性の条件：例
m

2
2
1 2 a a   4 0 のとき
a
2

1

a
1
a
2

1

a
1
2
1 2 a a   4 0 のとき
a
2


1
-2 -1 1 2
-1
1
0
32
2
a
1 a
複素根
実 根
ライン状のスペクトル
33
n n nnn n 1 1 2 2 11 2 2
y
a
y
a
y v bv b v       
2
1 2
2
1 2
0.99 2 0.99
0.95 2 0.95
a a
b b
 
 
0.99, 45
0.95, 45
°
°
r
r




 
a
(B)=0,
b
(B)=0 の根の
 が同じ場合
# AR model : y(n) = 0.9sqrt(3)y(n-1) - 0.81y(n-2) + v(n)
z <- armaimp(arcoef=a, v=1.0, n=1000, lag=20)
z$croot.ar
Rによる計算：AR(2)モデル
34
インパルス応答関数 ⾃⼰共分散関数
PARCOR パワースペクトル
特性根
# MA model : y(n) = v(n) -0.9sqrt(2)v(n-1) + 0.81v(n-2)
z <- armaimp(macoef=b, v=1.0, n=1000, lag=20)
z$croot.ma
Rによる計算： MA(2)モデル
35
インパルス応答関数 ⾃⼰共分散関数
PARCOR パワースペクトル
特性根
Rによる計算： ARMA(2,2)モデル
# ARMA model : y(n) = 0.9sqrt(3)y(n-1) - 0.81y(n-2)
# + v(n) -0.9sqrt(2)v(n-1) + 0.81v(n-2)
a <- c(0.9*sqrt(3), -0.81)
b <- c(0.9*sqrt(2), -0.81)
z <- armaimp(arcoef=a, macoef=b, v=1.0, n=1000, lag=20)
z$croot.ar
z$croot.ma
36
インパルス応答関数 ⾃⼰共分散関数
PARCOR パワースペクトル
特性根
# ARMA model : y(n) = 0.99sqrt(2)y(n-1) - 0.99^2y(n-2)
# + v(n) -0.95sqrt(2)v(n-1) + 0.95^2v(n-2)
a <- c(0.99*sqrt(2), -0.9801)
b <- c(0.95*sqrt(2), -0.9025)
z <- armaimp(arcoef=a, macoef=b, v=1.0, n=1000, lag=20)
z$croot.ar
z$croot.ma
ARMA(2,2)モデル
AR part
MA part
37
インパルス応答関数 ⾃⼰共分散関数
PARCOR パワースペクトル
特性根
多変量⾃⼰回帰モデル（MAR, VAR Model)
1
m
n j nj n
j
y Ay v 




(1,1) (1, )
( ,1) ( , )
j j
j
j j
a a
A
a a

        


 



11 1
1
0
[] , [ ]
0
[ ]
[ ]
T
n n n ij ji
T
n m
T
n m
Ev Evv W
Evv O n m
Evy O n m
 


 
     
           
 
 

 

  

38
( ,, ) (1) ( )
T
nn n yy y 


 変量時系列
v
n :  変量正規⽩⾊雑⾳
v
nは⾃分⾃⾝と独⽴（⽩⾊）
v
n
は
y
n の過去と独⽴
 多変量ARMAモデルも同様に定義できる
相互共分散関数
(1,1) (1, )
( ,1) ( , )
k k
k
k k
C C
C
C C
   
      

 



39
(, ) () ( ) [ ]
[ ]
k n nk
T
k n nk
C Ey y ij i j
C Eyy




0
1
1
( 1, 2, )
m
j j
j
m
k j kj
j
C AC W
C AC k




 
 

 
Yule-Walker⽅程式
1
m
n j nj n
j
y Ay v 

  
多変量ARモデル
(1,1) (1, )
( ,1) ( , )
k k
k
k k
a a
A
a a
   
      

 



クロススペクトル
40
2 ( ) (, )
( , ) cos 2 ( , )sin 2
ikf
sj k
k
k k
k k
p f C s je
C s j ikf i C s j ikf

 



 
 

 

 
1
2
1
2
2
2
( )
( )
ikf
k
k
ikf
k
f
f
P Ce
C P e df










11 1
1
() ()
( )
() ()
m
m mm
pf p f
P f
pf p f
   
      



1 1* P A WA () () () ff f ( )   
1
, ~ (0, )
m
n j nj n n
j
y Ay v v N W 

  
yn が多変量ARモデルに従うとき 11 1
1
2
0
0
() ()
( )
() ()
( ) (,)
m
m mm
m
ijf
jk j
j
f f
f
f f
f
A A
A
A A
A a jke
a I
 

   
      

 




クロススペクトル
41
2 2
( )
2
() () ()
( ) arctan ( ) / ( )
() ()
( ) coh ( ) () ()
jk
jk jk jk
jk jk jk
i f
jk jk
jk
jk
jj kk
f cf df
f dfcf
p f fe
f
f p fp f





 



() () () jk jk jk p f c f id f 

( ) jk p
f
( ) jk c
f
( ) jk d
f
( ) jk 
f
( ) jk 
f
( )
( )
( )
coh ( )
jk
jk
jk
jk
f
f
p f
f


振幅スペクトル
位相スペクトル
クロススペクトル
コヒーレンシー
インパルス応答関数
B
A
A
A
B
A
B
インパルス応答関数（開ループ）
ステップ応答関数
フィードバックシステム インパルス応答関数（開ループ）
42
フィードバックシステムの解析
43
A
B
n y
nx
n u
nv
フィードバックシステム
・農業⽣産物の⽣産量と価格
・⽯油価格とエコカーの販売量など
周波数応答関数ではフィードバックシステム
の解析は困難（
u
nが⽩⾊雑⾳でない限り
un
と
xn
は無相関とならない）
⼯学的システム以外ではフィードバックを切
断して実験を⾏うのは困難
2変量（
x
n
と
y
n）の場合
⼀般の場合（省略）
2変量フィードバックシステム
44
1
1
n j nj n
j
n j nj n
j
y ax u
x by v












aj Aのインパルス応答関数
bj Bのインパルス応答関数
u
n, v
n 互いに無相関な外乱
 問題
x
n
と
y
nの観測値からインパルス応答関数
aj,
bj および外乱
u
n, v
n の特性を推定
 ⽩⾊化の必要性
通常の最⼩⼆乗法では，
x
n
と
u
nに相関があるために良い
推定値が得られない．

u
n
と
v
nをARモデルにより⽩⾊化する
1 1
, n j nj n n jnj n
j j
u cu v dv 

 
 
 
  
2変量フィードバックシステム
45
1
1
n j nj n
j
n j nj n
j
y ax u
x by v






 
 


1
1
n i ni n
i
n i ni n
i
u cu
v dv








 
 


1
n n j nj
j
u y ax



 

1
1 1
1
(1,1) ,( 1, 2,...), (1, 2) , (1, 2)
j
j j j j i ji
i
a c
j a a a a ca



   

1 1
1 1
(1,1) (1, 2)
(2,1) (2,2)
n j n j j ni n
j j
n j n j j ni n
j j
y ay a x
x ay a x


 
 
 
 
 
 


 
 
111
1 1 11
( ) n j n j i ni j ni j n
jij
n i ni j n j i j ni j n
i j ii
y ax c y ax
y cy a x ca x



  
 
  
  
  
 
  

  
2変量ARモデル！
ただし，変数間に
制約あり
j m
1,

モデルを求める⽅法
46
1
(1,1) (1, 2)
(2,1) (2, 2)
m
n n j j nj
n n j j j nj
y aa y
x aa x





     
       
     

１．2変量ARモデル
２．ノイズ
u
n
と
v
nのモデル
(1,1), (2, 2) jj jj ca da  
３．A，Bのインパルス応答関数
1 1
1 1
1 1
1 1
(1, 2) , ( 2, , ), , ( 1, )
(2,1) , ( 2, , ), , ( 1, )
m m
j j i ji j i ji
i i
m m
j j i ji j i ji
i i
a a ca j m a ca j m
b a db j m b db j m
 
 
 
 
 
 
    
    
 
 
 
 
周波数応答関数
47
2 2
1 1
1 1
2 2
() , () ,
m m
ijf ijf
j j
j j
A f ae B f be f    
 
     
周波数応答関数
外乱のパワースペクトル
2 2
22 22
1 1
() , ()
|1 |1 | |
vv uu
vv uu m m
ijf ijf
j j
j j
pf pf
ce de  
 
 
 
 
   
閉ループの周波数応答関数（un から xn および vn から xn）
2 1
2 1
1 ( ) ( ) ( ( ) ( )) (1 ( ) ( ))
( ) ( ) ( ) ( ) ( )( ( ) ( )) ( )(1 ( ) ( ))
Bf Af Bf Af Bf Af
A f AfBf Af Af Bf Af Af Bf Af


   
   


1 1 1
11 12
1 1
21 22
( )(1 ( ) ( ))
( )(1 ( ) ( ))
(1 ( ) ( ))
(1 ( ) ( ))
1 ()
() 1
Bf Af Bf
Af Bf Af
Af Bf
Bf Af
B f c c
A f c c

 
 




                     
パワースペクトルの分解
48
y
n
と
x
nのパワースペクトル
2 2
11 12
2 2
21 22
( ) | | ( ) | | ( )
( ) | | ( ) | | ( )
yy vv uu
xx vv uu
p
f c p
f c p
f
p
f c p
f c p
f
 
 
パワー寄与率
1 1 1
11 12
1 1
21 22
( )(1 ( ) ( ))
( )(1 ( ) ( ))
(1 ( ) ( ))
(1 ( ) ( ))
1 ()
() 1
Bf Af Bf
Af Bf Af
Af Bf
Bf Af
B f c c
A f c c

 
 




    

             


2 2
11 12
2 2
21 22
| | () | | () () , () () ()
| | () | | () () , () () ()
vv uu
yv yu
yy yy
vv uu
xv xu
xx xx
c pf c pf rf p f pf pf
c pf c pf rf p f pf pf
 
 
パワー寄与率
49
2 * 22
1 1
2 2
2 2
1
1
( ) ( ) ( ) | ( )|
| ( )| ( ) ( )
| ( )|
() () ( )
ii ij j ij ij j
j j
ij j
ij
ii
j
j ik k
k
ij ik
k ii
pf bf bf bf
b f r f p f
b f
sf rf p f
 


 


 

 
 


 
 パワースペクトルをノイズソース毎に分解したもの
 どのノイズに起因するものかが分かる
 ノイズの直交性を仮定している
 ノイズに相関がある場合：⼀般パワー寄与率
パワースペクトル
パワーの分解
パワー寄与率
パワー寄与率
50
51
船体運動データ（５変量）
5変量（⽅向⾓速度，横揺れ，縦揺れ，回転数，舵⾓）
52
Autopilot Control Manual Control
data(HAKUSAN)
length <- dim(HAKUSAN)[1]
y <- matrix(, length/2, 3)
for( i in 1:length/2) {
y[i,1] <- HAKUSAN[i*2,1] # yaw rate
y[i,2] <- HAKUSAN[i*2,2] # rolling
y[i,3] <- HAKUSAN[i*2,4] # rudder
marfit(y,20) # Yule-Walker法
marlsq(y,20) ＃ 最⼩⼆乗法
クロススペクトル
対⾓線：スペクトル
上：振幅スペクトル
下：位相スペクトル
⽅向⾓速度
舵⾓
縦揺れ
⽅向⾓速度 縦揺れ 舵⾓
53
パワースペクトルとコヒーレンシー
対⾓線：パワースペクトル
上： コヒーレンシー
⽅向⾓速度 縦揺れ 舵⾓
⽅向⾓速度
舵⾓
縦揺れ
54
パワー寄与率
方向角速度
方向角速度
舵角
舵角
⽅向⾓速度
舵⾓
縦揺れ
パワー分解 パワー寄与率
55
0.0 0.1 0.2 0.3 0.4 0.5
パワー寄与率
マネタリーベース 国債⾦利
卸売物価 鉱⼯業⽣産指数
機械受注 為替相場
為替相場
機械受注
⾦利
⾦利
為替
⾦利
IIP
受注
為替
物価
IIP
0.0 0.1 0.2 0.3 0.4 0.5
0.0 0.1 0.2 0.3 0.4 0.5 0.0 0.1 0.2 0.3 0.4 0.5
0.0 0.1 0.2 0.3 0.4 0.5 0.0 0.1 0.2 0.3 0.4 0.5
マネタリー
ベース
IIP
56
```
