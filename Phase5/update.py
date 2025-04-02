def update(accounts, file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print("Error reading file:", e)
        return

    new_lines = []
    for line in lines:
        line_stripped = line.rstrip("\n")
        if len(line_stripped) < 5:
            new_lines.append(line)
            continue

        # Extract fixed-width fields:
        file_acc = line_stripped[0:5]       # positions 0-4: account number (5 characters)
        file_name = line_stripped[6:26]       # positions 6-25: name (20 characters)
        
        updated_line = line  # Default to original line if no match is found.
        for acc in accounts:
            if file_acc[:4] == acc['account_number']:
                new_status = acc['status']
                new_balance = "{:08.2f}".format(acc['balance'])
                new_total = "{:04d}".format(acc['total_transactions'])
                new_plan = acc['plan']
                # Rebuild the line with the exact fixed widths.
                updated_line = "{:5s} {:20s} {:1s} {:8s} {:4s} {:2s}\n".format(
                    file_acc, file_name, new_status, new_balance, new_total, new_plan
                )
                break

        new_lines.append(updated_line)

    # Debug: print the new file content for verification.
    print("New file content to be written:")
    for nl in new_lines:
        print(nl, end="")

    try:
        with open(file_path, "w") as f:
            f.writelines(new_lines)
        print("\nFile update successful.")
    except Exception as e:
        print("Error writing file:", e)




# Testing purposes

# from read import read_old_bank_accounts

# accounts = read_old_bank_accounts("accounts.txt")


# # Modify a specific account
# for acc in accounts:
#     if acc['account_number'] == "1234":
#         acc['balance'] += 5000
#         acc['total_transactions'] += 1
#         acc['status'] = 'D'
#         acc['plan'] = 'SP'

# for acc in accounts:
#     print(acc)


# # Update the file
# update(accounts, "accounts.txt")
