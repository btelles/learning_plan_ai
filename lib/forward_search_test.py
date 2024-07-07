
from dataclasses import dataclass, field
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

@dataclass()
class SimpleForwardSearch(ForwardSearch):

  satisfies_goal_values: List[bool] = field(default_factory=lambda: [False])
  select_applicable_values: List[SimpleAction] = field(default_factory=lambda: [SimpleAction(1)])
  update_applicables_values: List[List[SimpleAction]] = field(default_factory=lambda: [[]])
  update_state_values: List[SimpleState] = field(default_factory=lambda: [])
  update_plan_values: List[List[SimpleAction]] = field(default_factory=lambda: [[]])

  def satisfies_goal(self, s1: SimpleState, s2: SimpleState) -> bool:
    return self.satisfies_goal_values.pop(0)

  def select_applicable(self, s: SimpleState, actions: List[SimpleAction]) -> SimpleAction:
    return self.select_applicable_values.pop(0)
  
  def update_applicables(self, previous_actions: List[SimpleAction], new_actions: List[SimpleAction]) -> List[SimpleAction]:
    return self.update_applicables_values.pop(0)
  
  def update_state(self, s: SimpleState, a: SimpleAction) -> SimpleState:
    return self.update_state_values.pop(0)
  
  def update_plan(self, actions: List[Action], new_action: Action) -> List[Action]:
    return self.update_plan_values.pop(0)

@dataclass()
class SimpleProblemSpec(ProblemSpec):

  expand_values: List[List[SimpleAction]] = field(default_factory=lambda: [[]])
  step_values: List[SimpleState] = field(default_factory=lambda: [])
  
  def expand(self, s: SimpleState) -> List[SimpleAction]:
    return self.expand_values.pop(0)
  
  def step(self, s: SimpleState, a: SimpleAction) -> SimpleState:
    return self.step_values.pop(0)

@pytest.fixture()
def simple_forward_search() -> SimpleForwardSearch:
  return SimpleForwardSearch()

@pytest.fixture()
def problem_spec() -> SimpleProblemSpec:
  return SimpleProblemSpec()

class TestSimpleForwardSearch:
  def test_searching_with_no_viable_plan_returns_false(self, simple_forward_search, problem_spec):
    initial_state = SimpleState(0)
    goal_state = SimpleState(0)

    problem_spec.expand_values = [[]]
    simple_forward_search.satisfies_goal_values = [False]

    assert simple_forward_search.search(problem_spec, initial_state, goal_state) == False

  def test_searching_with_same_initial_and_goal_state_returns_empty_plan(self, simple_forward_search, problem_spec):
    initial_state = SimpleState(0)
    goal_state = SimpleState(0)
    problem_spec.expand_values=[[SimpleAction(1)]]
    problem_spec.step_values=[]
    simple_forward_search.satisfies_goal_values = [True]
    assert simple_forward_search.search(problem_spec, initial_state, goal_state) == []

  def test_searching_for_a_plan_that_does_exist_returns_the_plan(self, simple_forward_search, problem_spec):
    initial_state = SimpleState(0)
    goal_state = SimpleState(0)

    simple_forward_search.update_plan_values = [[SimpleAction(1)]]
    simple_forward_search.update_applicables_values = [[SimpleAction(1)]]
    simple_forward_search.satisfies_goal_values = [False, True]

    problem_spec.step_values = [SimpleState(1), SimpleState(1)]

    assert simple_forward_search.search(problem_spec, initial_state, goal_state) == [SimpleAction(1)]
  
  def test_searching_for_a_plan_with_many_steps_returns_the_plan(self, simple_forward_search, problem_spec):
    initial_state = SimpleState(0)
    goal_state = SimpleState(0)

    simple_forward_search.update_plan_values = [[SimpleAction(1)], [SimpleAction(1), SimpleAction(2)]]
    simple_forward_search.update_applicables_values = [[SimpleAction(1)], [SimpleAction(1)]]
    simple_forward_search.select_applicable_values = [SimpleAction(1), SimpleAction(1)]
    simple_forward_search.satisfies_goal_values = [False, False, True]

    problem_spec.step_values = [SimpleState(1), SimpleState(1)]
    problem_spec.expand_values = [[SimpleAction(1)], [SimpleAction(2)]]

    
    assert simple_forward_search.search(problem_spec, initial_state, goal_state) == [SimpleAction(1), SimpleAction(2)]
  