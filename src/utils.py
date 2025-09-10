def validate_number(value):
    """Validate if the input is a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def handle_division_by_zero(divisor):
    """Handle division by zero error."""
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return divisor