#Write a function asks user for birth month and returns correct birth stone, watch out for invalid inputs

def birth_stone():
    
    while True:
        month = int(input("What month were you born in?: "))
        if month>12 or month<1:
            print("INVALID INPUT, MONTH MUST BE FROM 1 TO 12")
            continue
        else: 
            break

    return stones[month]

stones={
    1:"Garnet",
    2:"Amethyst",
    3:"Aquamarine",
    4:"Diamond",
    5:"Emerald",
    6:"Pearl",
    7:"Ruby",
    8:"Peridot",
    9:"Sapphire",
    10:"Opal",
    11:"Topaz",
    12:"Turquoise"
}

print("\n"+birth_stone())