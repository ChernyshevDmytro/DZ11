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
    def __init__(self, phone):
        self.value = phone        
        self._current_phone =''
        self._new_phone =''

name='gggg'
phone=7777777
name1 = Name(name)
# name1.value = name
phone1 = Phone(phone)
print(phone1.value)

                