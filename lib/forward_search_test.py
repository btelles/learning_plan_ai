
from dataclasses import dataclass, field
from action import Action
from lib.state_action import StateAction
from problem_spec import ProblemSpec
from state import State
from forward_search import ForwardSearch
from typing import List, override
import pytest


@dataclass(eq=True, init=True, repr=True, order=True, frozen=True, unsafe_hash=True)
class SimpleState(State):
    value: int


@dataclass(eq=True, init=True, repr=True, order=True, frozen=True, unsafe_hash=True)
class SimpleAction(Action):
    value: int


@dataclass()
class SimpleForwardSearch(ForwardSearch):
    """A class that lets us explicitly test ForwardSearch base behavior without
    implementing the ForwardSearch interface.

    In particular, set the {method_name}_values to a list of values you want the
    method to return.

    This was easier than trying to track the values in a real problem, and lets
    us handle edge cases more directly.
    """

    satisfies_goal_values: List[bool] = field(default_factory=lambda: [False])
    select_applicable_values: List[StateAction] = field(
        default_factory=lambda: [StateAction(SimpleState(1), SimpleAction(1), 1)])
    update_applicables_values: List[List[StateAction]] = field(
        default_factory=lambda: [[]])
    update_state_values: List[SimpleState] = field(default_factory=lambda: [])
    update_plan_values: List[List[Action]] = field(
        default_factory=lambda: [[]])

    @override
    def satisfies_goal(self, s1: State, s2: State) -> bool:
        return self.satisfies_goal_values.pop(0)

    @override
    def select_applicable(self, state: State, state_actions: List[StateAction]) -> StateAction:
        return self.select_applicable_values.pop(0)

    @override
    def update_applicables(self, existing_actions: List[StateAction], new_actions: List[StateAction]) -> List[StateAction]:
        return self.update_applicables_values.pop(0)

    @override
    def update_plan(self, actions: List[Action], new_action: Action) -> List[Action]:
        return self.update_plan_values.pop(0)


@dataclass()
class SimpleProblemSpec(ProblemSpec):

    successors_values: List[List[StateAction]] = field(
        default_factory=lambda: [[]])
    step_values: List[State] = field(default_factory=lambda: [])

    @override
    def successors(self, state: State) -> List[StateAction]:
        return self.successors_values.pop(0)

    @override
    def step(self, state: State, action: Action) -> State:
        return self.step_values.pop(0)


@pytest.fixture()
def simple_forward_search() -> SimpleForwardSearch:
    return SimpleForwardSearch()


@pytest.fixture()
def problem_spec() -> SimpleProblemSpec:
    return SimpleProblemSpec()


class TestSimpleForwardSearch:
    def test_searching_with_no_viable_plan_returns_false(self, simple_forward_search: SimpleForwardSearch, problem_spec: SimpleProblemSpec):
        initial_state = SimpleState(value=0)
        goal_state = SimpleState(value=0)

        problem_spec.successors_values = [[]]
        simple_forward_search.satisfies_goal_values = [False]

        assert simple_forward_search.search(
            problem_spec, initial_state, goal_state) == False

    def test_searching_with_same_initial_and_goal_state_returns_empty_plan(self, simple_forward_search: SimpleForwardSearch, problem_spec: SimpleProblemSpec):
        initial_state = SimpleState(0)
        goal_state = SimpleState(0)
        problem_spec.successors_values = [
            [StateAction(SimpleState(1), SimpleAction(1), 1)]]
        problem_spec.step_values = []
        simple_forward_search.satisfies_goal_values = [True]
        assert simple_forward_search.search(
            problem_spec, initial_state, goal_state) == []

    def test_searching_for_a_plan_that_does_exist_returns_the_plan(self, simple_forward_search: SimpleForwardSearch, problem_spec: SimpleProblemSpec):
        initial_state = SimpleState(0)
        goal_state = SimpleState(0)

        simple_forward_search.update_plan_values = [[SimpleAction(1)]]
        simple_forward_search.update_applicables_values = [
            [StateAction(SimpleState(1), SimpleAction(1), 1)]]
        simple_forward_search.select_applicable_values = [
            StateAction(SimpleState(1), SimpleAction(1), 1)]
        simple_forward_search.satisfies_goal_values = [False, True]

        problem_spec.step_values = [SimpleState(1), SimpleState(1)]

        assert simple_forward_search.search(
            problem_spec, initial_state, goal_state) == [SimpleAction(1)]

    def test_searching_for_a_plan_with_many_steps_returns_the_plan(self, simple_forward_search: SimpleForwardSearch, problem_spec: SimpleProblemSpec):
        initial_state = SimpleState(0)
        goal_state = SimpleState(0)

        simple_forward_search.update_plan_values = [
            [SimpleAction(1)], [SimpleAction(1), SimpleAction(2)]]
        simple_forward_search.update_applicables_values = [
            [StateAction(SimpleState(1), SimpleAction(1), 1)],
            [StateAction(SimpleState(1), SimpleAction(1), 1)]
        ]
        simple_forward_search.select_applicable_values = [StateAction(SimpleState(1), SimpleAction(1), 1),
                                                          StateAction(SimpleState(1), SimpleAction(1), 1)]
        simple_forward_search.satisfies_goal_values = [False, False, True]

        problem_spec.step_values = [SimpleState(1), SimpleState(1)]
        problem_spec.successors_values = [[StateAction(SimpleState(1), SimpleAction(1), 1)], [
            StateAction(SimpleState(1), SimpleAction(2), 1)]]

        assert simple_forward_search.search(problem_spec, initial_state, goal_state) == [
            SimpleAction(1), SimpleAction(2)]
