#dictionaries
clothes = { "t-shirt": "blue", "hat": "red", "jeans": "black", "shoes": "purple"}
print(clothes["t-shirt"])

# can you please explain how to use the get() method? we had a go ... getatt(clothes["hat"])
x = clothes.get("hat")
print(x)

#pop an item from the dictionary
clothes.pop("jeans")
print(clothes)

#add new items to the dictionary - because you change the data
clothes.update({"trousers": "white", "stockings": "brown"})
print(clothes)

# how are boolean values similar to if statements?
if "trousers" in clothes:
    print("Trousers is there!")

if "jeans" not in clothes:
    print("Jeans have been removed")

#the below code doesn't work because we haven't accessed the values - we just used the keys
cars = {"red cars": "2", "blue cars": "3", "white cars": "7", "purple cars": "7"}
if "white cars" == "purple cars" in cars:
    print("These are the same")