str1="hello hii"
str2="how are you"
print(str1+str2)
# string methods
# capitalise()
s1="hello whatsup"
print(s1.capitalize())
#uppermethod()
b1="hey whatsapp"
print(b1.upper())
#lowermethod()
q1="WHATSAPP HELLO"
print(q1.lower())
#countmethod()
l1="hello whtasapp how are you"
print(l1.count("a"))
#center method()
r1="hello"
print(r1.center(50))
#findmethod()
c1="let,s google the pineapple"
print(c1.find("the"))
#endswithmethod()
m1="give me my phone"
print(m1.endswith("e"))
#format method()
p1=("hello {name},which model is your phone. i want  {model} phone")
print(p1.format(name="ajmal",model="samsung"))

#isalpha model
h1="HEYBRO"
print(h1.isalpha())
#isalnum method()
u1="hello22"
print(u1.isalnum())
# isasccimethod
i1="ABC123abc"
print(i1.isascii())
#isdecimal method
y1="123450123"
print(y1.isdecimal())
#isdigit method
o1="345"
print(o1.isdigit())
#isupper method
a1="UWELCOME"
print(a1.isupper())
#islowermethod
x1="hai hello"
print(x1.islower())
#partition method
s1="hai bro how,s you"
print(s1.partition("bro"))

# replace method
ww1="orange is vegetable"
print(ww1.replace("vegetable","fruit"))

# lstrip method
c1="hello "
c2=c1.lstrip()
print(c1,"bro. my name is ajmal")
# rstrip method
z1="hello "
z2=z1.rstrip()
print(z1,"bro how are you")

# rfind method()
aa1="let,s google the pineapple"
print(aa1.rfind("l"))
# zfill method
qe1="9"
print(qe1.zfill(6))

# singlevariable multiple values
# lenfunction()
e1=("GOOGLG","THE","PINEAPPLE")
print(len(e1))
# concatination
q1=("asia","china","japan")
q2=("singapore","india")
print(q1+q2)

# slicing tuple method
# ss1="let,s google the pineapple"
# print(ss1[2:4])
# print(ss1[::-1])
# print(ss1[0:27])
# print(ss1[-27])

# removes method() in  list
zz1=["uk","america","europe","india"]
zz1.remove("uk")
print(zz1)