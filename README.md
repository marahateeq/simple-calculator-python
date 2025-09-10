# simple-calculator-python
=======
# Simple Calculator

This is a simple calculator project implemented in Python. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure

```
simple-calculator
├── src
│   ├── calculator.py
│   └── utils.py
├── tests
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts one number from another.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides one number by another with error handling for division by zero.

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

1. Import the `Calculator` class from the `calculator` module.
2. Create an instance of the `Calculator`.
3. Use the methods `add`, `subtract`, `multiply`, and `divide` to perform calculations.

### Example

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
```

## Running Tests

To run the unit tests for the calculator, use the following command:

```
pytest tests/test_calculator.py
```

## License

This project is licensed under the MIT License.