from dataclasses import dataclass
from aliases import NameComponent, ComponentTemplate
from prettier import Prettier
from style_sheet import StyleSheet


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]
    template: ComponentTemplate
    is_folder: bool
    prettier: Prettier
    stylesheet: StyleSheet
