menu=['Americano', 'Croissant', 'Hot chocolate', 'Breakfast sandwich'] #Items in menu list

stock = {menu[0]:100,  #stocks for each item
         menu[1]: 150,
         menu[2]:87,
         menu[3]:50}

price={menu[0]: 3.75,   #Inflation prices per item (£) are no joke
       menu[1]: 2.50,   
       menu[2]: 4.50,
       menu[3]: 5.00}

final_stock_worth = 0
for items in menu:     #items are the items in the menu
    final_stock_worth += stock[items]*price[items] #setting the items as keys for values in price and stock
    
print(final_stock_worth) # choose between coffee or a house