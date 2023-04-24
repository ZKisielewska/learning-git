print("Lista zakupów")
# definiujemy słownik
shopping_dict = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

# używając pętli for iterujemy po słowniku
# nazwy sklepów i produktów powinny być wypisane dużą literą
for shop, product in shopping_dict.items():
    print(f"Idę do {shop.title()} i kupuję tu następujące rzeczy: {str(product).title()}.")

# używając listy składanej obliczamy ilość zakupionych produktów
total_products = sum([len(product) for shop in shopping_dict.values()])
print(f"W sumie kupuję {total_products} produktów.")