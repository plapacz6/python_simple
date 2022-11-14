import pprint
inventory = {
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12
        }

def displayInventory(inv):
  print("INWENTARZ GRACZA:")
  for article, quantity in inv.items():
    print("{", article, "}: ", quantity, " sztuk")

pprint.pprint(pprint.pformat(inventory))
pprint.pprint(inventory)
displayInventory(inventory)

exit()
    
