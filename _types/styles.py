from dataclasses import dataclass
from typing import NamedTuple


class StyleExtensions(NamedTuple):
    css: bool
    scss: bool
    sass: bool
    less: bool


@dataclass(slots=True, frozen=True)
class Styles:
    is_module: bool
    file_extensions: StyleExtensions
