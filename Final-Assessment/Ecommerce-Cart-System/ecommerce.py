import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MILI@75",
    database="ecommerce_cart_system_db"
)

cursor = conn.cursor()

while True:

    print("\n===== ECOMMERCE CART SYSTEM =====")
    print("1. View Products")
    print("2. Add Product")
    print("3. Add To Cart")
    print("4. View Cart")
    print("5. Remove From Cart")
    print("6. Generate Bill")
    print("7. Clear Cart")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        cursor.execute(
            """
            SELECT *
            FROM products
            """
        )

        products = cursor.fetchall()

        print("\n===== PRODUCTS =====")

        for product in products:

            print(
                product[0],
                "|",
                product[1],
                "| ₹",
                product[2]
            )

    elif choice == "8":

        print("Thank You!")
        break

    elif choice == "2":

        product_name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))

        cursor.execute(
            """
            INSERT INTO products(product_name,price)
            VALUES(%s,%s)
            """,
            (product_name, price)
        )

        conn.commit()

        print("Product Added Successfully!")

    elif choice == "3":

        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))

        cursor.execute(
            """
            INSERT INTO cart(product_id,quantity)
            VALUES(%s,%s)
            """,
            (product_id, quantity)
        )

        conn.commit()

        print("Product Added To Cart!")

    elif choice == "4":

        cursor.execute(
            """
            SELECT
            c.cart_id,
            p.product_name,
            p.price,
            c.quantity,
            (p.price*c.quantity) AS total
            FROM cart c
            INNER JOIN products p
            ON c.product_id=p.product_id
            """
        )

        items = cursor.fetchall()

        print("\n===== CART ITEMS =====")

        for item in items:

            print("\n----------------------------")
            print("Cart ID :", item[0])
            print("Product :", item[1])
            print("Price   :", item[2])
            print("Qty     :", item[3])
            print("Total   :", item[4])
            print("----------------------------")

    elif choice == "5":

        cart_id = int(
            input("Enter Cart ID To Remove: ")
        )

        cursor.execute(
            """
            DELETE FROM cart
            WHERE cart_id=%s
            """,
            (cart_id,)
        )

        conn.commit()

        print("Item Removed Successfully!")

    elif choice == "6":

        cursor.execute(
            """
            SELECT
            p.product_name,
            p.price,
            c.quantity,
            (p.price*c.quantity) AS total
            FROM cart c
            INNER JOIN products p
            ON c.product_id=p.product_id
            """
        )

        items = cursor.fetchall()

        grand_total = 0

        print("\n===== BILL =====")

        for item in items:

            print(
                item[0],
                "| Price:", item[1],
                "| Qty:", item[2],
                "| Total:", item[3]
            )

            grand_total += float(item[3])

        print("\nGrand Total = ₹", grand_total)

    elif choice == "7":

        confirm = input(
            "Clear Entire Cart? (Y/N): "
        )

        if confirm.upper() == "Y":

            cursor.execute(
                """
                DELETE FROM cart
                """
            )

            conn.commit()

            print("Cart Cleared Successfully!")

        else:

            print("Operation Cancelled!")

    elif choice == "8":

        print("Thank You!")
        break