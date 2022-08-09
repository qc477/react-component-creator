from dataclasses import dataclass
from .aliases import NumberOfSpaces


@dataclass(slots=True, frozen=True)
class Prettier:
    tab_width: NumberOfSpaces
    is_semi: bool
    is_single_quote: bool
