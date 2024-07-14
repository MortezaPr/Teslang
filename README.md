# Teslang

TesLang is a custom programming language designed for educational purposes. This project includes the front-end compiler for TesLang, developed using Python and PLY (Python Lex-Yacc).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

TesLang is a custom language designed to help users understand the basics of compiler construction. It includes a lexer, parser, semantic analyzer, and intermediate representation (IR) generator. This project demonstrates the front-end compilation process, turning source code into an intermediate representation.

## Features

- **Lexer**: Tokenizes the input source code.
- **Parser**: Generates an abstract syntax tree (AST) from the tokenized input.
- **Semantic Analyzer**: Performs type checking and scope management.
- **Intermediate Representation (IR) Generator**: Converts the AST into an intermediate representation for further processing.

## Installation

1. Clone the repository:

    ```bash
    https://github.com/MortezaPr/Teslang.git
    cd Teslang
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To compile a TesLang source file, use the `main.py` script. Ensure you have a TesLang source file named `teslang_source.txt` in the same directory as `main.py`.

```bash
python main.py
```
## Modules

### Lexer (`lexer.py`)

Tokenizes the input source code using PLY (Python Lex-Yacc).

### Tokens (`tokens.py`)

Defines the tokens and reserved words used in the language.

### Parser (`parser.py`)

Parses the tokenized input to generate an abstract syntax tree (AST).

### Semantic Analyzer (`semantic_analyzer.py`)

Performs type checking and manages the symbol table.

### Abstract Syntax Tree (AST) (`ast.py`)

Defines the AST node classes used by the parser and semantic analyzer.

### Intermediate Representation (IR) (`ir.py`)

Defines the IR node classes used by the IR generator.

### IR Generator (`ir_generator.py`)

Generates the intermediate representation from the AST.

### Symbol Table (`symbol_table.py`)

Manages the symbols and their attributes during semantic analysis.

### Main Script (`main.py`)

The entry point for the compiler, which ties together the lexer, parser, semantic analyzer, and IR generator.

## Example

Create a TesLang source file named `teslang_source.txt` with the following content:

```plaintext
fn add(a as int, b as int) <int>
{
    result :: int = a + b;
    return result;
}
```

Run the compiler using the following command:

```bash
python main.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


## License

Distributed under the MIT License.  See the [LICENSE](LICENSE) file for more information.