# 作业实现指南

本文档说明如何使用 Python 完成本次作业。实现时建议将代码拆分到 `src/` 目录中，便于分别实现和测试 α-β 剪枝、中国地图着色、弧相容性检查等功能。

## 一、推荐项目结构

建议使用如下目录结构：

```text
hw2/
├── README.md
├── IMPLEMENTATION_GUIDE.md
├── hw.png
├── src/
│   ├── alpha_beta.py
│   ├── map_coloring.py
│   └── main.py
└── tests/
    ├── test_alpha_beta.py
    └── test_map_coloring.py
```

各文件职责如下：

- `src/alpha_beta.py`：实现博弈树建模和 α-β 剪枝算法。
- `src/map_coloring.py`：实现中国地图着色、回溯搜索和弧相容性检查。
- `src/main.py`：统一运行两个任务，并打印结果。
- `tests/`：可选，用于验证算法结果是否正确。

## 二、任务一：α-β 剪枝实现步骤

### 1. 明确问题目标

本任务需要根据作业图中的博弈树，实现 α-β 剪枝算法，并输出：

1. 根节点最终得到的结果值。
2. 最终结果对应的节点或路径。
3. 搜索过程中被剪枝的节点。

图中：

- `△` 表示 Max 节点，目标是选择子节点中的最大值。
- `▽` 表示 Min 节点，目标是选择子节点中的最小值。
- 叶子节点有固定效用值，例如 `A = 15`、`B = 9`。

### 2. 设计树节点数据结构

可以定义一个 `Node` 类表示博弈树节点。

建议字段：

- `name`：节点名称，例如 `"A"`、`"Root"`、`"L1"`。
- `node_type`：节点类型，可取 `"max"`、`"min"`、`"leaf"`。
- `value`：叶子节点的效用值，非叶子节点初始为 `None`。
- `children`：子节点列表。

示例结构：

```python
class Node:
    def __init__(self, name, node_type, value=None, children=None):
        self.name = name
        self.node_type = node_type
        self.value = value
        self.children = children or []
```

### 3. 按图片建立博弈树

按照 README 中的 Mermaid 图，从左到右建立树结构。

叶子节点效用值如下：

```python
A = Node("A", "leaf", 15)
B = Node("B", "leaf", 9)
C = Node("C", "leaf", 5)
D = Node("D", "leaf", 7)
E = Node("E", "leaf", 1)
F = Node("F", "leaf", -2)
G = Node("G", "leaf", -1)
H = Node("H", "leaf", 3)
I = Node("I", "leaf", 6)
J = Node("J", "leaf", 3)
K = Node("K", "leaf", 8)
L = Node("L", "leaf", 1)
M = Node("M", "leaf", -1)
N = Node("N", "leaf", 4)
O = Node("O", "leaf", 1)
P = Node("P", "leaf", 6)
Q = Node("Q", "leaf", 12)
R = Node("R", "leaf", 10)
S = Node("S", "leaf", 14)
T = Node("T", "leaf", 7)
U = Node("U", "leaf", 3)
V = Node("V", "leaf", 2)
```

然后从底向上组合非叶子节点。例如左侧第一棵子树可以写成：

```python
left_1 = Node("L1", "max", children=[A, B])
left_2_1 = Node("L21", "min", children=[C, D])
left_2_2 = Node("L22", "min", children=[E, F])
left_2 = Node("L2", "max", children=[left_2_1, left_2_2])
left_3 = Node("L3", "max", children=[G, H])
left = Node("Left", "min", children=[left_1, left_2, left_3])
```

中间和右侧子树同理，最后建立根节点：

```python
root = Node("Root", "max", children=[left, middle, right])
```

按照图中的结构从左到右搜索时，完整博弈树的根节点结果值应为 `3`。如果遇到相同值时保留最先找到的路径，则最终路径应为：

```text
Root -> Left -> L3 -> H
```

按标准 α-β 剪枝、从左到右展开时，预计被剪枝的叶子节点包括：

```text
F, L, N, P, T
```

这组结果可以作为程序实现后的参考检查。若你的程序在相同树结构和相同搜索顺序下得到不同结果，应优先检查节点类型、子节点顺序和 `alpha >= beta` 的剪枝条件。

### 4. 实现 α-β 剪枝函数

函数接口建议如下：

