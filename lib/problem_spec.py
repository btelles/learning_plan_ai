
from abc import abstractmethod
from typing import List

from action import Action
from state import State
from state_action import StateAction


class ProblemSpec:
  """Represents the specification of the search problem.
  """
  @abstractmethod
  def expand(self, state: State) -> List[StateAction]:
    """Returns a list of all possible actions that can be taken from the given state."""
    pass

  @abstractmethod
  def step(self, state: State, action: Action) -> State:
    """ Takes a state and applies the given action, returning the resulting state. """
    pass
