"""
task4.py - Uses a function to calculate the final price of a product after applying a discount.
Shows Python's Duck Typing by allowing any numeric type as input.
"""

def calculate_discount(price, discount):
    """
    Calculates the final price after applying a discount percentage.

    Parameters:
    - price (int or float): The original price of the product.
    - discount (int or float): The discount percentage (between 0 and 100).

    Returns:
    - float: The final price rounded to two decimal places.

    Raises:
    - ValueError: If price or discount are not numeric.
    - ValueError: If discount is negative or greater than 100.
    """
    
    # Ensure both inputs are numeric (Duck Typing demonstration)
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise ValueError("Price and discount must be numeric values.")

    # Ensure discount is within a valid range
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100 percent.")

    # Calculate final price after applying discount
    final_price = price - (price * (discount / 100))
    return round(final_price, 2)  # Round to 2 decimal places for currency formatting
