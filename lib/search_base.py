from typing import List
from node import Node

class SearchBase:
  """Abstract base class for depth-first and breadth-first searches."""

  visited: List[Node] = []
  unvisited: List[Node] = []
  goal_node: Node
  comparisons: int = 0

  def search(self, root: Node, goal: Node) -> str | None:
    self.goal_node = goal
    self.unvisited: List[Node] = [root]
    self.visited: List[Node] = []

    result = self._search()
    return ' -> '.join([n.__repr__() for n in result]) if result else None

  def _search(self) -> List[Node] | None:
    pass
