from dataclasses import dataclass

@dataclass(eq=True, init=True, repr=True, order=True, frozen=True, unsafe_hash=True)
class Action(object):
  """Represents an action that can be taken in the search problem."""
  pass