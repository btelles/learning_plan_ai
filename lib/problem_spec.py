
from typing import Callable, List

from action import Action
from state import State


class ProblemSpec:
  """Represents the specification of the search problem.
  """
  expand: Callable[[State], List[Action]]  # Returns a list of all possible actions that can be taken from the current state.
  step: Callable[[State, Action], State]  # Takes an action and updates the state accordingly.
