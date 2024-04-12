# Checking Member-ship.

# We can check whether the character or string is the member of another string or not by using in and not in operators

# Comparison Of Strings.

#Comparing the First Letter Only.. (Alphabetical Order) 

a="ajith"
b="saran"
if(a==b):
    print("both are Equal")

elif(a>b):
    print("a is greater than b")
else:
    print("b is Greater")
    
    
#Remove Spaces.

# 1. rstrip()=>To remove spaces at right hand side 
# 2. lstrip()=>To remove spaces at left hand side
# 3. strip() =>To remove spaces both sides

# j=" ajith ganapathy "
# a=j.strip()
# print(a)


#Sub-String -> Later We Discuss..

#Counting Sub-string..

s="ajithganapathy"
print(s.count("a"))

#Replacing a String..
q="Madara is the God of Shinobi"
print(q.replace("Madara","Ajith"))

#Splitting Of Strings.

#Used to Split the Words.

e="ajithganapathy is a Good Boy"
l=e.split(" ")
print(l)


#Joining Of Strings.

#Seperate Words are joined to Form the Complete Single String.

k=["ajith","bala","saran"]
h="".join(k)
print(h)


#Changing Case Of A string.

# 1)UpperCase()
# 2)LowerCase()
# 3)SwapCase()
# 4)Title()
# 5)Capitalize()


# w="ajithganapathy"
# d=w.upper()
# print(d,"upper")
# f=d.lower()
# print(f,"lower")
# g=f.swapcase()
# print(g,"g")
# h=g.title()
# print(h,"title")
# j=h.capitalize()
# print(j,"capitalize")


# Checking the String Starts With & Ends With...

# b="Ajith is the God Of Shinobi"
# print(b.startswith("A"))
# print(b.endswith("s"))

#Checking the Type Of Character in Strings Or Not.

k="Ajith2333"
print(k.isalnum(),"isalnum")
l="Ajith@#$%^&8393"
print(l.isalnum(),"isalnum")

k="938373"
print(k.isdigit(),"isdigit")

