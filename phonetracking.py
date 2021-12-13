photos={"camera":10,"instagram images":25,"canva":1,"screenshots":100}
photos["googlelens"]=12
photos["snapchat"]=6
photos["snapseed"]=5       
photos["B216"]=2

print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)
