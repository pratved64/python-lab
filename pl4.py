from datetime import datetime
import os


# Helper Functions
def sum_key(itr, key=0):
    itersum = 0
    for i in itr:
        itersum += i[key]
    return itersum


def max_spaces(itr, key=0):
    maxlen = 0
    for i in itr:
        if len(i[key]) > maxlen:
            maxlen = len(i[key])
    return maxlen


# Main Functions
def bill(net, grand, disc, items, order):
    os.system('cls')
    print("\n- - - - BURGER KING - - - -\n")

    # Customer Details
    print(f"Date: {order['time']}")
    print(f"Address: {order['address']}\n")

    # Items
    print(f"Particulars: ({order['n_items']})")
    mlen = max_spaces(items)
    for item in items:
        print(f"{item[0].ljust(mlen)} : {str(item[1]).rjust(mlen)}")
    print(f"{'TOTAL'.ljust(mlen)} : {str(net).rjust(mlen)}")

    # Payment Details
    print("\n- - - - - - - - - - - - - - - \n")
    print(f"Promocode: {order['promocode']}")
    print(f"Payment Mode: {order['mode'].upper()} ({'Premium' if order['premium'] else 'Free'})\n")
    print(f"Discount: {disc}%")
    print(f"Grand Total: ${grand}")
    print("\n- - - - - - - - - - - - - - - \n")


def calculate_discount(order):
    # Calculate discounts on mode of payment
    match (order['mode']):
        case 'cash':
            dis = 2
        case 'debit':
            dis = 5
        case 'credit':
            dis = 10
        case 'upi':
            dis = 12
        case _:
            dis = 0

    # Premium
    dis += 10 if order['premium'] else 0

    # Promocode
    codes = ['AXY641', 'DJSAIML', 'CODEAI']
    dis += 10 if order['promocode'] in codes else 0

    return dis


def shopping_cart(*items, **order_details):
    net_total = sum_key(items, key=1)

    # Generic Order dict
    order = {
        'mode': '',
        'address': '',
        'time': datetime.now().strftime("%d-%m-%Y"),
        'n_items': len(items),
        'premium': False,
        'promocode': ''
    }

    # Update order with user details
    for k, v in order_details.items():
        if k in order:
            order[k] = v

    dis = calculate_discount(order)

    grand_total = net_total - (net_total * (dis / 100))
    bill(net_total, grand_total, dis, items, order)


def menu(items):
    cart = []
    user = {}
    print("- - - BURGER KING MENU - - -")

    mlen = max_spaces(items)
    while True:
        os.system('cls')
        for i, item in enumerate(items):
            print(f"{i + 1}. {item[0].ljust(mlen)} - {("$" + str(item[1])).rjust(mlen)}")
        choice = input("Enter item choice (q to quit): ")
        if choice == 'q':
            print("Cart finalised!")
            break
        cart.append(items[int(choice) - 1])

    os.system('cls')
    print("Cart: ", end="")
    for c in cart:
        print(c[0], end=", ")
    print()

    # ADD INPUTS FOR USER DETAILS
    user['addr'] = input("Enter your address: ")

    os.system('cls')
    print("1. Cash \n2. Debit \n3. Credit \n4. UPI")
    match int(input("How would you like to pay? (1-4) ")):
        case 1:
            user['mode'] = 'cash'
        case 2:
            user['mode'] = 'debit'
        case 3:
            user['mode'] = 'credit'
        case 4:
            user['mode'] = 'upi'
        case _:
            user['mode'] = 'cash'

    os.system('cls')
    prm = input("Are you a premium user? (y/n) ")
    user['premium'] = True if prm == 'y' else False

    os.system('cls')
    coupon = input("Enter a promocode: (leave blank if none) ")
    if not coupon:
        user['promocode'] = None
    else:
        user['promocode'] = coupon

    return cart, user


its = [('Crispy Veg', 80), ('Crispy Chicken', 120), ('Veg Whopper', 130), ('Chicken Whopper', 170), ('Fries', 60),
       ('Nuggets', 80)]

cart, usr = menu(its)
shopping_cart(*cart, mode=usr['mode'], premium=usr['premium'], address=usr['addr'], promocode=usr['promocode'])
