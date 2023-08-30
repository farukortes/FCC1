# Dummy code 
#Error= too many inputs
list=["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","523 - 49","523 - 49"]
p=len(list)
print("The length of list is:",p)

# Check if too many inputs are available
if p>5:
    print("Error: Too many problems.")
    exit()
else:
    print("Go on, the number of items is less than 5")
    
print("It works man!")