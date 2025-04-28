import csv

# List of dishes with their ingredients and ingredient types
dishes = [
    ("Feijoada", ["black beans", "pork", "beef", "rice", "farofa", "collard greens", "orange"], ["protein", "protein", "protein", "carbohydrate", "carbohydrate", "vegetable", "fruit"]),
    ("Moqueca", ["fish", "shrimp", "coconut milk", "dende oil", "tomato", "onion", "bell pepper", "cilantro"], ["protein", "protein", "fat", "fat", "vegetable", "vegetable", "vegetable", "vegetable"]),
    ("Pão de Queijo", ["tapioca flour", "cheese", "milk", "egg", "butter"], ["carbohydrate", "dairy", "dairy", "protein", "fat"]),
    ("Brigadeiro", ["condensed milk", "cocoa powder", "butter", "chocolate sprinkles"], ["dairy", "others", "fat", "others"]),
    ("Acarajé", ["black-eyed peas", "onion", "shrimp", "dende oil"], ["protein", "vegetable", "protein", "fat"]),
    ("Vatapá", ["bread", "shrimp", "peanuts", "coconut milk", "dende oil"], ["carbohydrate", "protein", "fat", "fat", "fat"]),
    ("Coxinha", ["chicken", "flour", "potato", "cream cheese"], ["protein", "carbohydrate", "carbohydrate", "dairy"]),
    ("Pastel", ["flour", "ground beef", "cheese", "heart of palm"], ["carbohydrate", "protein", "dairy", "vegetable"]),
    ("Baião de Dois", ["rice", "beans", "cheese", "sun-dried meat"], ["carbohydrate", "protein", "dairy", "protein"]),
    ("Churrasco", ["beef", "pork", "chicken", "sausage"], ["protein", "protein", "protein", "protein"]),
    ("Farofa", ["cassava flour", "bacon", "onion", "egg", "butter"], ["carbohydrate", "protein", "vegetable", "protein", "fat"]),
    ("Tapioca", ["tapioca starch", "butter", "cheese", "coconut"], ["carbohydrate", "fat", "dairy", "fruit"]),
    ("Arroz Carreteiro", ["rice", "beef jerky", "onion", "garlic", "tomato"], ["carbohydrate", "protein", "vegetable", "vegetable", "vegetable"]),
    ("Bolinho de Chuva", ["flour", "sugar", "milk", "egg", "cinnamon"], ["carbohydrate", "carbohydrate", "dairy", "protein", "condiment"]),
    ("Empadão", ["flour", "chicken", "cheese", "heart of palm"], ["carbohydrate", "protein", "dairy", "vegetable"]),
    ("Bolo de Rolo", ["flour", "sugar", "butter", "guava paste"], ["carbohydrate", "carbohydrate", "fat", "fruit"]),
    ("Caruru", ["okra", "shrimp", "peanuts", "dende oil"], ["vegetable", "protein", "fat", "fat"]),
    ("Quibebe", ["pumpkin", "onion", "garlic", "butter"], ["vegetable", "vegetable", "vegetable", "fat"]),
    ("Canjica", ["white corn", "milk", "coconut milk", "peanuts", "sugar"], ["carbohydrate", "dairy", "fat", "fat", "carbohydrate"]),
    ("Pamonha", ["corn", "milk", "sugar", "cheese"], ["carbohydrate", "dairy", "carbohydrate", "dairy"]),
    ("Curau", ["corn", "milk", "sugar", "cinnamon"], ["carbohydrate", "dairy", "carbohydrate", "condiment"]),
    ("Tutu de Feijão", ["beans", "flour", "garlic", "onion", "bacon"], ["protein", "carbohydrate", "vegetable", "vegetable", "protein"]),
    ("Maniçoba", ["manioc leaves", "pork", "beef", "bacon"], ["vegetable", "protein", "protein", "protein"]),
    ("Caldo Verde", ["potato", "collard greens", "sausage", "onion"], ["carbohydrate", "vegetable", "protein", "vegetable"]),
    ("Frango com Quiabo", ["chicken", "okra", "onion", "garlic"], ["protein", "vegetable", "vegetable", "vegetable"]),
    ("Rabada", ["oxtail", "potato", "carrot", "collard greens"], ["protein", "carbohydrate", "vegetable", "vegetable"]),
    ("Dobradinha", ["tripe", "beans", "carrot", "potato"], ["protein", "protein", "vegetable", "carbohydrate"]),
    ("Cuscuz Paulista", ["cornmeal", "sardines", "egg", "peas", "tomato"], ["carbohydrate", "protein", "protein", "vegetable", "vegetable"]),
    ("Escondidinho", ["cassava", "ground beef", "cheese"], ["carbohydrate", "protein", "dairy"]),
    ("Peixada", ["fish", "potato", "tomato", "onion"], ["protein", "carbohydrate", "vegetable", "vegetable"]),
    ("Camarão na Moranga", ["shrimp", "pumpkin", "cream cheese"], ["protein", "vegetable", "dairy"]),
    ("Sururu", ["shellfish", "coconut milk", "dende oil"], ["protein", "fat", "fat"]),
    ("Buchada de Bode", ["goat stomach", "blood", "onion", "garlic"], ["protein", "protein", "vegetable", "vegetable"]),
    ("Arroz Doce", ["rice", "milk", "sugar", "cinnamon"], ["carbohydrate", "dairy", "carbohydrate", "condiment"]),
    ("Beiju", ["tapioca starch", "butter", "cheese"], ["carbohydrate", "fat", "dairy"]),
    ("Salpicão", ["chicken", "mayonnaise", "carrot", "peas", "corn"], ["protein", "fat", "vegetable", "vegetable", "carbohydrate"]),
    ("Galinhada", ["rice", "chicken", "peppers", "onion"], ["carbohydrate", "protein", "vegetable", "vegetable"]),
    ("Pato no Tucupi", ["duck", "cassava sauce", "jambu leaves"], ["protein", "others", "vegetable"]),
    ("Tacacá", ["shrimp", "jambu", "tucupi"], ["protein", "vegetable", "others"]),
    ("Pirarucu de Casaca", ["fish", "cassava flour", "banana", "onion"], ["protein", "carbohydrate", "fruit", "vegetable"]),
    ("Torresmo", ["pork skin", "salt"], ["fat", "condiment"]),
    ("Pipoca", ["corn", "butter", "salt"], ["carbohydrate", "fat", "condiment"]),
    ("Romeu e Julieta", ["guava paste", "cheese"], ["fruit", "dairy"]),
    ("Queijadinha", ["cheese", "coconut", "milk", "sugar"], ["dairy", "fruit", "dairy", "carbohydrate"]),
    ("Paçoca", ["peanuts", "sugar", "cassava flour"], ["fat", "carbohydrate", "carbohydrate"]),
    ("Pé-de-moleque", ["peanuts", "sugar"], ["fat", "carbohydrate"]),
    ("Bolo de Milho", ["corn", "flour", "sugar", "milk"], ["carbohydrate", "carbohydrate", "carbohydrate", "dairy"]),
    ("Mingau de Milho", ["cornmeal", "milk", "sugar", "cinnamon"], ["carbohydrate", "dairy", "carbohydrate", "condiment"]),
    ("Feijão Tropeiro", ["beans", "bacon", "sausage", "collard greens", "egg", "cassava flour"], ["protein", "protein", "protein", "vegetable", "protein", "carbohydrate"]),
    ("Bobó de Camarão", ["shrimp", "cassava", "coconut milk", "dende oil", "tomato", "onion"], ["protein", "carbohydrate", "fat", "fat", "vegetable", "vegetable"])
]

# Open CSV file
with open('brazilian_dishes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["dish_name", "ingredients", "ingredient_type"])
    for dish_name, ingredients, ingredient_types in dishes:
        writer.writerow([
            dish_name,
            ",".join(ingredients),
            ",".join(ingredient_types)
        ])