#!/Users/sorakojima/miniforge3/envs/python39/bin/python3
#%%
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
# %%
def plot_graph(X, Y, x, y):
    fig, ax = plt.subplots(dpi=100)
    ax.set_title('最高気温とアイスクリーム・シャーベットの支出額')
    ax.set_xlabel('最高気温の月平均（℃）')
    ax.set_ylabel('支出額（円）')
    ax.set_xlim(0, 35)
    ax.set_ylim(-250, 2000)
    ax.grid()
    ax.scatter(X, Y, marker='.')
    ax.plot(x, y, 'r')
    fig.show()

X = np.array([
     9.1, 11.2, 12.3, 18.9, 22.2, 26. , 30.9, 31.2, 28.8, 23. , 18.3,
    11.1,  8.3,  9.1, 12.5, 18.5, 23.6, 24.8, 30.1, 33.1, 29.8, 23. ,
    16.3, 11.2,  9.6, 10.3, 16.4, 19.2, 24.1, 26.5, 31.4, 33.2, 28.8,
    23. , 17.4, 12.1, 10.6,  9.8, 14.5, 19.6, 24.7, 26.9, 30.5, 31.2,
    26.9, 23. , 17.4, 11. , 10.4, 10.4, 15.5, 19.3, 26.4, 26.4, 30.1,
    30.5, 26.4, 22.7, 17.8, 13.4, 10.6, 12.2, 14.9, 20.3, 25.2, 26.3,
    29.7, 31.6, 27.7, 22.6, 15.5, 13.8, 10.8, 12.1, 13.4, 19.9, 25.1,
    26.4, 31.8, 30.4, 26.8, 20.1, 16.6, 11.1,  9.4, 10.1, 16.9, 22.1,
    24.6, 26.6, 32.7, 32.5, 26.6, 23. , 17.7, 12.1, 10.3, 11.6, 15.4,
    19. , 25.3, 25.8, 27.5, 32.8, 29.4, 23.3, 17.7, 12.6, 11.1, 13.3,
    16. , 18.2, 24. , 27.5, 27.7, 34.1, 28.1, 21.4, 18.6, 12.3])

Y = np.array([
    463.,  360.,  380.,  584.,  763.,  886., 1168., 1325.,  847.,
    542.,  441.,  499.,  363.,  327.,  414.,  545.,  726.,  847.,
   1122., 1355.,  916.,  571.,  377.,  465.,  377.,  362.,  518.,
    683.,  838., 1012., 1267., 1464., 1000.,  629.,  448.,  466.,
    404.,  343.,  493.,  575.,  921., 1019., 1149., 1303.,  805.,
    739.,  587.,  561.,  486.,  470.,  564.,  609.,  899.,  946.,
   1295., 1325.,  760.,  667.,  564.,  633.,  478.,  450.,  567.,
    611.,  947.,  962., 1309., 1307.,  930.,  668.,  496.,  650.,
    506.,  423.,  531.,  672.,  871.,  986., 1368., 1319.,  924.,
    716.,  651.,  708.,  609.,  535.,  717.,  890., 1054., 1077.,
   1425., 1378.,  900.,  725.,  554.,  542.,  561.,  459.,  604.,
    745., 1105.,  973., 1263., 1533., 1044.,  821.,  621.,  601.,
    549.,  572.,  711.,  819., 1141., 1350., 1285., 1643., 1133.,
    784.,  682.,  587.])
# %%
W = np.polyfit(X, Y, 2)
W
# %%
x = np.linspace(0, 35, 100)
y_hat = np.polyval(W, x)
plot_graph(X, Y, x, y_hat)
# %%
W = np.polyfit(X, Y, 3)
W
# %%
x = np.linspace(0, 35, 100)
y_hat = np.polyval(W, x)
plot_graph(X, Y, x, y_hat)
#%%
W = np.polyfit(X, Y, 4)
W
# %%
x = np.linspace(0, 35, 100)
y_hat = np.polyval(W, x)
plot_graph(X, Y, x, y_hat)

