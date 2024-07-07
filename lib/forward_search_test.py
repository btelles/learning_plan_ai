
from dataclasses import dataclass
from action import Action
from problem_spec import ProblemSpec
from state import State
from forward_search import ForwardSearch
from typing import List
import pytest
import abc

@dataclass(eq=True, repr=True)
class SimpleState(State):
  value: int

  def __hash__(self):
    return f"SimpleState#{self.value()}"

@dataclass(eq=True, repr=True)
class SimpleAction(Action):
  value: int

  def __hash__(self):
    return f"SimpleAction#{self.value()}"


class SimpleForwardSearch(ForwardSearch):
  def satisfies_goal(self, s1: SimpleState, s2: SimpleState) -> bool:
    return s1 == s2
  
  def select_applicable(self, s: SimpleState, actions: List[SimpleAction]) -> SimpleAction:
    return actions.pop(0)

  def update_applicables(self, previous_actions: List[SimpleAction], new_actions: List[SimpleAction]):
    return new_actions

  def update_state(self, s: SimpleState, a: SimpleAction) -> SimpleState:
    return State(s.value + a.value)
  
  def update_plan(self, actions: List[Action], new_action: Action) -> List[Action]:
    return actions + [new_action]

class SimpleProblemSpec(ProblemSpec):
  def expand(self, s: SimpleState) -> List[SimpleAction]:
    if (s.value == 0):
      return []
    
    return [SimpleAction(1), SimpleAction(2)]
  
  def step(self, s: SimpleState, a: SimpleAction) -> SimpleState:
    return SimpleState(s.value + a.value)

@pytest.fixture()
def simple_forward_search():
  return SimpleForwardSearch()


class TestSimpleForwardSearch:
  def test_searching_with_no_viable_plan_returns_false(self, simple_forward_search):
    initial_state = SimpleState(0)
    goal_state = SimpleState(2)

    assert simple_forward_search.search(SimpleProblemSpec(), initial_state, goal_state) == False

  def test_searching_with_same_initial_and_goal_state_returns_empty_plan(self, simple_forward_search):
    initial_state = SimpleState(1)
    goal_state = SimpleState(1)

    assert simple_forward_search.search(SimpleProblemSpec(), initial_state, goal_state) == []

  def test_searching_for_a_plan_that_does_exist_returns_the_plan(self, simple_forward_search):
    initial_state = SimpleState(1)
    goal_state = SimpleState(2)

    assert simple_forward_search.search(SimpleProblemSpec(), initial_state, goal_state) == [SimpleAction(1)]
  
  def test_searching_for_a_plan_with_many_steps_returns_the_plan(self, simple_forward_search):
    initial_state = SimpleState(1)
    goal_state = SimpleState(3)
    
    assert simple_forward_search.search(SimpleProblemSpec(), initial_state, goal_state) == [SimpleAction(1), SimpleAction(1)]
  