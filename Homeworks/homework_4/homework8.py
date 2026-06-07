shopping = []

for i in range(3):
    product = input("Что вы хотите покупать: ")
    shopping.append(product)


for shop in shopping:
    print(f"Вы покупали: {shop}")

print(f"Ваш список покупки: {shopping}")