```python
def alpha_beta(node, alpha=float("-inf"), beta=float("inf"), pruned=None):
    ...
```

参数含义：

- `node`：当前搜索节点。
- `alpha`：当前 Max 路径上已知的最好值。
- `beta`：当前 Min 路径上已知的最好值。
- `pruned`：用于记录被剪枝节点名称的列表。

基本逻辑：

1. 如果当前节点是叶子节点，直接返回该叶子的效用值。
2. 如果当前节点是 Max 节点：
   - 初始化 `best_value = -inf`。
   - 依次遍历子节点。
   - 递归计算子节点值。
   - 更新 `best_value = max(best_value, child_value)`。
   - 更新 `alpha = max(alpha, best_value)`。
   - 如果 `alpha >= beta`，说明后续兄弟节点不会影响上层 Min 节点选择，可以剪枝。
3. 如果当前节点是 Min 节点：
   - 初始化 `best_value = inf`。
   - 依次遍历子节点。
   - 递归计算子节点值。
   - 更新 `best_value = min(best_value, child_value)`。
   - 更新 `beta = min(beta, best_value)`。
   - 如果 `alpha >= beta`，说明后续兄弟节点不会影响上层 Max 节点选择，可以剪枝。

### 5. 记录被剪枝节点

当发生剪枝时，需要记录当前节点后面尚未搜索的兄弟节点。

例如正在遍历 `children`，如果第 `i` 个子节点计算后触发剪枝，则 `children[i + 1:]` 都是被剪枝的节点。

可以写一个辅助函数收集被剪枝节点名称：

```python
def collect_leaf_names(node):
    if node.node_type == "leaf":
        return [node.name]

    result = []
    for child in node.children:
        result.extend(collect_leaf_names(child))
    return result
```

如果要求输出被剪枝的“节点”，可以记录被剪掉的子树根节点名称；如果要求输出被剪枝的“叶子”，可以记录整棵被剪子树下的所有叶子节点名称。为了结果更清楚，建议同时输出：

- 被剪枝的子树根节点。
- 被剪枝子树包含的叶子节点。

### 6. 返回最终结果节点

除了返回最终值，还需要知道最终选择的是哪个节点或路径。

可以让递归函数返回二元组：

```python
return best_value, best_path
```

其中 `best_path` 是从当前节点到最终叶子节点的路径，例如：

```python
["Root", "...", "<Leaf>"]
```

Max 节点选择值最大的子节点路径，Min 节点选择值最小的子节点路径。

### 7. 输出格式建议

程序运行后可以输出：

```text
Alpha-Beta 剪枝结果
最终值: <程序计算出的根节点值>
最终路径: Root -> ... -> <最终叶子节点>
被剪枝的节点: ...
被剪枝的叶子节点: ...
```

最终值和路径需要以实际程序运算结果为准，不要手写固定答案。

### 8. 测试建议

至少测试以下内容：

1. 根节点返回值是否正确。
2. 最终路径是否是合法路径。
3. 被剪枝节点是否与从左到右搜索顺序一致。
4. 空树或单叶子树是否能正确处理。

## 三、任务二：中国地图五色着色实现步骤

### 1. 明确问题目标

本任务要求用 Python 实现中国地图着色：

1. 将省、自治区、直辖市、特别行政区作为节点。
2. 将陆地相邻关系作为边。
3. 使用 5 种颜色着色。
4. 加入弧相容性检查。

这是一个典型的约束满足问题，也就是 CSP。

### 2. 定义 CSP 中的基本概念

可以这样建模：

- 变量：每个省级行政区。
- 取值域：每个变量都可以选择 5 种颜色之一。
- 约束：相邻行政区不能使用相同颜色。
- 目标：给每个行政区分配一种颜色，并满足所有相邻约束。

示例颜色：

```python
COLORS = ["red", "green", "blue", "yellow", "purple"]
```

### 3. 建立行政区列表

可以先建立省级行政区列表：

```python
REGIONS = [
    "北京", "天津", "河北", "山西", "内蒙古",
    "辽宁", "吉林", "黑龙江",
    "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东",
    "河南", "湖北", "湖南", "广东", "广西", "海南",
    "重庆", "四川", "贵州", "云南", "西藏",
    "陕西", "甘肃", "青海", "宁夏", "新疆",
    "香港", "澳门", "台湾",
]
```

