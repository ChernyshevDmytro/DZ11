from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, name5):
        self.value = name5

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass

class Birthday(Field):
    pass

class Record:
    def __init__(self, name4, *args):
        self.name = name4
        self.phones = []
        self.add_phone(*args)
        self._birthday="00.00.0000"

    


    def add_phone(self, *args) -> None:
        for item in args:
            self.phones.append(item)

    def add_birthday(self, birthday) -> None:
        

        @property
        def birthday(self):
            return self._birthday

        @birthday.setter
        def birthday(self, birthday):
            if len (birthday) == 10:
                self._birthday=birthday
            else:
                print('Please enter correct birthday')

    def delete_phone(self, index) -> str:
        try:
            phone = self.phones.pop(index)
        except IndexError:
            return f"Sorry, there is no phone number with the index {index}"
        return f"phone {phone} deleted from contact {self.name}"

    def edit_phone(self, index, phone: Phone) -> str:
        try:
            self.phones[index] = phone
        except IndexError:
            return f"Sorry, there is no phone number to change with the index {index}"
        return f"""Phone with index {index} in record with name {self.name} changed on phone {phone}"""

    def __str__(self) -> str:
        if self._birthday != "00.00.0000":
            return f"Name: {self.name}, phones : {', '.join([str(p) for p in self.phones])}, birthday is {self._birthday}"
        else: return f"Name: {self.name}, phones : {', '.join([str(p) for p in self.phones])}"

    def __repr__(self) -> str:
        return f"Name: {self.name}, phones : {', '.join([str(p) for p in self.phones])}"

    def days_to_birthday (self)-> None:
        current_time=datetime.now()
        
        happy_birthday=datetime(year=current_time.year, month=int(self.birthday[3:5]), day=int(self.birthday[0:2]))
        days_to_birthday = happy_birthday - current_time
                      
        return print(f'{days_to_birthday.days} days left for { self.name} birthday')


class AddressBook(UserDict):
    current_index=0
    def add_record(self, obj):
        if isinstance(obj, Record):
            if obj.name.value in self.data.keys():
               
                self.data.update({obj.name.value: obj})
            else:
                self.data[obj.name.value] = obj  # , print("bbb")

    def del_record(self, obj):
        del self.data[obj.name.value]

    def delete_record(self, name: Name):
        print( f"Record with name {name} deleted from AddressBook")
        self.data.pop(name)
        

    def __str__(self) -> str:
        result = "\n".join([str(rec) for rec in self.data.values()])
        
        return result

    def __iter__(self):
        
        return self 

    def __next__(self):
        
        if self.current_index < len(self.data):
            self.current_index += 1             
            return  self.data
            
        raise StopIteration    

def input_error(get_handler):
    def inner(command1):
        try:
            get_handler(command1)
            return get_handler(command1)
        except ValueError as e:
            print(e)
            command1 = "help"
        except IndexError as e:
            print(e)
            command1 = "help"
        except TypeError as e:
            print(e)
            command1 = "help"
        except KeyError as e:
            print("hhhhhh")
            command1 = "help"
        return command1

    return inner


def input_():
    while True:
        user_command1 = input("Please, give me a command:")
        if (
            "hello" in user_command1
            or "exit" in user_command1
            or "close" in user_command1
            or "good bye" in user_command1
            or "show all" in user_command1
            or "phone" in user_command1
            or "add" in user_command1
            or "change" in user_command1
            or "add_phone" in user_command1
            or "del_phone" in user_command1
            or "edit_phone" in user_command1
            or "del_contact" in user_command1
            or "add_birthday" in user_command1
            or "birthday" in user_command1   
                     
        ):
            return user_command1
        continue


def normalization(user_command1):
    user_command1.casefold()
    user_command1_norm = user_command1
    return user_command1_norm


def input_error_2(parser):
    def inner(user_command1_norm):
        a = 0
        while a < 10:
            try:
                name, phone, command1, new_phone, birthday = parser(user_command1_norm)
                a += 1
                return name, phone, command1, new_phone, birthday
            except TypeError:
                print("Give me name and phone please")

            except IndexError:

                print("Give me true name or phone please2")

                while True:
                    user_command1 = input_()
                    user_command1_norm = normalization(user_command1)
                    try:
                        name, phone, command1, new_phone, birthday = parser(user_command1_norm)
                        a += 1
                        return name, phone, command1, new_phone, birthday
                    except:
                        print(f'"{phone}" is not a number. Try again')

            except ValueError:
                print("Give me true name or phone please3")

            except KeyError:
                print("Give me true name or phone please4")

    return inner


def help_func():
    user_command1 = input("Please, give me a new command1:")
    user_command1_norm = normalization(user_command1)
    name, phone, command1, new_phone, birthday = parser(user_command1_norm)
    return name, phone, command1, new_phone, birthday


