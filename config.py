class ProgrammConfig:
    NAME = "ReactComponentCreator"
    DESCRIPTION = "Console utility for creating React components."


class SettingsConfig:
    SEMI = ";"
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'


class ComponentConfig:
    TYPESCRIPTREACT_EXTENSION = "tsx"
    JAVASCRIPTREACT_EXTENSION = "jsx"

class StyleFileConfig:
    SUFFIX = ".module"
    DEFAULT_EXTENSION = "css"


class ContentConfig:
    TEMPLATE_FILE_INDEX = (
        "import {name} from {quote}./{name}{quote}{semi}\n"
        "export default {name}{semi}"
    )
    COMPONENT_TEMPLATE = (
        "import React from {quote}react{quote}{semi}\n"
        "{style_import_row}"
        "\n"
        "const {name}{declaring_functional_component} = () => {{\n"
        "{tab}return (){semi}\n"
        "}}{semi}\n"
        "\n"
        "export default {name}{semi}"
    )
    STYLE_IMPORT_ROW = "import {quote}./{name_styles_file}{quote}{semi}\n"
    DECLARING_FUNCTIONAL_COMPONENT = ": React.FC"
