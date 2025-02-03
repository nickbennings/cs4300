def calculate_discount(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise ValueError("Price and discount must be numeric values.")

    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100 percent.")

    final_price = price - (price * (discount / 100))
    return round(final_price, 2)
