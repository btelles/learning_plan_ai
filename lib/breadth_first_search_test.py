from breadth_first_search import BreadthFirstSearch
from node import Node

def test_starting_node_is_goal_node():
  a = Node('a')
  assert BreadthFirstSearch().search(a, a) == 'a'

def test_one_step_to_goal_node():
  a = Node('a')
  b = Node('b')
  a >> b
  print(a.neighbors)
  assert BreadthFirstSearch().search(a, b)== 'a -> b'

def test_two_step_to_goal_node():
  a = Node('a')
  b = Node('b')
  c = Node('c')
  a >> b
  b >> c
  print(a.neighbors)
  print(b.neighbors)
  assert BreadthFirstSearch().search(a, c)== 'a -> b -> c'

def test_visits_first_level_in_full_then_visits_second_branch_to_find_goal():
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
  breadth_first_search = BreadthFirstSearch()
  assert breadth_first_search.search(a, f) == 'a -> b -> c -> e -> d -> f'
  assert breadth_first_search.comparisons == 6
