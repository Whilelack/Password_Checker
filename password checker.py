import re
password = input()
score = 0

if (len(password) > 8):
    score = score + 5
if re.search("[a-z]", password):
    score = score + 5
if re.search("[A-Z]", password):
    score = score + 5
if re.search("[0-9]", password):
    score = score + 5
if re.search("[_@$!]", password):
    score = score + 5

if 0 <= score <= 10 :
    print("Zwak wachtwoord")
if 11 <= score <= 15:
    print("Matig wachtwoord")
if 16 <= score <= 20:
    print("Sterk wachtwoord")
if 21 <= score <= 25:
    print("Erg sterk wachtwoord")
