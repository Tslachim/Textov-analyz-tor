"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Stuchlík 
email: tslachim@gmail.com
discord: Mišakus#1763
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

name_password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz":"pass123"}
separator = "-" * 40

user = input("Please enter your name: ").lower() # .lower() = user-friendly
password = input("Please enter your password: ")

if user in name_password:
    if name_password[user] == password:
        print(separator, f"Welcome to the app, {user.title()} \nWe have 3 texts to be analyzed.", separator ,  sep="\n")
    else:
        print("Password is wrong! Terminating the program ....")
        quit()
else:
    print(f"User:{user} \nUnregistred user! Terminating the program ....")
    quit()

text_num = input("Enter a number btw. 1 and 3 to select: ")
print(separator)

if text_num.isnumeric and int(text_num) >= 1 and int(text_num) <=3: 
    for i in TEXTS[text_num - 1]:                 # udělej to přes for for word in TEXTS[text_num - 1].split(" "): tohle == slepá ulička zatím 
        

            #počet slov

            #počet slov začínajících velkým písmenem,  if istitle() tak přiřaď do skupiny kde mají první velké

            #počet slov psaných velkými písmeny,     - if isupper() pak přiřaď do listu velká písmena?

            #počet slov psaných malými písmeny,     - if islower() pak přiřaď do listu malá pismena?

            #počet čísel (ne cifer),                if str. isnumeric pak jej přiřaď do číselné promněnné

            #sumu všech čísel (ne cifer) v textu.       count celou číselnou promněnou


elif not text_num.isnumeric:                                                          # pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
    print("Your entred value is not number! Terminating the program ....")
    quit()
else:                                                                                    # Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
    print("Your entred number is out of 1 - 3. Terminating the program ...")
    quit()


