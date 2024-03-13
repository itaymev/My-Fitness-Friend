# calorie-tracker
A simple python application for tracking calories and macronutrients.

# main.py
The main driver of the program, contains class definitions for application windows and function for application utility.
Current Features:
- Adding foods to macronutrient tracker
- One button clear food entries
- Load foods that have been previously saved
- Save foods to load in the future
- Pie chart visual representation

# food_class.py
A file containing definitions for python classes that are used throughout the application.

# Food (class):
        self.cals (int) - Calories per serving in food
        self.grams (float) - Grams per serving in food (sometimes this will be in mL for liquid foods)
        self.name (str) - Name of food and brand
        self.prot (float) - Grams of protein per serving in food
        self.carb (Carbs) - Grams of carbs per serving in food, broken down to total carbs, fiber, total sugars and added sugars
        self.fat (Fats) - Grams of fats per serving in food, broken down to total fats, saturated fats, trans fats, polyunsaturated fats and monounsaturated fats

# Carbs (class):
        self.total (float) - Total grams of carbs per serving in food
        self.fiber (float) - Grams of fiber per serving in food
        self.sugars (float) - Total grams of sugar per serving in food
        self.added_sugars (float) - Grams of added sugar per serving in food

# Fats (class):
        self.total (float) - Total grams of fats per serving in food
        self.sat (float) - Grams of saturated fats per serving in food
        self.trans (float) - Grams of trans fats per serving in food
        self.poly (float) - Grams of polyunsaturated fats per serving in food
        self.mono (float) - Grams of monounsaturated fats per serving in food

# preloaded.csv
A csv file containing "preloaded" foods, by row. This file is directly edited and read by the main.py and food_class.py files. This enables features such as loading foods into the food app which is a massibe quality of life shortcut for the user.

# track.csv
A csv file which will contain the users daily intake data. This will continuously get updated as the user created more inputs, and will not create 2 rows for the same day. Eventually this will enable features like weekly progress and more.
