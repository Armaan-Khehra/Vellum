# Syntho

## Basic Language Interpreter

### Overview
This project is a simple interpreter for a custom programming language called "Basic". The interpreter is implemented in Python and includes a lexer that tokenizes input strings, error handling, and the capability to parse basic mathematical expressions.

### Features
- **Tokenization**: Converts input strings into a sequence of tokens.
- **Error Handling**: Detects and reports errors in the input, including illegal characters and provides line/column information.
- **Mathematical Operations**: Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
- **Parentheses**: Allows grouping of expressions using parentheses.
- **Interactive Shell**: Provides a command-line interface for user interaction.

### Installation
To run this project, you need Python installed on your machine. Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <repository-directory>

Usage
To start the interactive shell, run the following command in your terminal:

bash
Copy code
python shell.py
You will be prompted with basic >. You can enter mathematical expressions or commands. Here are some examples of valid inputs:

2 + 3
4 * (5 - 2)
7 / 2 + 3.5
Press Enter to see the results. If an error occurs, it will display a message indicating the nature of the error along with the line and column of the issue.

Structure
basic.py: Contains the lexer, token definitions, and error handling.
shell.py: The interactive shell for user input and output.
Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Any contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
Thanks to the online communities and resources that helped in understanding the concepts of language interpretation and error handling.
Contact
For any questions or feedback, please reach out to your-email@example.com.
