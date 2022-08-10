from dataclasses import dataclass
from typing import NamedTuple


class Extensions(NamedTuple):
    scss: bool
    sass: bool
    less: bool


@dataclass(slots=True, frozen=True)
class StyleSheet:
    is_module: bool
    extensions: Extensions
