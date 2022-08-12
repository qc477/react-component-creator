from dataclasses import dataclass
from .component import Component
from .prettier import Prettier
from .styles import Styles


@dataclass(slots=True, frozen=True)
class Arguments:
    component: Component
    prettier: Prettier
    styles: Styles
