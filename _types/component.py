from dataclasses import dataclass

from .aliases import NameComponent


@dataclass(slots=True, frozen=True)
class Component:
    names: list[NameComponent]
    is_folder: bool
    is_tsx: bool
