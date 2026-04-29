from math import inf


MAX = "max"
MIN = "min"
LEAF = "leaf"


class Node:
  def __init__(self, name, node_type, value=None, children=None):
    self.name = name
    self.node_type = node_type
    self.value = value
    self.children = children or []


def leaf(name, value):
  return Node(name, LEAF, value=value)


def build_game_tree():
  a = leaf("A", 15)
  b = leaf("B", 9)
  c = leaf("C", 5)
  d = leaf("D", 7)
  e = leaf("E", 1)
  f = leaf("F", -2)
  g = leaf("G", -1)
  h = leaf("H", 3)
  i = leaf("I", 6)
  j = leaf("J", 3)
  k = leaf("K", 8)
  l = leaf("L", 1)
  m = leaf("M", -1)
  n = leaf("N", 4)
  o = leaf("O", 1)
  p = leaf("P", 6)
  q = leaf("Q", 12)
  r = leaf("R", 10)
  s = leaf("S", 14)
  t = leaf("T", 7)
  u = leaf("U", 3)
  v = leaf("V", 2)

  left = Node("Left", MIN, children=[
    Node("L1", MAX, children=[a, b]),
    Node("L2", MAX, children=[
      Node("L21", MIN, children=[c, d]),
      Node("L22", MIN, children=[e, f]),
    ]),
    Node("L3", MAX, children=[g, h]),
  ])

  middle = Node("Middle", MIN, children=[
    Node("M1", MAX, children=[i, j]),
    Node("M2", MAX, children=[k, l]),
    Node("M3", MAX, children=[
      Node("M31", MIN, children=[m, n]),
      Node("M32", MIN, children=[o, p]),
    ]),
  ])

  right = Node("Right", MIN, children=[
    Node("N1", MAX, children=[q, r]),
    Node("N2", MAX, children=[s, t]),
    Node("N3", MAX, children=[u, v]),
  ])

  return Node("Root", MAX, children=[left, middle, right])


def collect_leaf_names(node):
  if node.node_type == LEAF:
    return [node.name]

  names = []
  for child in node.children:
    names.extend(collect_leaf_names(child))
  return names


def record_pruned(children, start_index, pruned_nodes, pruned_leaves):
  for child in children[start_index:]:
    pruned_nodes.append(child.name)
    pruned_leaves.extend(collect_leaf_names(child))


def alpha_beta(node, alpha, beta, pruned_nodes, pruned_leaves):
  if node.node_type == LEAF:
    return node.value, [node.name]

  if node.node_type == MAX:
    best_value = -inf
    best_path = []

    for index, child in enumerate(node.children):
      child_value, child_path = alpha_beta(
        child,
        alpha,
        beta,
        pruned_nodes,
        pruned_leaves
      )

      if child_value > best_value:
        best_value = child_value
        best_path = [node.name] + child_path

      alpha = max(alpha, best_value)

      if alpha >= beta:
        record_pruned(
          node.children,
          index + 1,
          pruned_nodes,
          pruned_leaves
        )
        break

    return best_value, best_path

  if node.node_type == MIN:
    best_value = inf
    best_path = []

    for index, child in enumerate(node.children):
      child_value, child_path = alpha_beta(
        child,
        alpha,
        beta,
        pruned_nodes,
        pruned_leaves
      )

      if child_value < best_value:
        best_value = child_value
        best_path = [node.name] + child_path

      beta = min(beta, best_value)

      if alpha >= beta:
        record_pruned(
          node.children,
          index + 1,
          pruned_nodes,
          pruned_leaves
        )
        break

    return best_value, best_path

  raise ValueError("Unknown node type: " + node.node_type)


def solve():
  root = build_game_tree()
  pruned_nodes = []
  pruned_leaves = []

  value, path = alpha_beta(
    root,
    -inf,
    inf,
    pruned_nodes,
    pruned_leaves
  )

  return value, path, pruned_nodes, pruned_leaves


def main():
  value, path, pruned_nodes, pruned_leaves = solve()

  print("Alpha-Beta 剪枝结果")
  print("最终值:", value)
  print("最终路径:", " -> ".join(path))
  print("被剪枝的节点:", pruned_nodes)
  print("被剪枝的叶子节点:", pruned_leaves)


if __name__ == "__main__":
  main()
