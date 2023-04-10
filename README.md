# Terminal Colors

This Python class provides a set of methods for formatting text with ANSI escape codes for terminal colors. The class includes the following colors:

1. HEADER
1. OKBLUE
1. OKCYAN
1. OKGREEN
1. WARNING
1. FAIL
1. BOLD
1. UNDERLINE

You can use these colors to format text using the provided methods, or by calling the color method and passing in the desired ANSI escape code.

The test method provides an example of how to use the class and its methods. It prints out the class's logo in each of the available colors.
Usage

To use the TerminalColors class in your own code, you can simply import it and create an instance of the class:

```py

from terminal_colors import TerminalColors

tc = TerminalColors()
```

You can then use the class's methods to format your text:

```py

print(tc.okblue("This text will be formatted in OK blue."))
```
Alternatively, you can use the color method to format your text with any of the available ANSI escape codes:

```py
print(tc.color("This text will be formatted in OK blue.", "\033[94m"))
```

Example

```py

import os
from terminal_colors import TerminalColors

if __name__ == "__main__":
    os.system('color')
    tc = TerminalColors()

    # Print the class logo in each available color
    print(tc.header(tc.__repr__()))
    print(tc.okblue(tc.__repr__()))
    print(tc.okcyan(tc.__repr__()))
    print(tc.okgreen(tc.__repr__()))
    print(tc.warning(tc.__repr__()))
    print(tc.fail(tc.__repr__()))
    print(tc.bold(tc.__repr__()))
    print(tc.underline(tc.__repr__()))
```
The above code will print the class logo in each of the available colors.
