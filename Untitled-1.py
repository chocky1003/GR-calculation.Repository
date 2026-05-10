import sympy
from einsteinpy.symbolic import MetricTensor

# 1. 座標と物理定数の定義
# 物理学徒になじみ深い t, r, theta, phi と rs (シュヴァルツシルト半径) を定義します
t, r, theta, phi = sympy.symbols('t r theta phi')
rs = sympy.symbols('r_s')

# 2. 計量成分 g_uv のリストを作成
# ds^2 = -(1 - rs/r)dt^2 + (1/(1 - rs/r))dr^2 + r^2*dtheta^2 + r^2*sin^2(theta)*dphi^2
m_list = [[0 for _ in range(4)] for _ in range(4)]
m_list[0][0] = -(1 - rs/r)
m_list[1][1] = 1 / (1 - rs/r)
m_list[2][2] = r**2
m_list[3][3] = r**2 * sympy.sin(theta)**2

# 3. EinsteinPyのMetricTensorオブジェクトを作成
# これにより、クリストッフェル記号やリーマンテンソルへの計算の準備が整います
metric = MetricTensor(m_list, (t, r, theta, phi))

# 4. 行列形式で表示
# sympy.pprint と sympy.Matrix を組み合わせることで、
# 4x4 行列として視覚的に分かりやすく出力します
print("Schwarzschild Metric Tensor g_μν:")
#sympy.pprint(sympy.Matrix(metric.tensor))
#sympy.pprint(sympy.Matrix(metric.tensor.tolist()))
#sympy.pprint(metric.to_matrix())
# metric.tensor を経由せず、定義した m_list を直接使う
sympy.pprint(sympy.Matrix(m_list))