from typing import List
from node import Node
from search_base import SearchBase

class DepthFirstSearch(SearchBase):
  """Requires that the graph be fully connected."""

  def _search(self) -> List[Node] | None:
    if not self.unvisited:
      return None
    while self.unvisited:

      node = self.unvisited.pop()
      self.visited.append(node)
      self.comparisons += 1
      if node == self.goal_node:
        return self.visited

      for neighbor in node.neighbors:
        if neighbor not in self.visited and neighbor not in self.unvisited:
          self.unvisited.append(neighbor)
      return self._search()

