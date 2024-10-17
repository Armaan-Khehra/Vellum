# Vellum

**Vellum** is a simple interpreted language designed to evaluate mathematical expressions. It supports fundamental arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation.

## Features

- **Basic Arithmetic Operations**: Vellum can handle addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`^`).
- **Number Types**: Supports both integers and floating-point numbers.
- **Parentheses Support**: You can use parentheses to group expressions and control the order of operations.
- **Error Handling**: The language provides clear error messages for issues like invalid syntax, illegal characters, and division by zero.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/armaan-khehra/Vellum.git
2. Navigate to the project directory:
    ```bash
   cd Vellum
    ```
3. Make sure you have Python installed (Python 3.x is recommended).

## How to Use

To run a Vellum program, use the run() function. This function takes two arguments: a filename (for reference in error messages) and a string containing the expression to evaluate.

## Example
```python
from Vellum import run

result, error = run('<stdin>', '3 + 4 * (2 - 1)')

if error:
    print(error.as_string())
else:
    print(result)
```
This will output:
```
7
```

## Error Handling

- Invalid Syntax: When the user enters an incorrect expression, Vellum will detect the syntax error and provide an informative message indicating the location of the problem.
- Illegal Characters: If unsupported characters are encountered, Vellum will raise an Illegal Character error, providing details about the location and character in question.
- Runtime Errors: Issues such as division by zero will be caught and reported as runtime errors.

## File Structure

- Vellum.py: The main interpreter that includes the lexer, parser, interpreter, and error handling.
- strings_with_arrows.py: Utility file to enhance error message readability by pointing to the position of the error in the input.
