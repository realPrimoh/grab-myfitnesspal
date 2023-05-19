import myfitnesspal
from supabase import create_client, Client
import json
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

supabase: Client = create_client(os.environ.get("url"), os.environ.get("key"))


client = myfitnesspal.Client()

local_arr = []
local_arr += [
    "rice",
    "pasta",
    "bread",
    "potatoes",
    "meat",
    "fish",
    "eggs",
    "dairy",
    "fruits",
    "vegetables",
    "tofu",
    "beans",
    "nuts",
    "seeds",
    "honey",
    "sugar",
    "oil",
    "butter",
    "salt",
    "pepper",
    "garlic",
    "onions",
    "herbs",
    "spices",
    "coffee",
    "tea",
    "water",
    "soda",
    "juice",
    "alcohol",
    "chocolate",
    "ice cream",
    "cookies",
    "cakes",
    "pizza",
    "hamburgers",
    "fries",
    "hot dogs",
    "sandwiches",
    "salads",
    "soups",
    "beverages",
    "desserts",
]
local_arr += [
    "cereal",
    "milk",
    "kirkland",
    "costco",
    "chicken bake",
    "oatmeal squares",
    "cashews",
    "coffee",
    "costco muffin",
    "whey protein",
    "optimum nutrition protein",
    "fairlife protein",
    "chilis",
    "panera",
    "pinkberry",
    "gong cha",
    "whataburger",
    "the habit",
    "five guys",
    "pf changs",
]
local_arr += [
    "fairlife protein shake",
    "steak",
    "chicken",
    "chicken tenderloin",
    "mcdonalds",
    "muscle milk",
    "chobani",
    "in n out",
    "panda express",
    "subway",
    "taco bell",
    "burger king",
    "wendys",
    "KFC",
    "Dominos",
    "papa johns",
    "little caesars",
    "pizza hut",
    "dairy queen",
    "arbys",
    "starbucks",
    "dunkin",
    "chipotle",
    "pork",
    "carnitas",
    "thai",
    "shrimp",
    "panang curry",
    "olive garden",
    "taro",
    "boba",
    "thai iced tea",
    "jamba juice",
    "donuts",
    "Krispy kreme",
    "baja fresh",
    "lays",
    "doritos",
    "miss vickies",
    "goldfish",
    "cheetos",
    "takis",
    "turkey",
    "salmon",
    "tuna",
    "tilapia",
    "breaded tilapia",
    "quinoa",
    "brown rice",
    "protein bar",
    "clif bar",
    "cheese",
    "haagen dazs",
    "halo top",
    "oats",
    "cocoa puffs",
    "special k",
    "peanut butter",
    "nutella",
    "almond butter",
    "ferrero rocher",
    "trader joes",
    "buffalo wild wings",
    "chicken melt",
    "ramen",
    "maggi noodles",
    "potstickers",
    "chicken nuggets",
    "panko breaded chicken",
    "drumsticks",
    "ben and jerrys",
    "coldstone",
    "baskin robbins",
    "gyro",
    "egg tart",
    "fruit snacks",
    "vitamin water",
    "hint water",
    "sea bass",
    "alligator",
    "lamb",
    "shark",
    "lobster",
    "crab",
    "carrots",
    "broccoli",
    "lettuce",
    "kale",
    "almonds",
    "peanuts",
    "chocolate milk",
    "korean barbeque",
    "pork belly",
    "steak",
    "beef",
    "brisket",
    "ribs",
    "short ribs",
    "burger",
    "cheeseburger",
    "chicken sandwich",
    "taco shells",
    "tortilla",
    "roti",
    "butter chicken",
    "naan",
    "basmati rice",
    "tandoori chicken",
    "chicken tikka masala",
    "mango sticky rice",
    "ice cream cone",
    "bibigo potstickers",
    "breaded tilapia",
]
local_set = set(local_arr)
search_q = []

for searchable in search_q:
    if searchable in local_set:
        continue
    food_items = client.get_food_search_results(searchable)
    for i in food_items:
        try:
            item = client.get_food_item_details(i.mfp_id)
            print("______________________________")
            print("______________________________")
            print("______________________________")
            print("Processing new item:", item)
            food_dict = {
                "id": item.mfp_id,
                "Name": item.name,
                "Brand": item.brand,
                "Verified": item.verified,
                "Serving": item.serving,
                "Calories": item.calories,
                "Fat": item.fat,
                "Carbohydrates": item.carbohydrates,
                "Protein": item.protein,
                "Fiber": item.fiber,
                "Sugar": item.sugar,
                "Sodium": item.sodium,
                "Calcium": item.calcium,
                "Cholesterol": item.cholesterol,
                "Iron": item.iron,
                "Monounsaturated Fat": item.monounsaturated_fat,
                "Polyunsaturated Fat": item.polyunsaturated_fat,
                "Potassium": item.potassium,
                "Saturated Fat": item.saturated_fat,
                "Trans Fat": item.trans_fat,
                "Vitamin A": item.vitamin_a,
                "Vitamin C": item.vitamin_c,
                "Confirmations": item.confirmations,
                "Servings": json.dumps([s.dictify() for s in item.servings]),
            }
            print(food_dict)
            # serving_items = []
            # for serving in item.servings:
            #     curr_serving = {}
            #     curr_serving['id'] = int(serving._serving_id)
            #     curr_serving['nutrition_multiplier'] = serving.nutrition_multiplier
            #     curr_serving['value'] = serving.value
            #     curr_serving['unit'] = serving.unit
            #     curr_serving['index'] = serving.index
            #     try:
            #         data, count = supabase.table('servings').insert(curr_serving).execute()
            #         print('data', data)
            #         if 'data' in data:

            #             serving_items.append(data.data[0])
            #             print("Got inserted serving_items data:", data.data[0])
            #             print("Data type:", type(data))
            #             print("Serving successfully inserted", str(serving))
            #         else:
            #             print('DATA ERROR!!!:', data)
            #             break
            #     except Exception as e:
            #         print("Supabase Serving addition error:", e)
            #         print('failed on serving:', curr_serving)
            #         if (hasattr(e, 'code') and e.__getattribute__('code') == '23505'):
            #             response = supabase.table('servings').select('id', 'uuid').eq('id', serving._serving_id).execute()
            #             print("Duplicate serving successfully received", serving)
            #             serving_items.append(response.data[0])
            # print(serving_items)
            # print(str(item.servings))
            # print("Serving match:", len(serving_items) == len(item.servings))
            # if (len(serving_items) == len(item.servings)):
            #     print("Serving match SUCCESS!")
            # food_dict["linked_servings"] = [s["uuid"] for s in serving_items]
            try:
                data, count = supabase.table("foods").insert(food_dict).execute()
                print("------")
                print("Successfully added:", item)
                print("------")
            except Exception as e:
                print("Food addition error:", e)
                if e.__getattribute__("code") == "23505":
                    print("Duplicate Food addition error:", e)
        except Exception as e:
            print("PROGRAM ERROR:", e)
            print("Current food item failed on item:", item)
            print("Current food item failed on food_dict:", food_dict)
            break
# data, count = supabase.table('foods').insert({"id": 1, "name": "Denmark"}).execute()
# print(food_items)
