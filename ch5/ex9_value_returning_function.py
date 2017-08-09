#!/usr/bin/python3

def get_sale_price(current_price):
    # As soon as the return statement is encountered, the function completes
    # and provides the expression's value to the caller. No subsequent
    # statements are executed.
    if current_price < 10:
        return current_price * 0.90  # 10% discount
    elif current_price >= 10 and current_price < 20:
        return current_price * 0.80  # 20% discount
    else:
        return current_price - 10
        
def main():
    output = '{} was ${:.2f}, now ${:.2f}'
    price = 7
    sale_price = get_sale_price(price)
    print(output.format('T-shirt', price, sale_price))
    
    price = 17
    sale_price = get_sale_price(price)
    print(output.format('Hat', price, sale_price))
    
    price = 35
    sale_price = get_sale_price(price)
    print(output.format('Jersey', price, sale_price))
    
main()
