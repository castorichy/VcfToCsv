import csv
import re
from time import sleep
import quopri
import json

def country_code() -> list:
    with open('country_code.json', 'r') as p:
        codes = p.read()
        codes_list = json.loads(codes)
        return codes_list 
#print(country_code())

def checkNumber(phone_num) -> str:
    codes = country_code()

    phone = ""
    for n in phone_num:
        if n == '-':
            continue
        else:
            phone += n




    if len(phone) >= 10 and len(phone) < 14:
        c_code = phone[0:-9]
        if c_code == '0':
            return phone
        elif c_code[0] == '+':
            c_code = c_code[1:]
            if int(c_code) in codes:
                return phone
            else:
                return ''
        else:
            if int(c_code) in codes:
                return '+' + phone
            else:
                return ''
    else:
      #  print(phone)
        return ''

def decodeString(name) -> str:
    decoded_string = quopri.decodestring(name)
    return decoded_string.decode('utf-8')

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
    Phone = ""
    for line in file:
        name = re.findall('FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:(.*)', line)
        nm = ''.join(name)
        nm = decodeString(nm)
        #print(nm)
        if len(nm) == 0:
            continue

        name = nm.strip()
        Name = FName_rename(name, re_name)
        #contact.append(name)

        for lin in file:
            tel = re.findall('TEL;CELL:?(?:PREF)?:(.*)', lin)
            tel = ''.join(tel)
            tel = checkNumber(tel)

            if tel == '':
                continue

            tel = tel.strip()
            tel = ''.join(tel)#e for e in tel if e.isalnum())
            #print(tel)

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
