def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount percentage is 20% or higher, apply the discount;
    otherwise, return the original price.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.

    Returns:
    float: The final price after applying the discount.
    """
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    else:
        return price


# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percent)
    
    # Output the result
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