是否将海上相邻关系算作相邻边，需要根据作业要求决定。题目写的是“陆地邻接为相邻边”，因此只应加入陆地接壤关系。

### 4. 建立邻接表

使用字典表示地图图结构：

```python
NEIGHBORS = {
    "北京": ["天津", "河北"],
    "天津": ["北京", "河北"],
    "河北": ["北京", "天津", "山西", "内蒙古", "辽宁", "山东", "河南"],
    ...
}
```

注意事项：

1. 邻接关系应是双向的。
2. 如果 `"北京"` 中包含 `"河北"`，则 `"河北"` 中也应该包含 `"北京"`。
3. 香港、澳门与广东陆地相邻。
4. 台湾、海南如果只考虑陆地邻接，可以没有陆地相邻省份。

为了避免手写时漏掉反向边，可以先写边列表：

```python
EDGES = [
    ("北京", "天津"),
    ("北京", "河北"),
    ("天津", "河北"),
    ...
]
```

再用代码生成双向邻接表：

```python
def build_neighbors(regions, edges):
    neighbors = {region: [] for region in regions}
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    return neighbors
```

### 5. 定义取值域

每个行政区初始都有 5 种颜色可选：

```python
def create_domains(regions, colors):
    return {region: colors[:] for region in regions}
```

得到的数据结构示例：

```python
{
    "北京": ["red", "green", "blue", "yellow", "purple"],
    "天津": ["red", "green", "blue", "yellow", "purple"],
    ...
}
```

### 6. 实现约束检查

当给某个行政区赋值时，需要检查它和已赋值邻居是否颜色不同。

```python
def is_consistent(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True
```

参数说明：

- `region`：当前准备赋值的行政区。
- `color`：当前尝试的颜色。
- `assignment`：已经完成的部分赋值。
- `neighbors`：邻接表。

### 7. 实现弧相容性检查 AC-3

弧相容性检查用于提前删除不可能的颜色，减少回溯搜索次数。

对于地图着色问题，任意相邻行政区 `Xi` 和 `Xj` 的约束是：

```text
Xi 的颜色 != Xj 的颜色
```

如果 `Xi` 的某个颜色在 `Xj` 的取值域中找不到任何兼容颜色，则这个颜色应从 `Xi` 的取值域中删除。

AC-3 的核心步骤：

1. 将所有有向弧 `(Xi, Xj)` 加入队列。
2. 从队列中取出一条弧。
3. 调用 `revise(Xi, Xj)` 修剪 `Xi` 的取值域。
4. 如果 `Xi` 的取值域被修改：
   - 如果 `Xi` 的取值域为空，说明无解。
   - 将所有 `(Xk, Xi)` 重新加入队列，其中 `Xk` 是 `Xi` 的其他邻居。
5. 队列为空时，说明当前取值域满足弧相容。

`revise` 函数示例：

```python
def revise(domains, xi, xj):
    revised = False
    for color in domains[xi][:]:
        if not any(color != other_color for other_color in domains[xj]):
            domains[xi].remove(color)
            revised = True
    return revised
```

`ac3` 函数示例：

```python
from collections import deque

def ac3(domains, neighbors):
    queue = deque()

    for xi in neighbors:
        for xj in neighbors[xi]:
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            if not domains[xi]:
                return False

            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True
```

### 8. 在回溯搜索中使用 AC-3

基本回溯搜索流程：

1. 如果所有行政区都已经赋值，返回完整结果。
2. 选择一个尚未赋值的行政区。
3. 遍历它当前可选的颜色。
4. 如果颜色与已赋值邻居不冲突：
   - 复制当前赋值和取值域。
   - 给该行政区赋值。
   - 将该行政区取值域缩小为当前颜色。
   - 运行 AC-3。
   - 如果 AC-3 没有发现冲突，则递归搜索下一步。
5. 如果所有颜色都失败，回溯。

代码框架：

```python
def backtracking_search(assignment, domains, neighbors):
    if len(assignment) == len(domains):
        return assignment

    region = select_unassigned_variable(assignment, domains)

    for color in domains[region]:
        if is_consistent(region, color, assignment, neighbors):
            new_assignment = assignment.copy()
            new_domains = {key: value[:] for key, value in domains.items()}

            new_assignment[region] = color
            new_domains[region] = [color]

            if ac3(new_domains, neighbors):
                result = backtracking_search(new_assignment, new_domains, neighbors)
                if result is not None:
                    return result

    return None
```

