import subprocess
import csv
import os
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

def get_contacts_from_mac():
#    Retrieves contact information from the macOS Address Book using the 'osascript' command.

#     Returns:
#         list: A list of dictionaries, where each dictionary represents a contact.
#               Returns None if an error occurs.
#     """
        # AppleScript command to get contact information
    script = """
        tell application "Contacts"
            set theContacts to {}
            repeat with aPerson in people
                set theContact to {}
                set end of theContact to value of first name of aPerson
                set end of theContact to value of last name of aPerson
                set thePhones to {}
                repeat with aPhone in phones of aPerson
                    set end of thePhones to value of aPhone
                end repeat
                set end of theContact to thePhones
                set theEmails to {}
                repeat with anEmail in emails of aPerson
                    set end of theEmails to value of anEmail
                end repeat
                set end of theContact to theEmails
                set end of theContacts to theContact
            end repeat
            return theContacts
        end tell
        """

        # Execute the AppleScript command
    process = subprocess.Popen(
            ["osascript", "-e", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    stdout, stderr = process.communicate()

        # Check for errors
    if stderr:
        print(f"Error executing AppleScript: {stderr.decode()}")
        return None

        # Process the output
    output = stdout.decode().strip()
    if not output:
        print("No contacts found.")
        return []

        # Parse the output
    contacts = []
    contact_entries = output.split("}, {")
    for entry in contact_entries:
        print (f"Processing entry: {entry}")
        parts = entry.split(", ")
        if len(parts) < 4:
            print(f"Skipping incomplete entry: {entry}")
            continue
        first_name = parts[0].split(": ")[1].strip("'")
        last_name = parts[1].split(": ")[1].strip("'")
        phones = [part.split(": ")[1].strip("'") for part in parts[2].split("}, {")]
        emails = [part.split(": ")[1].strip("'") for part in parts[3].split("}, {")]
        contacts.append({
            "First Name": first_name,
            "Last Name": last_name,
            "Phones": phones,
            "Emails": emails
        })
    return contacts
# Example usage 
contacts = get_contacts_from_mac()
print(contacts)
# Save contacts to a CSV file
if contacts:   
    csv_file = 'contacts.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name", "Phones", "Emails"])
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
    print(f"Contacts saved to {csv_file}")
# Save contacts to an Excel file
    excel_file = 'contacts.xlsx'
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Contacts"
    # Write header
    sheet.append(["First Name", "Last Name", "Phones", "Emails"])   
    # Write data
    for contact in contacts:
        sheet.append([
            contact["First Name"],
            contact["Last Name"],
            ", ".join(contact["Phones"]),
            ", ".join(contact["Emails"])
        ])
    workbook.save(excel_file)
    print(f"Contacts saved to {excel_file}")
else:
    print("No contacts found.")
