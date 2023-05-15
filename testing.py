import myfitnesspal
client = myfitnesspal.Client()
food_items = client.get_food_search_results("bacon cheeseburger")
print(food_items)