from dataclasses import dataclass
from typing import NamedTuple

from .aliases import NameComponent


class ReactExtensions(NamedTuple):
    is_js: bool
    is_ts: bool
    is_jsx: bool
    is_tsx: bool


@dataclass(slots=True, frozen=True)
class Component:
    names: list[NameComponent]
    is_folder: bool
    file_extensions: ReactExtensions
