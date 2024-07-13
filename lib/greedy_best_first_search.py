from typing import List, override
from forward_search import ForwardSearch
from lib.action import Action
from lib.state import State
from lib.state_action import StateAction
from abc import abstractmethod
from itertools import chain

class GreedyBestFirstSearch(ForwardSearch):
  """Greedy Best First Search is a depth-first forward search that tries to
  find a solution from an initial state to a goal state using a static
  heuristic function."""
  
  @abstractmethod
  def heuristic_fn(self, state: State) -> int:
    """A function that takes a state and returns an estimated cost of
    reaching a goal from that state."""
    pass

  def satisfies_goal(self, s1: State, s2: State) -> bool:
    return s1 == s2
  
  @override
  def select_applicable(self, state: State, state_actions: List[StateAction]) -> StateAction:
    """ Returns the action whose resulting state has the lowest heuristic.
    In this implementation, this will always be the first applicable action
    since actions are stored in ascending order of lowest resulting state cost.
    """
    return state_actions.pop(0)
  
  @override
  def update_applicables(self, existing_actions: List[StateAction], new_actions: List[StateAction]) -> List[StateAction]:
    return sorted(
      list(
        chain(
          set(existing_actions + new_actions)
          )
        ),
      key=lambda sa: sa.cost
    )
  
  @override
  def update_plan(self, actions: List[Action], new_action: Action) -> List[Action]:
    return actions + [new_action]
