# Dictionary Methods

a={1:"ajith",2:"saran",3:"susmitha"}
print(a)
print(type(a))
print(len(a))   # finding the Length of Dictionary

#Delete Method in Dictionary
del a[2]
print(a)


# get Keyword in Python(Dictionary)
print(a.get(1))

#Update Method in Dictionary..

a[6]="ajithganapathy"
a[9]="varata"
a[0]="rajini"
print(a)


#Pop Method in Dictionary.
print(a.pop(1))


#Pop item..
print(a.popitem(),"ajith")

print(a.keys) #Only the Keys will get Printed.
print(a.values) # Only the Values will get Printed.


#Items..
for k,v in a.items():
    print(k,"---",v)
    


