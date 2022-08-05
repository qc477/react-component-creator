from dataclasses import dataclass
from style_sheet_templates import StyleSheetTemplates


@dataclass(slots=True, frozen=True)
class StyleSheet:
    is_module: bool
    templates: StyleSheetTemplates
