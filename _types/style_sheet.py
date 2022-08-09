from dataclasses import dataclass
from .aliases import FileTemplate


@dataclass(slots=True, frozen=True)
class StyleSheet:
    is_module: bool
    template: FileTemplate
