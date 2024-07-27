import dataclasses
from dataclasses import field
from typing import List, Self

@dataclasses.dataclass()
class Node:
  value: str
  neighbors: List[Self] = field(default_factory=list)

  def __repr__(self):
    return self.value

  def __rshift__(self, other: Self):
    self.neighbors.append(other)
    other.neighbors.append(self)

  def __eq__(self, other: Self) -> bool:
    return self.value == other.value
