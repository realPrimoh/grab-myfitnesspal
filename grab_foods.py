import myfitnesspal
import time
import pickle
client = myfitnesspal.Client('YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE')
print("Got client")
print("Opening foods_searched and loading...")
infile = open("foods_searched",'rb')
foods_searched = pickle.load(infile)
infile.close()
print("Got foods_searched")
print(foods_searched)
foods_to_search = ['PUT_FOODS_HERE', 'FOOD1', 'FOOD2']
print("Searching foods...")
searched = 0
while len(foods_to_search) != 0:
    current_search_item = foods_to_search.pop()
    print("Got", current_search_item)
    if current_search_item not in foods_searched:
        print("Currently searching", current_search_item)
        client.get_food_search_results(current_search_item)
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


