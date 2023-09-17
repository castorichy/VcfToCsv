# Specify the path to your VCF file
vcf_file_path = 'whatspromoSave.csv'
contact_name = "☔ SV WtsPromo "
output_csv_file = 'whatspromoSaveRen.csv'

# Open the VCF file for reading
with open(vcf_file_path, 'r') as vcf_file, open(output_csv_file, 'w') as csv_write:
    for indx, line in enumerate(vcf_file):
        # Process each line here
        Phone_details = line.split(",")  # Print the line (strip removes leading/trailing whitespace)
        Phone_details[0] = contact_name + str(indx)
        csv_write.write(f"{Phone_details[0]},{Phone_details[1]}")

