
from abc import abstractmethod
from typing import List

from action import Action
from state import State


class ProblemSpec:
  """Represents the specification of the search problem.
  """
  @abstractmethod
  def expand(self, state: State) -> List[Action]:
    """Returns a list of all possible actions that can be taken from the current state."""
    pass

  @abstractmethod
  def step(self, state: State, action: Action) -> State:
    """ Takes an action and updates the state accordingly."""
    pass
