# Food classes definitions
import csv

CSV_FILE_PATH = "cal:macro track/preloaded.csv"

class Fats():
    def __init__(self, total: float, saturated: float, trans: float, polyunsat: float = 0.0, monounsat: float = 0.0) -> None:
        """
        total - (float): total grams of fats on food label per 1 serving
        saturated - (float): grams of saturated fats on food label per 1 serving
        trans - (float): grams of trans fats on food label per 1 serving
        polyunsat - (float): grams of trans fats on food label per 1 serving, some food labels do not denote this
        monounsat - (float): grams of trans fats on food label per 1 serving, some food labels do not denote this
        """
        self.total = total
        self.sat = saturated
        self.trans = trans
        self.poly = polyunsat
        self.mono = monounsat

    def __str__(self) -> str:
        return str((self.total, self.sat, self.trans, self.poly, self.mono))

class Carbs():
    def __init__(self, total: float, fiber: float, sugars: float, added_sugars: float) -> None:
        """
        total - (float): total grams of carbohydrates per 1serving
        fiber - (float): grams of dietary fiber per 1 serving
        sugars - (float): grams of total sugars per 1 serving
        added_sugars - (float): grams of added sugars per 1 serving
        """
        self.total = total
        self.fiber = fiber
        self.sugars = sugars
        self.added_sugars = added_sugars

    def __str__(self) -> str:
        return str((self.total, self.fiber, self.sugars, self.added_sugars))

class Food():
    def __init__(self, name: str, cals: int , protein: float, carb: Carbs, fat: Fats, grams: float) -> None:
        """
        name - (str): food label, should contain brand and item name ("Tillamook, Cream Cheese")
        cals - (int): kilocalories on food label per 1 serving
        prot - (float): grams of protein on food label per 1 serving
        carb - (float): grams of carbohydrates on food label per 1 serving
        fat - (float): grams of fats on food label per 1 serving
        grams - (float): amount of grams in 1 serving
        """
        self.cals = cals
        self.grams = grams
        self.name = name
        self.prot = protein
        self.carb = carb
        self.fat = fat

    def __str__(self) -> str:
        return str((self.name, self.cals, self.grams, self.prot, str(self.carb), str(self.fat)))
    
    def display_simple(self) -> str:
        # alternative display for str of Food class
        return str(self.grams) + " grams of " + str(self.name) + " with " + str(self.prot) + " grams of protein, " + str(self.carb.total) + " grams of carbs, and " + str(self.fat.total) + " grams of fat."

def record_preloaded_food(food: Food, csvf: str) -> None:
    with open(csvf, "r") as f:  # Open the file in read mode to check for duplicates
        rows = list(csv.reader(f))
        
        existing = []
        for i in rows:
            existing.append(i[2])

    new_row = [food.cals, food.grams, food.name, food.prot, food.carb.total, food.carb.fiber, food.carb.sugars, food.carb.added_sugars, food.fat.total, food.fat.sat, food.fat.trans, food.fat.poly, food.fat.mono]

    if new_row[2] not in existing:  # Check if the row already exists
        with open(csvf, "a") as f:  # Open the file in append mode
            writer = csv.writer(f)
            writer.writerow(new_row)
    else:
        print("duplicate item")
        pass


def load_preloaded_foods(csvf) -> list[Food]:
    with open(csvf, "r") as f:
        read_ob = csv.reader(f)
        loaded_foods = []

        for i in read_ob:
            food = Food(i[2], i[0], i[3], Carbs(i[4], i[5], i[6], i[7]), Fats(i[8], i[9], i[10], i[11], i[12]), i[1]) # Why did I not make the formatting all the same................
            loaded_foods.append(food)

        return loaded_foods

def t():
    # This is a test.
    record_preloaded_food(Food("Daisy Cottage Cheese", 90, 13, Carbs(5, 0, 4, 0), Fats(2, 1.5, 0, 0), 113), CSV_FILE_PATH)

    new_food = load_preloaded_foods(CSV_FILE_PATH)
    print(new_food[0])

# t()