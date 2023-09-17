import os
import random
import string
import csv

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def generate_random_filename_vcf():
    # Generate a random filename
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"contact_{random_string}.vcf"

def split_vcf_contacts(vcf_file, num_contacts_per_file):
    #create splitted_vcf directory
    directory_path = "splitted_vcf"
    create_directory(directory_path)


    with open(vcf_file, 'r') as file:
        contacts = file.read().split('BEGIN:VCARD')
    
    # Remove the empty string at the beginning
    cont = [contact for contact in contacts if contact.strip() != '']
    contacts = []
    for contact in cont:
        contacts.append('BEGIN:VCARD' + contact)
    
    num_files = (len(contacts) + num_contacts_per_file - 1) // num_contacts_per_file
    
    for i in range(num_files):
        # Select a subset of contacts for this file
        start_idx = i * num_contacts_per_file
        end_idx = min((i + 1) * num_contacts_per_file, len(contacts))
        subset_contacts = contacts[start_idx:end_idx]

        
        # Create a random filename
        filename = generate_random_filename_vcf()
        
        # Write the subset of contacts to the new VCF file
        with open(f"{directory_path}/{filename}", 'w') as output_file:
            output_file.write(''.join(subset_contacts))
    
    print(f"{num_files} files generated.")



def generate_random_filename_csv():
    # Generate a random filename
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"contact_{random_string}.csv"

def split_csv_contacts(csv_file, num_contacts_per_file):

    #create splitted_vcf directory
    directory_path = "splitted_csv"
    create_directory(directory_path)


    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header line
        all_contacts = list(reader)
    
    num_files = (len(all_contacts) + num_contacts_per_file - 1) // num_contacts_per_file
    
    for i in range(num_files):
        # Select a subset of contacts for this file
        start_idx = i * num_contacts_per_file
        end_idx = min((i + 1) * num_contacts_per_file, len(all_contacts))
        subset_contacts = all_contacts[start_idx:end_idx]
        
        # Create a random filename
        filename = generate_random_filename_csv()
        
        # Write the subset of contacts to the new CSV file with the header
        with open(f"{directory_path}/{filename}", 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)  # Write the header line
            writer.writerows(subset_contacts)
    
    print(f"{num_files} files generated.")

if __name__ == "__main__":
    def is_csv_file(file_path):
        return file_path.lower().endswith(".csv")

    def is_vcf_file(file_path):
        return file_path.lower().endswith(".vcf")


    def csv_file():
        csv_file = input("Enter CSV File Name: ")
        if is_csv_file(csv_file):
            num_contacts_per_file = int(input("Enter the desired number of contacts per file: "))
    
            if os.path.isfile(csv_file):
                split_csv_contacts(csv_file, num_contacts_per_file)
            else:
                print(f"The file {csv_file} does not exist.")
        else:
            print("Error: Unsupported file type. please provide a CSV file.")


    def vcf_file():
        vcf_file = input("Enter VCF File Name: ")
        if is_vcf_file(vcf_file):
            num_contacts_per_file = int(input("Enter the desired number of contacts per file: "))
    
            if os.path.isfile(vcf_file):
                split_vcf_contacts(vcf_file, num_contacts_per_file)
            else:
                print(f"The file {vcf_file} does not exist.")
        else:
            print("Error: Unsupported file type. please provide a VCF file.")




    file = int(input("File extension:\n1. csv\n2.vcf\n1 or 2? "))
    if file == 1:
        csv_file()
    elif file == 2:
        vcf_file()
    else:
        print("Please Follow instrctions given")

