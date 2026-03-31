#create the dictionary
grocery_inventory = {"Milk":("Dairy",3.50,8),
"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),
"Apples":("Produce",1.50,50)}
#check and update Price
if grocery_inventory["Eggs"][1]>5:
    print("Eggs are too expensive, reducing the price by $1.")
    category,price,quanity = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"]= (category,price- 1, quanity)
    print(grocery_inventory)
else:    
    print("The price of Eggs is reasonable.")
#Add a new item
grocery_inventory.update({"Tomatoes": ("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)
#Manage stock
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    category,price,quanity = grocery_inventory["Milk"]
    grocery_inventory["Milk"] =(category,price,quanity+20)
else:
    print("Milk has sufficient stock. Increasing stock by 20 units.")
if grocery_inventory["Apples"][1] > 2.00:
    grocery_inventory.pop("Apples")
print("Updated inventory:",grocery_inventory)