### 9. 选择下一个变量

为了减少搜索次数，建议使用 MRV 策略，即优先选择剩余可选颜色最少的未赋值行政区。

```python
def select_unassigned_variable(assignment, domains):
    unassigned = [
        region for region in domains
        if region not in assignment
    ]
    return min(unassigned, key=lambda region: len(domains[region]))
```

也可以进一步加入 Degree 策略：当多个变量剩余颜色数量相同时，优先选择邻居更多的变量。

### 10. 输出地图着色结果

程序运行后建议输出每个行政区对应的颜色：

```text
中国地图五色着色结果
北京: red
天津: green
河北: blue
...
```

同时输出验证信息：

```text
是否满足所有相邻约束: True
使用颜色数量: 5
```

### 11. 验证着色结果

实现一个验证函数，检查所有相邻行政区颜色是否不同：

```python
def validate_coloring(assignment, neighbors):
    for region, region_neighbors in neighbors.items():
        for neighbor in region_neighbors:
            if assignment.get(region) == assignment.get(neighbor):
                return False
    return True
```

如果返回 `True`，说明着色结果满足约束。

## 四、主程序实现步骤

可以在 `src/main.py` 中统一运行两个任务。

推荐流程：

```python
from alpha_beta import build_game_tree, alpha_beta
from map_coloring import solve_map_coloring, validate_coloring


def main():
    root = build_game_tree()
    value, path, pruned = alpha_beta(root)

    print("Alpha-Beta 剪枝结果")
    print("最终值:", value)
    print("最终路径:", " -> ".join(path))
    print("被剪枝节点:", pruned)

    assignment, neighbors = solve_map_coloring()

    print()
    print("中国地图五色着色结果")
    for region, color in assignment.items():
        print(f"{region}: {color}")
    print("是否满足所有相邻约束:", validate_coloring(assignment, neighbors))


if __name__ == "__main__":
    main()
```

## 五、实现顺序建议

建议按以下顺序完成代码：

1. 创建 `src/` 目录。
2. 编写 `alpha_beta.py` 中的 `Node` 类。
3. 根据 README 中的博弈树结构实现 `build_game_tree()`。
4. 实现基础版 `alpha_beta()`，先只返回最终值。
5. 为 `alpha_beta()` 增加最终路径记录。
6. 为 `alpha_beta()` 增加被剪枝节点记录。
7. 编写 `map_coloring.py` 中的行政区、颜色和邻接关系。
8. 实现 `build_neighbors()`。
9. 实现 `is_consistent()`。
10. 实现 `revise()` 和 `ac3()`。
11. 实现 `backtracking_search()`。
12. 加入 MRV 变量选择策略。
13. 实现 `validate_coloring()`。
14. 编写 `main.py` 串联两个任务。
15. 运行程序，检查输出是否满足作业要求。

## 六、运行和检查

如果采用推荐结构，可以在项目根目录运行：

```bash
python src/main.py
```

语法检查：

```bash
python -m py_compile src/*.py
```

如果编写了测试：

```bash
python -m pytest tests
```

## 七、常见问题

### 1. α-β 剪枝结果和别人不同怎么办

首先检查搜索顺序是否一致。本作业应按照图片中从左到右的顺序搜索。α-β 剪枝的剪枝节点依赖搜索顺序，顺序不同，剪枝结果可能不同。

### 2. 被剪枝节点应该输出内部节点还是叶子节点

题目只写“输出被剪枝的节点”，没有进一步限定。建议输出被剪枝的子树根节点，并额外输出该子树下包含的叶子节点，这样最清楚。

### 3. 地图着色中台湾、海南如何处理

题目要求“陆地邻接为相邻边”。如果只考虑陆地相邻，台湾和海南没有省级陆地邻接边，可以作为孤立节点处理。香港、澳门与广东存在陆地邻接，应加入相邻关系。

### 4. 为什么需要 AC-3

普通回溯搜索只在赋值后检查当前冲突。AC-3 会提前根据相邻约束缩小各变量的可选颜色范围，能减少后续搜索分支，也满足题目“加入弧相容性检查”的要求。
