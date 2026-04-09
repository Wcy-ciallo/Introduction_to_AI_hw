# Homework 1

人工智能导论第一次作业。

## 作业内容

使用 Python 实现以下内容：

- 图 `Graph`
- 树 `Tree`
- 栈 `Stack`
- 队列 `Queue`
- 优先队列 `PriorityQueue`
- 深度优先搜索 `DFS`
- 广度优先搜索 `BFS`
- 一致代价搜索 `UCS`

并对 DFS、BFS、UCS 的完备性、最优性、时间复杂度和空间复杂度进行说明。

## 目录结构

- `code/`：作业代码
- `doc/`：作业文档
- `hw.jpg`：题目图片
- `report.md`：作业说明草稿
- `step.md`：实现过程记录

## 代码说明

`code/data_structures/` 中包含：

- `Graph.py`
- `Tree.py`
- `Stack.py`
- `Queue.py`
- `PriorityQueue.py`

`code/search.py` 中实现了：

- `dfs`
- `bfs`
- `ucs`

`code/main.py` 用于构造测试图并运行三种搜索算法。

## 运行方式

在仓库根目录下执行：

```bash
python hw1\code\main.py
```

## 说明

本作业中的图采用邻接表实现，优先队列采用手写顺序查找最小优先级元素的方式实现，没有依赖现成堆结构库。
