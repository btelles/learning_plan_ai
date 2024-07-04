from typing import Callable, List

class State(object):
  """Represents a state in the search problem."""
  pass

class Action(object):
  """Represents an action that can be taken in the search problem."""
  pass

class ProblemSpec:
  """Represents the specification of the search problem.

  The `expand` function should return a list of all possible actions that can be taken from the current state, and the `step` function should take an action and update the state accordingly.
  """
  expand: Callable[[State], List[Action]]
  step: Callable[[State, Action], State]

class ForwardSearch:
  """Represents a forward search algorithm that uses a heuristic to guide the search towards the goal state."""


  satisfies_goal: Callable[[State, State], bool]  # Returns True if the current state is the goal state.
  select_applicables: Callable[[List[Action]], Action]  # Returns an action that can be taken from the current state to reach the goal state.
  update_applicables: Callable[[List[Action], List[Action]], List[Action]]  # Returns an updated list of actions that can be applied
  update_plan: Callable[[List[Action], Action], List[Action]]  # Returns an updated plan with the action that was selected.

  def search(self, o: ProblemSpec, si: State, goal_state: State):
    """Performs a forward search using the `expand` and `step` functions from the problem specification, until the goal state is reached.
    """
    state = si
    plan = List[Action]()
    applicables = List[Action]()

    while True:
      if (self.satisfies_goal(state, goal_state)):
        return plan
      applicables = self.update_applicables(applicables, o.expand(state))
      if (applicables.empty()):
        return False
      action = self.select_applicable(applicables)
      applicables.remove(action)
      state = o.step(state, action)
      plan = self.update_plan(plan, action)
