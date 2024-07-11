from dataclasses import dataclass

@dataclass(eq=True, init=True, repr=True, order=True, frozen=True, unsafe_hash=True)
class State(object):
  """Represents a state in the search problem."""
  pass  
