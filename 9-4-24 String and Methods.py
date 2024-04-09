# Strings 

# If the word or Letters or numbers comes under the Double quotation or Single Quotation 

# a="ajith"
# print(a)
# print(type(a))


# List, tuple & String can only be Acceseed by the Index & Slicing.

b="manoj"
print(b[0]) #Indexing Method.

print(b[::-1]) #Reversing..

print(b[:2])

# Index => Able to Access the One value
#Slicing => Able to Access the Multiple Value..


print("Slicing Method")

k="ajithganapathy"
print("jet",k[0:9:2])

#Concatenation

s="saran"
p="arun"
print(s+" "+p)


l="100"
print(l*3)

#Length Function

y="obulesu"
print(len(y))


d="ajithganapathy"
print("In Forward Direction")
for i in d:
    print(i,end=" ")
print("------------------")
print("\n")
print("In Backward Direction")
for k in d[::-1]:
    print(k,end=" ")
    
    

