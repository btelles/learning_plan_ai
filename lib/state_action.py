from lib.action import Action
from lib.state import State
from dataclasses import dataclass

@dataclass(eq=True, repr=True, frozen=True)
class StateAction:
  state: State
  action: Action
