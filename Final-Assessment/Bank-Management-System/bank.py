import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MILI@75",
    database="bank_system_db"
)

cursor = conn.cursor()

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Update Customer Name")
    print("7. Delete Account")
    print("8. View Transaction History")
    print("9. Search Account")
    print("10. Bank Summary")
    print("11. Exit")

    choice = input("Enter Choice: ")

    # CREATE ACCOUNT

    if choice == "1":

        name = input("Enter Customer Name: ")
        mobile = input("Enter Mobile Number: ")

        if len(mobile) != 10:
            print("Invalid Mobile Number!")
            continue

        print("\nAccount Types")
        print("1. Savings")
        print("2. Current")

        acc_choice = input("Select Type: ")

        if acc_choice == "1":
            account_type = "Savings"
        else:
            account_type = "Current"

        initial_deposit = float(
            input("Enter Initial Deposit Amount: ")
        )

        if initial_deposit < 0:
            print("Invalid Amount!")
            continue

        cursor.execute(
            """
            INSERT INTO accounts
            (customer_name,balance,mobile,account_type)
            VALUES(%s,%s,%s,%s)
            """,
            (
                name,
                initial_deposit,
                mobile,
                account_type
            )
        )

        account_no = cursor.lastrowid

        cursor.execute(
            """
            INSERT INTO transactions
            (account_no,transaction_type,amount)
            VALUES(%s,%s,%s)
            """,
            (
                account_no,
                "INITIAL DEPOSIT",
                initial_deposit
            )
        )

        conn.commit()

        print("Account Created Successfully!")
        print("Your Account Number is:", account_no)

    # DEPOSIT

    elif choice == "2":

        account_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            continue

        cursor.execute(
            """
            SELECT *
            FROM accounts
            WHERE account_no=%s
            """,
            (account_no,)
        )

        account = cursor.fetchone()

        if not account:
            print("Account Not Found!")
            continue

        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_no = %s
            """,
            (amount, account_no)
        )

        conn.commit()

        cursor.execute(
            """
            INSERT INTO transactions
            (account_no,transaction_type,amount)
            VALUES(%s,%s,%s)
            """,
            (
                account_no,
                "DEPOSIT",
                amount
            )
        )

        conn.commit()

        print("Amount Deposited Successfully!")

    # WITHDRAW

    elif choice == "3":

        account_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            continue

        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_no = %s
            """,
            (account_no,)
        )

        result = cursor.fetchone()

        if result:

            balance = result[0]

            if balance >= amount:

                cursor.execute(
                    """
                    UPDATE accounts
                    SET balance = balance - %s
                    WHERE account_no = %s
                    """,
                    (amount, account_no)
                )

                cursor.execute(
                    """
                    INSERT INTO transactions
                    (account_no,transaction_type,amount)
                    VALUES(%s,%s,%s)
                    """,
                    (account_no, "WITHDRAW", amount)
                )

                conn.commit()

                print("Withdrawal Successful!")

            else:

                print("Insufficient Balance!")

        else:

            print("Account Not Found!")

    # CHECK BALANCE

    elif choice == "4":

        account_no = int(input("Enter Account Number: "))

        cursor.execute(
            """
            SELECT *
            FROM accounts
            WHERE account_no = %s
            """,
            (account_no,)
        )

        account = cursor.fetchone()

        if account:

            print("\n===== ACCOUNT DETAILS =====")
            print("Account No :", account[0])
            print("Name       :", account[1])
            print("Balance    :", account[2])
            print("Mobile     :", account[3])
            print("Type       :", account[4])

        else:

            print("Account Not Found!")

    # VIEW ALL ACCOUNTS

    elif choice == "5":

        cursor.execute(
            """
            SELECT *
            FROM accounts
            """
        )

        accounts = cursor.fetchall()

        if not accounts:
            print("No Accounts Found!")
        else:

            for acc in accounts:

                print("\n-------------------------")
                print("Account No :", acc[0])
                print("Name       :", acc[1])
                print("Balance    :", acc[2])
                print("Mobile     :", acc[3])
                print("Type       :", acc[4])
                print("-------------------------")

    # UPDATE NAME

    elif choice == "6":

        account_no = int(input("Enter Account Number: "))
        new_name = input("Enter New Customer Name: ")

        cursor.execute(
            """
            UPDATE accounts
            SET customer_name = %s
            WHERE account_no = %s
            """,
            (new_name, account_no)
        )

        conn.commit()

        print("Customer Name Updated Successfully!")

    # DELETE ACCOUNT

    elif choice == "7":

        account_no = int(
            input("Enter Account Number To Delete: ")
        )

        confirm = input(
            "Are you sure? (Y/N): "
        )

        if confirm.upper() == "Y":

            # Delete transaction history first
            cursor.execute(
                """
                DELETE FROM transactions
                WHERE account_no = %s
                """,
                (account_no,)
            )

            # Delete account
            cursor.execute(
                """
                DELETE FROM accounts
                WHERE account_no = %s
                """,
                (account_no,)
            )

            conn.commit()

            print("Account Deleted Successfully!")

        else:

            print("Deletion Cancelled!")

    # TRANSACTION HISTORY

    elif choice == "8":

        account_no = int(input("Enter Account Number: "))

        cursor.execute(
            """
            SELECT *
            FROM transactions
            WHERE account_no = %s
            """,
            (account_no,)
        )

        records = cursor.fetchall()

        if not records:

            print("No Transactions Found!")

        else:

            print("\n===== TRANSACTION HISTORY =====")

            for row in records:

                print("\nTransaction ID :", row[0])
                print("Account No     :", row[1])
                print("Type           :", row[2])
                print("Amount         :", row[3])
                print("Date           :", row[4])

    # SEARCH ACCOUNT

    elif choice == "9":

        account_no = int(
            input("Enter Account Number: ")
        )

        cursor.execute(
            """
            SELECT *
            FROM accounts
            WHERE account_no = %s
            """,
            (account_no,)
        )

        account = cursor.fetchone()

        if account:

            print("\n===== ACCOUNT DETAILS =====")

            print("Account No :", account[0])
            print("Name       :", account[1])
            print("Balance    :", account[2])
            print("Mobile     :", account[3])
            print("Type       :", account[4])

        else:

            print("Account Not Found!")

    # BANK SUMMARY

    elif choice == "10":

        cursor.execute(
            """
            SELECT
            COUNT(*),
            SUM(balance),
            AVG(balance)
            FROM accounts
            """
        )

        result = cursor.fetchone()

        print("\n===== BANK SUMMARY =====")

        print("Total Accounts :", result[0])
        print("Total Money    :", result[1])
        print("Average Balance:", result[2])

    # EXIT

    elif choice == "11":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")

conn.close()