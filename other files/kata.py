pin="12"
val_char="1234567890"
char=""
c=""
def validate_pin(pin):
    # print(type(pin))
    # print(pin)
    c=len(pin)
    print(c)
    print(type(c))
    if c == 4 or c == 6:
        for char in pin:
            if char not in val_char:
                print("a")
                return False
    else:
        print("a")
        return False
    print("z")
    return True

validate_pin(pin)