def czy_palindrom(slowo):
    slowo = slowo.replace(" ", "").lower()
    return slowo == slowo[::-1]
print(czy_palindrom("kajak"))  
print(czy_palindrom("potop"))  
print(czy_palindrom("python")) 