# %%
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
# %%
reg = make_pipeline(PolynomialFeatures(3), LinearRegression())
reg.fit(X.reshape(-1, 1), Y)
# %%
reg[1].coef_
# %%
reg[1].intercept_
# %%
reg.score(X.reshape(-1, 1), Y)
# %%
x = np.linspace(0, 35, 100)
y_hat = reg.predict(x.reshape(-1, 1))
plot_graph(X, Y, x, y_hat)

# %%##############################################################################
##################################################################################
##################################################################################

# 2.10 確認問題
D = np.array([[1,3], [3,6], [6,5], [8,7]])
D
# (1) 行列による1次関数のパラメータ推定
#   y = w0 + (w1 * x) とおき，学習データDs上の平均二乗残差を最小にする
#   w = (w0, w1) を行列演算により求めよ

# (2) 二次関数による重回帰
#   y = w0 + (w1 * x) + (w2 * x^2)と置き，重回帰により平均二乗残差を最小にする
#   w = (w0, w1, w2) を求めよ 

# (3) 回帰直線の描画
#   回帰で求めた二次関数をデータ点とともにグラフに描け

# (4) 決定係数
#   回帰で得られて2次関数の決定係数（R^2）を求めよ

# (5) 3次関数による重回帰
#   y = w0 + w1x + w2x^2 + w3x^3とおき，重回帰により平均二乗残差を最小にする
#   w = (w0, w1, w2, w3)を求めよ

# (6) 回帰曲線の描画
#   回帰で求めた3次関数をデータ点とともにグラフに描け

# (7) 決定係数
#   回帰で求めた3次関数の決定係数（R^2）を求めよ
# %%
def Cov(x, y):
    return np.mean(x*y) - np.mean(x)*np.mean(y)
def Var(x):
    return np.sum((x-np.mean(x))**2)
# %%
# (1)
x = D[:,0]
y = D[:,1]

X = np.array([[1,x[0]], [1, x[1]], [1, x[2]], [1, x[3]]])
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f'(1)\n y = w0 + (w1 * x)と置いたときのw0とw1はそれぞれ，\n{w}')
# %% (2)
X = np.array([[1,1,1],
              [1,3,9], 
              [1,6,36], 
              [1,8,64]])
y = np.array([3, 6, 5, 7])
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f'(2)\n y = w0 + (w1 * x) + (w2 * x^2)と置いたときのw0,w1,w2はそれぞれ,\n{w}')
# %% (3)
fig, ax = plt.subplots()
xs = np.linspace(0, 10, 100)
y_hat = w[0] + w[1]*xs + w[2]*xs**2
ax.plot(xs, y_hat)
ax.scatter(x, y, color='red')
ax.grid()
ax.set_title('図1．確認問題（3）の回答．\n 2次関数での重回帰曲線')
ax.set_xlabel('x軸')
ax.set_ylabel('y軸')
plt.show()

# %% (4)
eps = y - X@w
R_squared = 1 - Var(eps) / Var(y)
print(f'(4) 決定係数 R^2 = {R_squared}')
# %% (5)
X = np.array([[1,1,1**2,1**3],
              [1,3,3**2,3**3],
              [1,6,6**2,6**3],
              [1,8,8**2,8**3]])
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(f'(5)\n y = w0 + w1x + w2x^2 + w3x^3と置いたときのw0,w1,w2,w3はそれぞれ，\n{w}')

# %% (6)
fig, ax = plt.subplots()
xs = np.linspace(0, 10, 100)
y_hat = w[0] + w[1]*xs + w[2]*xs**2 + w[3]*xs**3
ax.plot(xs, y_hat)
ax.scatter(x, y, color='red')

ax.grid()
ax.set_title('図2．確認問題（6）の回答．\n3次関数での重回帰曲線')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')

plt.show()
# %% (7)
eps = y - X@w
R_squared = 1 - Var(eps) / Var(y)
print(f'(7) 決定係数 R^2 = {R_squared}')
# %%
