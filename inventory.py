inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

stock_list = inventory.copy() #faz uma cópia do dicionário "inventory"

new_item = {'cookie': 18}

stock_list.update(new_item)

stock_list.pop('cake')

print(stock_list)

