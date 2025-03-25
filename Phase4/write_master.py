from read import read_old_bank_accounts

def write_master_bank_accounts(accounts, file_path):
    """
    Writes the Master Bank Accounts File in fixed-width 42-character format.
    Raises ValueError if invalid account data is encountered.
    """
    # Sort accounts by account_number as strings (for leading zero preservation)
    accounts = sorted(accounts, key=lambda acc: int(acc['account_number']))

    with open(file_path, 'w') as file:
        for acc in accounts:
            # Validate fields
            if not isinstance(acc['account_number'], str) or not acc['account_number'].isdigit():
                raise ValueError(f"Invalid account number: {acc['account_number']}")
            if len(acc['account_number']) > 5:
                raise ValueError(f"Account number too long: {acc['account_number']}")

            if len(acc['name']) > 20:
                raise ValueError(f"Name too long: {acc['name']}")
            if acc['status'] not in ('A', 'D'):
                raise ValueError(f"Invalid status: {acc['status']}")
            if not isinstance(acc['balance'], (int, float)):
                raise ValueError(f"Invalid balance type: {type(acc['balance'])}")
            if acc['balance'] < 0 or acc['balance'] > 99999.99:
                raise ValueError(f"Balance out of range: {acc['balance']}")
            if not isinstance(acc['total_transactions'], int) or acc['total_transactions'] < 0:
                raise ValueError(f"Invalid transaction count: {acc['total_transactions']}")

            # Format fields
            acc_num = acc['account_number'].zfill(5)
            name = acc['name'].ljust(20)[:20]
            status = acc['status']
            balance = f"{acc['balance']:08.2f}"
            txns = str(acc['total_transactions']).zfill(4)

            # Write formatted line
            file.write(f"{acc_num} {name} {status} {balance} {txns}\n")



# === MAIN ===
if __name__ == "__main__":
    input_file = "accounts.txt"
    output_file = "new_master_transactions.txt"

    accounts = read_old_bank_accounts(input_file)
    write_master_bank_accounts(accounts, output_file)
    print(f"Master Bank Accounts File written to {output_file}")
