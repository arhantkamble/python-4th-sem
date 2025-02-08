a="pyTHon Is FUN"

print("Original String =",a)
print("upper() :",a.upper())
print("isupper() :",a.isupper())
print("lower() :",a.lower())
print("title() :",a.title())
print("istitle() :",a.istitle())
print("swapcase() :",a.swapcase())
print("capitalize() :",a.capitalize())
print("center() :",a.center(30))
print("count() :",a.count("n"))
print("find() :",a.find("FUN"))
print("endswith() :",a.endswith("FUN"))
print("replace() :",a.replace("FUN", "Nice"))

b="Python123"
print("isalnum() :",b.isalnum())

c="HelloWorld"
print("isalpha() :",c.isalpha())

d="12345"
print("isdecimal() :",d.isdecimal())

e="   Hello Python!"
print("lstrip() :",e.lstrip())

f="Hello Python!   "
print("rstrip() :",f.rstrip())

g=" "
print("isspace() :",g.isspace())

print("concatinated string :",b + "  " + c)

h="Python"
length=8
print("rjust() :",h.rjust(length))