import myfitnesspal
import time
import pickle
import csv
client = myfitnesspal.Client()
print("Got client")
print("Opening foods_searched and loading...")
infile = open("foods_searched",'rb')
# foods_searched=set(['apple', "mango", "watermelon", "banana", "orange", "pear", "blueberries", "chobani", "chobani yogurt", "greek yogurt", 
# "spaghetti", "bread", "fiber bread", "bagel", "thomas bagel", "chicken tenderloin", "chicken breast", "chicken", "oat milk",  "whole milk", "starbucks",
# "olive garden", "mcdonalds", "taco bell", "chipotle", "black bear diner", "ihop", "dennys", "kirkland milk", "milk", "skim milk", "almond milk",
# "whey protein", "optimum nutrition protein powder", "mini wheat cereal", "oatmeal squares", "special k cereal", "gr8nola", "latte", "mocha", "ferrero rocher", "milano", "pork sausage", "chicken sausage", "beef brisket", "pork belly",
# "egg", "ice cream", "halo top", "carrots", "broccoli", "kbbq", "butter chicken", "roti", "naan", "rice", "basmati rice", "jasmine rice", "cheerios", "chocolate cheerios", "cocoa puffs", "fruit loops", "kit kat", "snickers", "jalapeno chips", "doritos", "cheetos", "hot cheetos", "pringles", "coffee", "haagen-dazs", "pizza", "little caesars", "dominos", "pizza hut", "chicken pizza", "hawaiian pizza", "panang curry", "red curry", "green curry", "buffalo wild wings", "wingstop", "kirkland chicken tenderloin", "chicken nuggets", "breaded chicken", "costco muffin", "strawberries",
# ["chicken wing", "turkey breast", "sliced turkey", "oven roasted turkey", "nutrigrain bar", "clif bar", "clif bar protein", "quest bar", "quest cookie", "lays", "takis", "thai iced tea", "mango lassi", "boba tea", "tea", "pesto chicken sandwich", "pesto pasta", "alfredo pasta", "marinara pasta", "chicken tikka", "bbq chicken", "protein pancakes",
# ])
foods_searched = set()
print("infile", infile)
print("foods_searched", foods_searched)
infile.close()
print("Got foods_searched")
print(foods_searched)
# pasta throws error currently
foods_to_search = ['apple']
print("Searching foods...")
searched = 0
csvfile = open('new_foods.csv', 'a',)
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
            try:
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
            except Exception as e:
                print("ERROR:", e)
                print(i)
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
