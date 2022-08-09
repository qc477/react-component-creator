from dataclasses import dataclass
from .aliases import NameComponent, FileTemplate
from .prettier import Prettier
from .style_sheet import StyleSheet


@dataclass(slots=True, frozen=True)
class CMDArguments:
    names: list[NameComponent]
    template: FileTemplate
    is_folder: bool
    prettier: Prettier
    stylesheet: StyleSheet
