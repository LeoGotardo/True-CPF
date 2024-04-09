# True CPF Application

## Introduction

The True CPF application is a Python-based graphical user interface that allows users to validate and generate Brazilian CPF numbers (Cadastro de Pessoas Físicas). The application uses `customtkinter` for the GUI, and includes features for real-time CPF generation and validation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Installation

To run the True CPF application, you need Python installed on your machine along with several dependencies.

### Prerequisites

- Python 3.6 or higher
- `pip` for package management

### Steps

1. Clone the repository or download the source code:
   ```bash
   git clone https://example.com/true-cpf-repo.git
   cd true-cpf-repo
   ```

2. Install required Python packages:
   ```bash
   pip install customtkinter pyperclip
   ```

## Usage

To start the application, run the `main.py` script:

```bash
python main.py
```

This will open a window where you can either validate a given CPF or generate a new CPF number.

## Features

- **CPF Validation**: Check if a CPF number is valid according to Brazilian rules.
- **CPF Generation**: Generate a random valid CPF number.
- **Copy to Clipboard**: Automatically copies generated CPF numbers to the clipboard.
- **User-Friendly GUI**: Easy to navigate graphical user interface.

## Dependencies

- `customtkinter`: Customized modern GUI components.
- `pyperclip`: Allows clipboard operations for copying CPF numbers.
- `random`: For generating random numbers as part of CPF.
- `re`: Regular expression operations for formatting CPF numbers.
- `os`: Used to clear the console.

## Configuration

No additional configuration is required to run the application as provided.

## Examples

### Validating a CPF

Enter the CPF number in the input field and click on "Validar CPF" to check its validity. A message box will inform you whether the CPF is valid or not.

### Generating a CPF

Click on "Criar CPF" to generate a new CPF number. The generated CPF will be shown in a message box and copied to your clipboard.

## Troubleshooting

- **Common Installation Issues**: Ensure all dependencies are properly installed using pip.
- **Running the Application**: If the application fails to start, check your Python version and ensure it's compatible.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
