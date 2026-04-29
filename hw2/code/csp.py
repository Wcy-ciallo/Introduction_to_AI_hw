COLORS = ["red", "green", "blue", "yellow", "purple"]


REGIONS = [
  "北京", "天津", "河北", "山西", "内蒙古",
  "辽宁", "吉林", "黑龙江",
  "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东",
  "河南", "湖北", "湖南", "广东", "广西", "海南",
  "重庆", "四川", "贵州", "云南", "西藏",
  "陕西", "甘肃", "青海", "宁夏", "新疆",
  "香港", "澳门", "台湾",
]


# 只记录陆地相邻关系；海南、台湾没有省级陆地相邻行政区。
ADJACENT_PAIRS = [
  ("北京", "天津"),
  ("北京", "河北"),
  ("天津", "河北"),

  ("河北", "辽宁"),
  ("河北", "内蒙古"),
  ("河北", "山西"),
  ("河北", "河南"),
  ("河北", "山东"),

  ("山西", "内蒙古"),
  ("山西", "陕西"),
  ("山西", "河南"),

  ("内蒙古", "黑龙江"),
  ("内蒙古", "吉林"),
  ("内蒙古", "辽宁"),
  ("内蒙古", "陕西"),
  ("内蒙古", "宁夏"),
  ("内蒙古", "甘肃"),

  ("辽宁", "吉林"),
  ("吉林", "黑龙江"),

  ("上海", "江苏"),
  ("上海", "浙江"),

  ("江苏", "山东"),
  ("江苏", "安徽"),
  ("江苏", "浙江"),

  ("浙江", "安徽"),
  ("浙江", "江西"),
  ("浙江", "福建"),

  ("安徽", "山东"),
  ("安徽", "河南"),
  ("安徽", "湖北"),
  ("安徽", "江西"),

  ("福建", "江西"),
  ("福建", "广东"),

  ("江西", "湖北"),
  ("江西", "湖南"),
  ("江西", "广东"),

  ("山东", "河南"),

  ("河南", "陕西"),
  ("河南", "湖北"),

  ("湖北", "陕西"),
  ("湖北", "重庆"),
  ("湖北", "湖南"),

  ("湖南", "重庆"),
  ("湖南", "贵州"),
  ("湖南", "广西"),
  ("湖南", "广东"),

  ("广东", "广西"),
  ("广东", "香港"),
  ("广东", "澳门"),

  ("广西", "贵州"),
  ("广西", "云南"),

  ("重庆", "四川"),
  ("重庆", "贵州"),
  ("重庆", "陕西"),

  ("四川", "贵州"),
  ("四川", "云南"),
  ("四川", "西藏"),
  ("四川", "青海"),
  ("四川", "甘肃"),
  ("四川", "陕西"),

  ("贵州", "云南"),

  ("云南", "西藏"),

  ("西藏", "新疆"),
  ("西藏", "青海"),

  ("陕西", "甘肃"),
  ("陕西", "宁夏"),

  ("甘肃", "宁夏"),
  ("甘肃", "青海"),
  ("甘肃", "新疆"),

  ("青海", "新疆"),
]


def build_neighbors():
  neighbors = {}

  for region in REGIONS:
    neighbors[region] = []

  for region_a, region_b in ADJACENT_PAIRS:
    neighbors[region_a].append(region_b)
    neighbors[region_b].append(region_a)

  return neighbors




NEIGHBORS = build_neighbors()

def build_domains():
  domains = {}
  for region in REGIONS:
    domains[region] = COLORS.copy()
  
  return domains

def is_consistent(region, color, assignment):
  for neighbor in NEIGHBORS[region]:
    if neighbor in assignment and assignment[neighbor] == color:
      return False

  return True

def select_unassigned_region(assignment, domains):
  unassigned = []
  for region in REGIONS:
    if region not in assignment:
      unassigned.append(region)
  
  best_region = unassigned[0]
  for region in unassigned:
    if len(domains[region]) < len(domains[best_region]):
      best_region = region
  return best_region

def revise(domains, region_a, region_b):
  revised = False
  if len(domains[region_b]) == 1:
    forbidden_color = domains[region_b][0]

    if forbidden_color in domains[region_a]:
      domains[region_a].remove(forbidden_color)
      revised = True
  
def ac3(domains):
  queue = []
  for region_a, region_b in ADJACENT_PAIRS:
    queue.append((region_a, region_b))
    queue.append((region_b, region_a))
  
  while queue:
    region_a, region_b = queue.pop(0)
  
  if revise(domains, region_a, region_b):
    if len(domains[region_a]) == 0:
      return False
    
    for neighbor in NEIGHBORS[region_a]:
      if neighbor != region_b:
        queue.append((neighbor, region_a))
  
  
  return True

def copy_domains(domains):
  new_domains = {}
  for region in domains:
    new_domains[region] = domains[region].copy()
  
  return new_domains

def forward_check(domains, region, color):
  domains[region] = [color]

  for neighbor in NEIGHBORS[region]:
    if color in domains[neighbor]:
      domains[neighbor].remove(color)

      if len(domains[neighbor]) == 0:
        return False

  return ac3(domains)

def backtrack(assignment, domains):
  if len(assignment) == len(REGIONS):
    return assignment

  region = select_unassigned_region(assignment, domains)
  for color in domains[region]:
    if is_consistent(region, color, assignment):
      new_assignment = assignment.copy()
      new_domains = copy_domains(domains)

      new_assignment[region] = color

      if forward_check(new_domains, region, color):
        result = backtrack(new_assignment, new_domains)

        if result is not None:
          return result
  
  return None

def solve_map_coloring():
  domains = build_domains()
  if not ac3(domains):
    return None
  
  return backtrack({}, domains)

def validate_solution(solution):
  if solution is None:
    return False
  
  for region in REGIONS:
    if region not in solution:
      return False
    
    if solution[region] not in COLORS:
      return False
    
  for region_a, region_b in ADJACENT_PAIRS:
    if solution[region_a] == solution[region_b]:
      return False
  
  return True


def main():
  solution = solve_map_coloring()

  if solution is None:
    print("没有找到合法染色方案")
    return
  
  print("结果：")

  for region in REGIONS:
    print(region + ":", solution[region])
  
  print("检查结果: ", validate_solution(solution))


if __name__ == "__main__":
  main()
