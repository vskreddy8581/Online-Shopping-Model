cart = []

def laptops():
    print("----SELECT COMPANY----")
    print("""
    1. HP
    2. Lenovo
    3. Acer
    4. Dell
    """)
    i = int(input("Select from the above: "))
    if i == 1:
        HP()
    elif i == 2:
        lenovo()
    elif i == 3:
         acer()
    elif i == 4:
        dell()
    else:
        print("Invalid selection.")

def HP():
    print("----HP LAPTOPS----")
    print("""
    1. HP Omen Laptop 
       Price: 1,20,000    
       Processor: Intel i7

    2. HP 15s Model    
       Price: 62,000
       Processor: Intel i7 with Intel Iris Graphics Card
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("HP Omen Laptop", 120000)
    elif choice == 2:
        add_to_cart("HP 15s Model", 62000)
    else:
        print("Invalid choice")

def dell():   
    print("----DELL LAPTOPS----")
    print("""
    1. Dell 15
       Price: 65,000
       Processor: Intel i5

    2. Dell Inspiron 15
       Price: 57,999
       Processor: Intel i7, 16GB RAM, 512GB SSD
    """) 
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Dell 15", 65000)
    elif choice == 2:
        add_to_cart("Dell Inspiron 15", 57999)
    else:
        print("Invalid choice")

def lenovo():
    print("----LENOVO LAPTOPS----")
    print("""
    1. Lenovo LOQ Model
       Price: 63,000
       Intel i5 Processor

    2. Lenovo Slim Ideapad
       Price: 54,000
       16GB RAM, 512GB SSD
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Lenovo LOQ", 63000)
    elif choice == 2:
        add_to_cart("Lenovo Slim Ideapad", 54000)
    else:
        print("Invalid choice")

def acer():
    print("----ACER LAPTOPS----")
    print("""
    1. Acer ROG
       Price: 73,000
       Ryzen 5 Processor

    2. Acer Vivobook 16x
       Price: 57,000
       Intel i7 Processor
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Acer ROG", 73000)
    elif choice == 2:
        add_to_cart("Acer Vivobook 16x", 57000)
    else:
        print("Invalid choice")

def mobiles():
    print("----MOBILE COMPANIES----")
    print("""
    1. Vivo
    2. Samsung
    3. iQOO
    4. iPhone
    """)
    j = int(input("Select from the above: "))
    if j == 1:
        vivo()
    elif j == 2:
        samsung()
    elif j == 3:
        iqoo()
    elif j == 4:
        iphone()
    else:
        print("Invalid selection.")

def vivo():
    print("----VIVO MOBILES----")
    print("""
    1. Vivo Y75
       Price: 17,000
       8GB RAM / 128GB Storage

    2. Vivo Y54
       Price: 13,999
       6GB RAM / 128GB Storage
    """)
    choice = int(input("Enter choice to add to cart: "))
    match choice:
        case 1: add_to_cart("Vivo Y75", 17000)
        case 2: add_to_cart("Vivo Y54", 13999)
        case _: print("Invalid choice")

def samsung():
    print("----SAMSUNG MOBILES----")
    print("""
    1. S24 Ultra - ₹77,000
       8GB RAM / 128GB SSD

    2. S24 Model - ₹49,999
       Snapdragon 7 Gen 2, 8GB RAM / 128GB SSD

    3. S23 Ultra - ₹63,999
       12GB RAM / 256GB SSD, 6.7-inch OLED
    """)
    choice = int(input("Enter choice to add to cart: "))
    match choice:
        case 1: add_to_cart("Samsung S24 Ultra", 77000)
        case 2: add_to_cart("Samsung S24", 49999)
        case 3: add_to_cart("Samsung S23 Ultra", 63999)
        case _: print("Invalid choice")

def iqoo():
    print("----IQOO MOBILES----")
    print("""
    1. IQOO Z9x 5G
       Price: 14,000
       Snapdragon 6 Gen 1

    2. IQOO Z9 5G
       Price: 19,000
       Mediatek Dimensity 7200
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("IQOO Z9x 5G", 14000)
    elif choice == 2:
        add_to_cart("IQOO Z9 5G", 19000)
    else:
        print("Invalid choice")

def iphone():
    print("----IPHONES----")
    print("""
    1. iPhone 15 - ₹73,999
    2. iPhone 15 Max - ₹99,999
    3. iPhone 16 - ₹89,675
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("iPhone 15", 73999)
    elif choice == 2:
        add_to_cart("iPhone 15 Max", 99999)
    elif choice == 3:
        add_to_cart("iPhone 16", 89675)
    else:
        print("Invalid choice")

def clothes():
    print("----CLOTHES----")
    print("""
    1. Shirt
    2. T-Shirt
    3. Jeans
    4. Night Pants
    """)
    j = int(input("Select from the above: "))
    if j == 1:
        shirts()
    elif j == 2:
        tshirt()
    elif j == 3:
        jeans()
    elif j == 4:
        nightpants()
    else:
        print("Invalid selection.")

def shirts():
    print("----SHIRTS----")
    print("""
    1. Black Checks Shirt - ₹550
    2. White Shirt - ₹999
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Black Checks Shirt", 550)
    elif choice == 2:
        add_to_cart("White Shirt", 999)
    else:
        print("Invalid choice")

def tshirt():
    print("----T-SHIRTS----")
    print("""
    1. Printed T-Shirt - ₹450
    2. Plain Blue T-Shirt - ₹499
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Printed T-Shirt", 450)
    elif choice == 2:
        add_to_cart("Plain Blue T-Shirt", 499)
    else:
        print("Invalid choice")

def jeans():
    print("----JEANS----")
    print("""
    1. Blue Jeans - ₹1400
    2. Black Jeans - ₹1600
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Blue Jeans", 1400)
    elif choice == 2:
        add_to_cart("Black Jeans", 1600)
    else:
        print("Invalid choice")

def nightpants():
    print("----NIGHT PANTS----")
    print("""
    1. Cotton Night Pants - ₹600
    2. Silk Night Pants - ₹850
    """)
    choice = int(input("Enter choice to add to cart: "))
    if choice == 1:
        add_to_cart("Cotton Night Pants", 600)
    elif choice == 2:
        add_to_cart("Silk Night Pants", 850)
    else:
        print("Invalid choice")

def add_to_cart(item, price):
    cart.append({"item": item, "price": price})
    print(f"{item} added to cart successfully!")

def view_cart():
    if not cart:
        print("Cart is empty.")
    else:
        total = 0
        print("\n----CART ITEMS----")
        for idx, val in enumerate(cart, start=1):
            print(f"{idx}. {val['item']} - ₹{val['price']}")
            total += val['price']
        print(f"\nTotal amount: ₹{total}")
        delete_opt = input("Do you want to delete an item from the cart? (yes/no): ").lower()
        if delete_opt == "yes":
            delete_cart()

def delete_cart():
    if not cart:
        print("Cart is empty — nothing to delete.")
        return
    try:
        item_no = int(input("Enter item number to delete: "))
        if 0 < item_no <= len(cart):
            removed = cart.pop(item_no - 1)
            print(f"{removed['item']} removed from the cart.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def products():
    while True:
        print("\n-----PRODUCTS AVAILABLE-----")
        print("""
        1. Laptops
        2. Mobiles
        3. Clothes
        4. View Cart
        5. Exit
        """)
        value = int(input("Select from the above: "))
        if value == 1:
            laptops()
        elif value == 2:
            mobiles()
        elif value == 3:
            clothes()
        elif value == 4:
            view_cart()
        elif value == 5:
            print("Thank you for shopping! Goodbye!")
            break
        else:
            print("Invalid selection.")

products()
