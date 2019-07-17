# File: pythonLearn.py

a = 100
b = 50
i = 1
#x = 8
#x = x + 3

fruitList = ["apple", "banana", "cherry"]
fruitList[1] = "blackcurrant"
print("Added at second place--> blackcurrant")
print(fruitList)
print(len(fruitList))
print\

fruitList.append("orange")
print("Append--> orange")
print(fruitList)
print(len(fruitList))
print\

fruitList.insert(1, "mango")
print("Insert--> mango")
print(fruitList)
print(len(fruitList))
print\

fruitList.remove("cherry")
print("Remove--> cherry")
print(fruitList)
print(len(fruitList))
print\

fruitList.pop()
print("POP--> last element deleted")
print(fruitList)
print(len(fruitList))
print\

for x in fruitList:
  print(x)

if "apple" in fruitList:
  print("Yes, 'apple' is in the fruits list")
else:
  print("Not available")
  
if "mango" in fruitList:
  print("Yes, 'apple' is in the fruits list")
else:
  print("Not available")
 
if b > a:
  print ("True")
else:
  print ("False")

while i < 6:
  print(i)
  i += 1
 