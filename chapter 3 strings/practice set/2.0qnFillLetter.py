from datetime import date
# wapp to fill in a letter template fiven below with name and date.
name=input("Enter your name ")
letter = '''Dear <|NAME|>,
You are selected
Dare: <|Date|>  
'''
letter=letter.replace("<|NAME|>",name.capitalize())
ajakodate =str(date.today())
letter=letter.replace(("<|Date|>"), ajakodate)
print(letter)
