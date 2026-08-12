from langchain_core.tools import tool

@tool
def calculate_percentage(value: float, percentage: float) -> float:
    """Calculate a percentage of a given value."""
    return value * (percentage / 100)

