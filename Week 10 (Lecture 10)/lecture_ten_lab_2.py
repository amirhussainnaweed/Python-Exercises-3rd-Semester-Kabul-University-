
import sqlite3

# -----------------------------
# 1. Connect to the database
# -----------------------------

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

# -----------------------------
# 2. Create the accounts table
# -----------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL NOT NULL
    )
""")

connection.commit()

print("Accounts table created successfully.")

# -----------------------------
# 3. Insert two sample accounts
# -----------------------------

cursor.execute("SELECT COUNT(*) FROM accounts")
account_count = cursor.fetchone()[0]

if account_count == 0:

    accounts = [
        ("Ali", 1000),
        ("Sara", 500)
    ]

    cursor.executemany("""
        INSERT INTO accounts (name, balance)
        VALUES (?, ?)
    """, accounts)

    connection.commit()

    print("Two sample accounts inserted successfully.")

else:
    print("Sample accounts already exist.")


# -----------------------------
# 4. Display account balances
# -----------------------------

def display_balances():

    print("\n--- ACCOUNT BALANCES ---")

    cursor.execute("SELECT * FROM accounts ORDER BY id")
    records = cursor.fetchall()

    for account in records:
        print(
            f"ID: {account[0]} | "
            f"Name: {account[1]} | "
            f"Balance: ${account[2]:.2f}"
        )


# -----------------------------
# 5. Transfer money function
# -----------------------------

def transfer_money(sender_id, receiver_id, amount):

    try:

        # Validate the transfer amount
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        # Prevent transferring to the same account
        if sender_id == receiver_id:
            raise ValueError("Sender and receiver cannot be the same.")

        # Start a transaction
        connection.execute("BEGIN IMMEDIATE")

        # Check if sender exists
        cursor.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (sender_id,)
        )

        sender = cursor.fetchone()

        if sender is None:
            raise ValueError("Sender account does not exist.")

        # Check if receiver exists
        cursor.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (receiver_id,)
        )

        receiver = cursor.fetchone()

        if receiver is None:
            raise ValueError("Receiver account does not exist.")

        # Check sender's balance
        sender_balance = sender[0]

        if sender_balance < amount:
            raise ValueError("Insufficient balance.")

        # Subtract money from sender
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, sender_id)
        )

        if cursor.rowcount != 1:
            raise sqlite3.DatabaseError(
                "Failed to update sender account."
            )

        # Add money to receiver
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, receiver_id)
        )

        if cursor.rowcount != 1:
            raise sqlite3.DatabaseError(
                "Failed to update receiver account."
            )

        # Commit only if both updates succeed
        connection.commit()

        print(
            f"\nTransfer of ${amount:.2f} "
            "completed successfully."
        )

    except (ValueError, sqlite3.Error) as error:

        # Undo all changes if something goes wrong
        connection.rollback()

        print(f"\nTransfer failed: {error}")
        print("Transaction rolled back.")


# -----------------------------
# 6. Display balances before transfer
# -----------------------------

print("\n--- BEFORE TRANSFER ---")

display_balances()


# -----------------------------
# 7. Perform the transfer
# -----------------------------

sender_id = 1
receiver_id = 2
amount = 200

print("\n--- TRANSFER ---")

transfer_money(sender_id, receiver_id, amount)


# -----------------------------
# 8. Display balances after transfer
# -----------------------------

print("\n--- AFTER TRANSFER ---")

display_balances()


# -----------------------------
# 9. Close database connection
# -----------------------------

connection.close()

print("\nDatabase connection closed.")
