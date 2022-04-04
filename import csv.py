import csv

filename="ss.csv"
contacts=[{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ["name", "email", "phone", "favorite"]
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        print(contacts[0])
        print(contacts[1])
        print(len(contacts))
    for i in contacts: 
        
        
        print(i)
        writer.writerow({'name': i['name'], 'email': i['email'], 'phone':i['phone'], 'favorite': i['favorite']})
def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        a=[]
        for row in reader:
            
            b={'name':row['name'], 'email':row['email'], 'phone':row['phone'], 'favorite':row['favorite']}
            a.append(b)   
        return  a

a=write_contacts_to_file(filename, contacts)
b=read_contacts_from_file(filename)