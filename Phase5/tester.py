from read import read_old_bank_accounts
from write import write_new_current_accounts
from write_master import write_master_bank_accounts

def main():
    # Step 1: Input and output file paths
    input_path = "accounts.txt"
    output_path = "current_accounts.txt"
    master_path = "new_master_transactions.txt"

    # Step 2: Read accounts from the old file
    accounts = read_old_bank_accounts(input_path)

    # Optional: Print parsed accounts for verification
    print("\n✅ Accounts read from file:")
    for acc in accounts:
        print(acc)

    # Step 3: Write both output files (current + master)
    try:
        write_new_current_accounts(accounts, output_path)
        write_master_bank_accounts(accounts, master_path)

        print(f"\n✅ Accounts successfully written to:")
        print(f"   - Current Accounts File: {output_path}")
        print(f"   - Master Accounts File: {master_path}")

    except ValueError as ve:
        print(f"\n❌ Validation error while writing: {ve}")
    except Exception as e:
        print(f"\n❌ Unexpected error while writing: {e}")

if __name__ == "__main__":
    main()
