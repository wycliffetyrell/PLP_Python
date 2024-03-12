# calculate discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent = price - (price * discount_percent / 100)
        return discount_percent
    else:
        return price

def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price != original_price:
        print("Final price after applying the discount: Ksh", final_price)
    else:
        print("No discount applied. Original price: Ksh", original_price)

if __name__ == "__main__":
    main()
