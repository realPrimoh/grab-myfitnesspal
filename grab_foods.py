import myfitnesspal
import time
import pickle
import csv
client = myfitnesspal.Client()
print("Got client")
print("Opening foods_searched and loading...")
infile = open("foods_searched",'rb')
foods_searched=set(['apple', "mango", "watermelon"])
print("infile", infile)
print("foods_searched", foods_searched)
infile.close()
print("Got foods_searched")
print(foods_searched)
foods_to_search = ["blueberries", "banana", "orange", "pear", ]
print("Searching foods...")
searched = 0
csvfile = open('foods.csv', 'a',)
writer = csv.writer(csvfile)
writer.writerow([
    'MFP ID',
    'Name', 
    'Brand',
    'Verified',
    'Serving',
    'Calories',
    'Fat',
    'Carbohydrates',
    'Protein',
    'Fiber',
    'Sugar',
    'Sodium',
    'Calcium',
    'Cholesterol',
    'Iron',
    'Monounsaturated Fat',
    'Polyunsaturated Fat',
    'Potassium',
    'Saturated Fat',
    'Trans Fat',
    'Vitamin A',
    'Vitamin C',
    'Confirmations',
    'Servings',
])
while len(foods_to_search) != 0:
    current_search_item = foods_to_search.pop()
    print("Got", current_search_item)
    if current_search_item not in foods_searched:
        print("Currently searching", current_search_item)
        current_food_items = client.get_food_search_results(current_search_item)
        for i in current_food_items:
            item = client.get_food_item_details(i.mfp_id)
            writer.writerow([
                    item.mfp_id,
                    item.name,
                    item.brand,
                    item.verified,  
                    item.serving,
                    item.calories,
                    item.fat,
                    item.carbohydrates,
                    item.protein,
                    item.fiber,
                    item.sugar,
                    item.sodium,
                    item.calcium,
                    item.cholesterol,
                    item.iron,
                    item.monounsaturated_fat,
                    item.polyunsaturated_fat,
                    item.potassium,
                    item.saturated_fat,
                    item.trans_fat,
                    item.vitamin_a,
                    item.vitamin_c,
                    item.confirmations,
                    item.servings,
                ]) 
        foods_searched.add(current_search_item)
        searched += 1
        if (len(foods_to_search)) != 0:
            print("Sleeping for 35 seconds...")
            time.sleep(35)
    else:
        print("Already searched for this... Moving on")


print("closing foods searched...")
print("Verify this: the length of foods_to_search is now", len(foods_to_search))
print("All foods_searched ever...")
print(foods_searched)
print("Foods Searched this session:", searched)
print("Dumping all foods_searched to file...")
outfile = open("foods_searched", 'wb')
pickle.dump(foods_searched,outfile)
outfile.close()
print("Successfully dumped. Closing program now")
