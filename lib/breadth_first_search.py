from typing import List
from search_base import SearchBase
from node import Node

class BreadthFirstSearch(SearchBase):
  """Requires that the graph be fully connected."""

  def _search(self) -> List[Node] | None:
    while self.unvisited:
      if not self.unvisited:
        return None

      node = self.unvisited.pop(0)
      self.visited.append(node)
      self.comparisons += 1
      if node == self.goal_node:
        return self.visited

      for neighbor in node.neighbors:
        if neighbor not in self.visited and neighbor not in self.unvisited:
          self.unvisited.append(neighbor)
      return self._search()

