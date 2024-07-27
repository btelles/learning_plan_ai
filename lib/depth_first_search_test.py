from depth_first_search import DepthFirstSearch, Node

def test_starting_node_is_goal_node():
  a = Node('a')
  assert DepthFirstSearch().search(a, a) == 'a'

def test_one_step_to_goal_node():
  a = Node('a')
  b = Node('b')
  a >> b
  print(a.neighbors)
  assert DepthFirstSearch().search(a, b)== 'a -> b'

def test_two_step_to_goal_node():
  a = Node('a')
  b = Node('b')
  c = Node('c')
  a >> b
  b >> c
  print(a.neighbors)
  print(b.neighbors)
  assert DepthFirstSearch().search(a, c)== 'a -> b -> c'

def test_visits_first_branch_at_full_depth_then_visits_second_branch_to_find_goal():
  a  = Node('a')
  b  = Node('b')
  c  = Node('c')
  d  = Node('d')
  e  = Node('e')
  f   = Node('f')
  a >> b
  b  >> c
  c  >> d
  b  >> e
  e  >> f
  depth_first_search = DepthFirstSearch()
  assert depth_first_search.search(a, f) == 'a -> b -> e -> f'
  assert depth_first_search.comparisons == 4

def test_visits_first_branch_at_full_depth_then_visits_first_branch_to_find_goal():
  a  = Node('a')
  b  = Node('b')
  c  = Node('c')
  d  = Node('d')
  e  = Node('e')
  f   = Node('f')
  a >> b
  b  >> e
  c  >> d
  b  >> c
  e  >> f
  depth_first_search = DepthFirstSearch()
  assert depth_first_search.search(a, f) == 'a -> b -> c -> d -> e -> f'
  assert depth_first_search.comparisons == 6
