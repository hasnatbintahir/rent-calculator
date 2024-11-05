rent = int(input("Enter total Rent: "))
total_units = int(input("Enter total electricity units used: "))
unit_price = int(input("Enter per unit price: "))
food = input("Enter amount of food: ")
total_person = int(input("Total persons living: "))
a = True


def filtering(n):
    n = n.strip("")
    if n.isdigit():
        return True
    return False




if("," in food):
    food = food.replace(" ", "").split(",")
    food_filtering = filter(filtering, food)
    food = list(food_filtering)
    food = [int(i) for i in food]
    food = sum(food)

        
else:
    food = int(food)

    
total = (rent + (total_units*unit_price) + food)
    
per_person = (rent + (total_units*unit_price) + food)//total_person

print(f"Total amount is {total} and amount divide in {total_person} is {per_person}")


 