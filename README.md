

MyFitnessPal Food Database Scraper
============

MyFitnessPal has a private API, which makes it hard to grab data from their databases.

Installation
------------

    git clone https://github.com/realPrimoh/myfitnesspal-scraper.git
    cd myfitnesspal-scraper
    python setup.py install


Authentication
--------------
To make searches, you must put your username and password in. Your username and password will go into "grab_foods.py".


Food Search Examples
--------------------

To search for items:

```python
import myfitnesspal

client = myfitnesspal.Client('my_username')

food_items = client.get_food_search_results("bacon cheeseburger")
food_items
# >> [<Bacon Cheeseburger -- Sodexo Campus>,
# <Junior Bacon Cheeseburger -- Wendy's>,
# <Bacon Cheeseburger -- Continental Café>,
# <Bacon Cheddar Cheeseburger -- Applebees>,
# <Bacon Cheeseburger - Plain -- Homemade>,
# <Jr. Bacon Cheeseburger -- Wendys>,
# ...

print("{} ({}), {}, cals={}, mfp_id={}".format(
    food_items[0].name,
    food_items[0].brand,
    food_items[0].serving,
    food_items[0].calories,
    food_items[0].mfp_id
))
# > Bacon Cheeseburger (Sodexo Campus), 1 Sandwich, cals = 420.0
```

To get details for a particular food:
```python
import myfitnesspal

client = myfitnesspal.Client('my_username')

item = client.get_food_item_details("89755756637885")
item.servings
# > [<1.00 x Sandwich>]
item.saturated_fat
# > 10.0
```

Saving Foods to a File
--------------------

To add foods searched into a CSV file that you can browse/import/etc:

Open 'grab_foods.py' and in the foods_to_search list, put foods you want to add.

Example:
```foods_to_search = ["chicken breast", "eggs", "bananas"]```

```python grab_foods.py```


This drops every food item found through MyFitnessPal's search into foods.csv. An example is shown in sampleoutput.csv.

To make sure there is no overloading of the server, there is a 35-second waiting period between each search.

Furthermore, I have implemented a cache to make sure there is no time wasted on repeating searches and also adding duplicate foods. Food IDs and food searches are stored in HashSets, and to make sure these persist over time, I pickle and un-pickle the set at appropriate times when the script runs.

Cleaning Previous Searches
--------------------
There may come a point where you want to clean your searches or clear the cache. In this case, just run:

```python clean.py```


NOTE: Some of this code is borrowed from [coddingtonbear's general repo.]https://github.com/coddingtonbear/python-myfitnesspal/. 

I have modified his code (which is now not maintained) to work again, along with saving items to CSV files. I chose CSV because Python works well with CSV and most programs can import CSV files easily.

Big credit to him for tests and scraper setup! 
