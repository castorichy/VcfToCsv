import csv

def csv_to_vcf(csv_filename, vcf_file):
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            vcf_file.write('BEGIN:VCARD\n')
            vcf_file.write('VERSION:3.0\n')
            vcf_file.write(f'FN:{row["Name"]}\n')
            #vcf_file.write(f'EMAIL:{row["Email"]}\n')
            vcf_file.write(f'TEL;CELL:{row["Phone"]}\n')
            vcf_file.write('END:VCARD\n')

if __name__ == '__main__':
    vcf_filename = input("Enter output VCF file name: ")
    
    with open(vcf_filename, 'w+') as vcf_file:
        num_csv_files = int(input("Enter the number of CSV files: "))
        
        for i in range(num_csv_files):
            csv_filename = input(f"Enter CSV file name {i + 1}: ")
            csv_to_vcf(csv_filename, vcf_file)
            
    print("Merging and conversion complete.")