@input_error_2
def parser(user_command1_norm):
    if user_command1_norm in ["hello", "exit", "close", "good bye", "show all"]:
        command1 = user_command1_norm
        return "", "", command1, "", ""

    elif "add_phone" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        name = c[1]
        command1 = c[0]
        if len(c) <= 2:
            phone = "no"
        else:
            phone = c[2]

        return name, phone, command1, "", ""

    elif "del_contact" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        name = c[1]
        command1 = c[0]
        if len(c) <= 2:
            phone = "no"
        else:
            phone = c[2]

        return name, phone, command1, "", "" 


    elif "del_phone" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        name = c[1]
        command1 = c[0]
        if len(c) <= 2:
            phone = "no"
        else:
            phone = c[2]

        return name, phone, command1, "", ""    


    elif "edit_phone" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        name = c[1]
        command1 = c[0]
        if len(c) <= 2:
            phone = "no"
        else:
            phone = c[2]
        
            new_phone = c[3]           

        return name, phone, command1, new_phone, ""                    
   
    elif "phone" in user_command1_norm:
        b = user_command1_norm.split("phone ")
        name = b[-1]
        command1 = "phone"
        return name, "", command1, "", ""    
  
    elif "add_birthday" in user_command1_norm:
        c = user_command1_norm.split(" ")
        name = c[1]
        command1 = c[0]
        
        if len(c[2]) < 10:
            birthday = "no"
        else:
           birthday = c[2]
           #print(birthday)
           #print(c[2])
        return name, "", command1, "", birthday

    elif "add" in user_command1_norm or "change" in user_command1_norm:
        c = user_command1_norm.split(" ")
        name = c[1]
        command1 = c[0]
        if len(c) <= 2:
            phone = "no"
        else:
            phone = c[2]
        return name, phone, command1, "", ""

    elif "birthday" in user_command1_norm:
        c = user_command1_norm.split(" ")
        name = c[1]
        command1 = c[0]
        #print(name)
        #print(command1)
        
        
        return name, "", command1, "", ''

        
    else:
        name = ""
        phone = ""
        command1 = "help"
        new_phone = ""
        return name, phone, command1, new_phone, birthday


def main():
    def close_func():
        print("Good bye!")

    def show_func():
        for contact in c_b.data:
            print(f'{c_b.data[contact]}')#
            #print(next(c_b))
            #print(c.obj)
        #for k,v in c.data.items():
            #print(f'{k}, {v}')
            #print('.........')    
        
        #print(c_b)
        # print(c_b.data.values)
        # for k, v in c_b.data.items():
        #     for i in v:
        #         if isinstance(i, Record):
        #             for g in i.phone:
        #                 print(f"{k} {g}")

    def phone_func():
        if name in c_b.data.keys():
            print(c_b.get(name).phones)
        #     for j, i in enumerate(c_b.data.get(name)):
        #         if i.phone:

        #             print(f"{name} {i.phones.value}")
        # else:
        #     print(f"{name} is not in contact book")

    def add_func():
        if name in c_b.data.keys():
            add_phone_func()
        else: c_b.add_record(record)

    def del_contact_func():     
        c_b.delete_record(name)
           

    def hello_func():
        print("How can I help you?")

    def add_phone_func():
        record=c_b.data.get(name)
        record.add_phone(phone1)
        c_b.add_record(record)

    def del_phone_func():
        record=c_b.data.get(name)        
        for i, j in enumerate(record.phones):                       
            if phone == str(j) and j != None:                  
                record.delete_phone(i)
                c_b.add_record(record)

    def edit_phone_func():
        record=c_b.data.get(name)
        for i, j in enumerate(record.phones):                       
            if phone == str(j) and j != None:                  
                record.edit_phone(i, new_phone)
                c_b.add_record(record)       

    def add_birthday_func():
        if name in c_b.data.keys():
            record=c_b.data.get(name)
            record.add_birthday(birthday)            
        else: print("Name is absent")

    def birthday_func():
        if name in c_b.data.keys():
            print(c_b.get(name).birthday) 
            record=c_b.data.get(name)
            record.days_to_birthday()     


    command1S = {
        "good bye": close_func,
        "close": close_func,
        "exit": close_func,
        "show all": show_func,
        "phone": phone_func,
        "change": add_func,
        "add": add_func,
        "add_phone": add_phone_func,
        "del_phone": del_phone_func,
        "hello": hello_func,
        "edit_phone": edit_phone_func,
        "help": help_func,
        "del_contact": del_contact_func,
        "add_birthday": add_birthday_func,
        "birthday": birthday_func,
    }

    @input_error
    def get_handler(command1):
        return command1S[command1]

    c_b = AddressBook()

    while True:

        user_command1 = input_()

        if user_command1 in ["close", "good bye", "exit"]:
            close_func()
            break

        user_command1_norm = normalization(user_command1)

        name, phone, command1, new_phone, birthday = parser(user_command1_norm)

        name1 = Name(name)
        # name1.value = name
        phone1 = Phone(phone)
        # phone1.phone = phone
        record = Record(name1, phone1)
        # record.add_phone(Phone(phone))

        if command1 is not None:

            #print(name)
            #print(new_phone)
            #print(phone)
            #print(command1)
            #print(birthday)

            a = get_handler(command1)
            a()


if __name__ == "__main__":

    main()
