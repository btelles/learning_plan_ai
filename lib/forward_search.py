from typing import List
import logging
from action import Action
from lib.state_action import StateAction
from problem_spec import ProblemSpec
from state import State

logger = logging.getLogger(__name__)


class ForwardSearch:
    """Represents a forward search algorithm that uses a heuristic to guide the search towards the goal state."""

    def satisfies_goal(self, s1: State, s2: State) -> bool:
        """Returns True if the current state is the goal state."""
        raise NotImplementedError("The satisfies_goal method must be implemented.")

    def select_applicable(self, state: State, state_actions: List[StateAction]) -> StateAction:
        """ Returns an action that can be taken from the given state to reach the goal state."""
        raise NotImplementedError("The select_applicable method must be implemented.")

    def update_applicables(self, existing_actions: List[StateAction], new_actions: List[StateAction]) -> List[StateAction]:
        """ Returns an updated list of actions that can be applied"""
        raise NotImplementedError("The update_applicables method must be implemented.")

    def update_plan(self, actions: List[Action], new_action: Action) -> List[Action]:
        """ Returns an updated plan with the action that was selected."""
        raise NotImplementedError("The update_plan method must be implemented.")

    def search(self, problem_spec: ProblemSpec, si: State, goal_state: State):
        """Performs a forward search using the `expand` and `step` functions from the problem specification, until the goal state is reached.
        """
        state = si
        plan = list[Action]()
        applicables = list[StateAction]()

        logger.debug(f"Starting search from state {state}")

        while True:
            if (self.satisfies_goal(state, goal_state)):
                logger.debug(f"Goal state reached with states:\n\n  {
                             state}\n\nand\n\n  {goal_state}")
                return plan

            logger.debug(f"Expanding state:\n  {state}")
            applicables: List[StateAction] = self.update_applicables(
                applicables, problem_spec.successors(state))
            logger.debug(f"New applicable actions are:\n  {applicables}")

            if (not applicables):
                return False
            state_action = self.select_applicable(state, applicables)
            logger.debug(f"Selected action:\n  {state_action}")

            state = problem_spec.step(state, state_action.action)
            logger.debug(f"visited state/action: {state_action}")
            applicables = [a for a in applicables if a != state_action]

            logger.debug(f"New state after applying the action is:\n  {state}")

            plan = self.update_plan(plan, state_action.action)
            logger.debug(f"New plan is:\n  {plan}")
