"""
__version__: alpha
"""
JSX_MODULE = (
    "import React from {quote}react{quote}{semi}\n"
    "import cl from {quote}./{name}.module.{extension}{quote}{semi}\n"
    "\n"
    "const {name} = () => {{\n"
    "{tab}return (){semi}\n"
    "}}{semi}\n"
    "\n"
    "export default {name}{semi}"
)
JSX_NO_MODULE = (
    "import React from {quote}react{quote}{semi}\n"
    "import {quote}./{name}.{extension}{quote}{semi}\n"
    "\n"
    "const {name} = () => {{\n"
    "{tab}return (){semi}\n"
    "}}{semi}\n"
    "\n"
    "export default {name}{semi}"
)
TSX_MODULE = (
    "import React from {quote}react{quote}{semi}\n"
    "import cl from {quote}./{name}.module.{extension}{quote}{semi}\n"
    "\n"
    "const {name}:React.FC = () => {{\n"
    "{tab}return (){semi}\n"
    "}}{semi}\n"
    "\n"
    "export default {name}{semi}"
)
