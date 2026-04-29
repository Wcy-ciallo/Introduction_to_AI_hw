# 第二次作业

本次作业内容来自当前目录下的 `hw.png`，使用 Python 完成两个任务：

1. α-β 剪枝
2. 中国地图着色 CSP

实现参考说明见 [GUIDE.md](GUIDE.md)。

## 目录结构

```text
hw2/
├── README.md
├── GUIDE.md
├── hw.png
├── code/
│   ├── alpha_beta.py
│   └── csp.py
└── doc/
    └── readme.docx
```

## 任务一：α-β 剪枝

### 任务要求

根据题目图片右侧的博弈树，实现 α-β 剪枝算法。

需要输出：

- 最终结果节点或路径
- 被剪枝的节点

### 实现文件

代码位于：

```text
code/alpha_beta.py
```

### 实现说明

程序使用 `Node` 类表示博弈树节点。节点类型包括：

- `max`：Max 节点
- `min`：Min 节点
- `leaf`：叶子节点

`build_game_tree()` 按照题目图片中从左到右的顺序构建完整博弈树。`alpha_beta()` 递归计算节点值，并在搜索过程中维护 `alpha` 和 `beta`。当出现 `alpha >= beta` 时，说明当前节点后续兄弟节点不会影响最终选择，因此进行剪枝。

程序会记录：

- 最终值
- 最终路径
- 被剪枝的节点
- 被剪枝的叶子节点

### 运行方式

在仓库根目录下执行：

```bash
python hw2/code/alpha_beta.py
```

### 当前运行结果

```text
Alpha-Beta 剪枝结果
最终值: 3
最终路径: Root -> Left -> L3 -> H
被剪枝的节点: ['F', 'L', 'N', 'P', 'T']
被剪枝的叶子节点: ['F', 'L', 'N', 'P', 'T']
```

## 任务二：中国地图着色

### 任务要求

使用 Python 实现中国地图着色问题。

要求：

1. 将省、自治区、直辖市、特别行政区作为图中的节点。
2. 将陆地相邻关系作为相邻边。
3. 使用 5 种颜色完成地图着色。
4. 加入弧相容性检查。

### 实现文件

代码位于：

```text
code/csp.py
```

### 实现说明

中国地图着色问题被建模为约束满足问题，即 CSP。

- 变量：省级行政区
- 取值域：`red`、`green`、`blue`、`yellow`、`purple`
- 约束：陆地相邻的两个行政区不能使用相同颜色

程序中：

- `REGIONS` 保存所有省级行政区。
- `ADJACENT_PAIRS` 保存陆地相邻关系。
- `build_neighbors()` 根据相邻边生成双向邻接表 `NEIGHBORS`。
- `build_domains()` 为每个行政区初始化 5 种颜色。
- `is_consistent()` 判断当前颜色是否与已赋值邻居冲突。
- `select_unassigned_region()` 选择下一个未赋值地区。
- `revise()` 和 `ac3()` 实现弧相容性检查。
- `forward_check()` 在赋值后更新邻居颜色域。
- `backtrack()` 使用回溯搜索寻找合法染色方案。
- `validate_solution()` 检查最终结果是否合法。

海南和台湾在本实现中没有省级陆地相邻行政区，因此它们在邻接表中的邻居为空。

### 运行方式

在仓库根目录下执行：

```bash
python hw2/code/csp.py
```

### 当前运行结果

程序可以输出一组合法的五色染色方案，并通过合法性检查：

```text
检查结果:  True
```

其中一次运行得到的染色结果为：

```text
北京: red
天津: green
河北: blue
山西: red
内蒙古: green
辽宁: red
吉林: blue
黑龙江: red
上海: blue
江苏: green
浙江: red
安徽: blue
福建: blue
江西: green
山东: red
河南: green
湖北: red
湖南: blue
广东: red
广西: green
海南: red
重庆: green
四川: blue
贵州: red
云南: yellow
西藏: red
陕西: yellow
甘肃: red
青海: green
宁夏: blue
新疆: blue
香港: green
澳门: green
台湾: red
```

## 语法检查

可以使用以下命令检查代码语法：

```bash
python -m py_compile hw2/code/alpha_beta.py hw2/code/csp.py
```
