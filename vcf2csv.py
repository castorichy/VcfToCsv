import csv
import re
from time import sleep
#re_name = input("Rename with?: ")

def FName_rename(contact_name, re_name) -> str:
    #re_name = input("Rename with?: ")
    Name = re_name + contact_name

    return Name


def VcfReader():

    file_name = input("Enter the file name: ")
    ans = str(input("Do you want to add character in name? Y/n"))
    if ans == 'y' or ans == 'Y':
        re_name = input("Rename with?: ")
    else:
        re_name = ''

    out_name = input("OutPut file name eg qawed.csv: ")

    print("\nprocessing...\n")
    sleep(2)


    file = open(file_name, 'r', encoding="utf-8")
    Name = ""
    for line in file:
        name = re.findall('FN:(.*)', line)
        nm = ''.join(name)
        if len(nm) == 0:
            continue

        name = nm.strip()
        Name = FName_rename(name, re_name)
        #contact.append(name)

        for lin in file:
            tel = re.findall('TEL;TYPE=CELL:?(?:PREF)?:(.*)', lin)
            tel = ''.join(tel)

            if len(tel) == 0:
                continue

            tel = tel.strip()
            tel = ''.join(e for e in tel if e.isalnum())

            phone = tel
            Phone = phone
            #contact.append(phone)
            break
        writeToCsv(out_name, Name, Phone)
        #print(Name, phone)



def writeToCsv(file_name, name, phone):
    """saves To A csv file"""
    with open(file_name, 'a', newline = '') as f:
        writer = csv.writer(f)
        #writer.writerow(["Name","Phone"])
        writer.writerow([name, phone])

VcfReader()
