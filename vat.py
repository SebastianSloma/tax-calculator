tax = 21
calculated_tax = (1 + tax / 100)

netto_price_apple = 12
netto_price_peach = 15
netto_price_banana = 20
netto_price_orange = 23
netto_price_citron = 17

brutto_price_apple = netto_price_apple * calculated_tax
brutto_price_peach = netto_price_peach * calculated_tax
brutto_price_banana = netto_price_banana * calculated_tax
brutto_price_orange = netto_price_orange * calculated_tax
brutto_price_citron = netto_price_citron * calculated_tax

print(brutto_price_apple)
print(brutto_price_peach)
print(brutto_price_banana)
print(brutto_price_orange)
print(brutto_price_citron)