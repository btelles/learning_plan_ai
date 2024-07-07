from typing import List
import abc
from action import Action
from problem_spec import ProblemSpec
from state import State

class ForwardSearch:
  """Represents a forward search algorithm that uses a heuristic to guide the search towards the goal state."""


  @abc.abstractmethod
  def satisfies_goal(self, s1: State, s2: State) -> bool:
    """Returns True if the current state is the goal state."""
    pass

  @abc.abstractmethod
  def select_applicable(self, state: State, actions: List[Action]) -> Action:
    """ Returns an action that can be taken from the given state to reach the goal state."""
    pass

  @abc.abstractmethod
  def update_applicables(self, existing_actions: List[Action], new_actions: List[Action]) -> List[Action]:
    """ Returns an updated list of actions that can be applied"""
    pass

  @abc.abstractmethod
  def update_plan(actions: List[Action], new_action: Action) -> List[Action]:
    """ Returns an updated plan with the action that was selected."""
    pass

  def search(self, o: ProblemSpec, si: State, goal_state: State):
    """Performs a forward search using the `expand` and `step` functions from the problem specification, until the goal state is reached.
    """
    state = si
    plan = list[Action]()
    applicables = list[Action]()

    while True:
      if (self.satisfies_goal(state, goal_state)):
        return plan
      applicables = self.update_applicables(applicables, o.expand(state))
      if (not applicables):
        return False
      action = self.select_applicable(state, applicables)
      state = o.step(state, action)
      plan = self.update_plan(plan, action)
