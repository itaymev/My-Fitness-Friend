# calorie-tracker intructions for use
Place all files in the repository in a single directory. Python version 3.12 must be installed. The following packages for Python 3.12 must be installed aswell: tkinter, matplotlib, numpy, datetime, os, csv. Next, please edit the PRELOADED_FILE_PATH and TRACK_FILE_PATH global variables in main.py to match your relative path. And ensure the same for CSV_FILE_PATH in food_class.py, though it should just be a difference of directory name. Compile main.py with "python3.12 main.py" in a terminal and you will be prompted with the main menu.

- Step 1: Create a profile, entering a username and password (both are case sensitive).
- Step 2: Once your profile is created, the textbox in the main menu will confirm the profile, and you are ready to log in.
- Step 3: Your current macronutrient and calorie goals will all be set to 0, as you are a new user. Go ahead and set some goals and click "Update Progress/Set Goals" which will update the pie charts in the progress tab. You may track foods by selecting the "Load Recorded Foods" button and double-clicking your desired food, then clicking the "Add Food" button.
- Step 4: After you've tracked some foods you may click the "Track Today's Intake" button. If you alreayd hit "Track Today's Intake" bu then end up tracking more food, there is no issue, as the program will seek entries with the same dates and overwrite the entry. Tracking via this feature allows the program to remember your goals for tomorrow.
- Step 5: You can also add your own custom meals or foods by simply entering the name, calories, macronutrients, and serving size into the textboxes then clicking the "Save Food to Records".


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
