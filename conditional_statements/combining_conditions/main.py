discounted = True
low_in_stock = True
movingProduct = discounted or low_in_stock
promotion = (not discounted) and (not low_in_stock)
print("is the item eligible for promotion?",promotion)
     