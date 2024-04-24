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


class MicroNutrients():
    def __init__(self, iron: float, zinc: float, calcium: float, 
                 magnesium: float, potassium: float, vitaminA: float, 
                 vitaminB12: float, vitaminC: float, vitaminD: float, 
                 omega3: float, omega6: float, cholesterol: float, sodium: float) -> None:
        self.iron = iron
        self.zinc = zinc
        self.calcium = calcium
        self.magnesium = magnesium
        self.potassium = potassium
        self.vitaminA = vitaminA
        self.vitaminB12 = vitaminB12
        self.vitaminC = vitaminC
        self.vitaminD = vitaminD
        self.omega3 = omega3
        self.omega6 = omega6
        self.cholesterol = cholesterol
        self.sodium = sodium


    def __str__(self) -> str:
        return str((self.iron, self.zinc, self.calcium, self.magnesium, self.vitaminA, self.vitaminB12, self.vitaminC, self.vitaminD, self.omega3))
    

class Food():
    def __init__(self, name: str, cals: float, grams: float, protein: float, carb: Carbs, fat: Fats, 
                 micro: MicroNutrients = MicroNutrients(0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)) -> None:
        """
        name - (str): food label, should contain brand and item name ("Tillamook, Cream Cheese")
        cals - (int): kilocalories on food label per 1 serving
        prot - (float): grams of protein on food label per 1 serving
        carb - (float): grams of carbohydrates on food label per 1 serving
        fat - (float): grams of fats on food label per 1 serving
        grams - (float): amount of grams in 1 serving
        """
        self.name = name
        self.cals = cals
        self.grams = grams
        self.prot = protein
        self.carb = carb
        self.fat = fat
        self.micro = micro

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

    new_row = [food.cals, food.grams, food.name, food.prot, 
               food.carb.total, food.carb.fiber, food.carb.sugars, food.carb.added_sugars, 
               food.fat.total, food.fat.sat, food.fat.trans, food.fat.poly, food.fat.mono,
               food.micro.iron, food.micro.zinc, food.micro.calcium, food.micro.magnesium, 
               food.micro.potassium, food.micro.vitaminA, food.micro.vitaminB12, food.micro.vitaminC, 
               food.micro.vitaminD, food.micro.omega3, food.micro.omega6, food.micro.cholesterol, food.micro.sodium]

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

# name,Calories,Serving Weight 1 (g),Protein (g),Carbohydrate (g),Fiber (g),Sugars (g),Added Sugar (g),Fat (g),Saturated Fats (g),
# Trans Fatty Acids (g),"Fatty acids, total polyunsaturated (mg)","Fatty acids, total monounsaturated (mg)",
# "Iron, Fe (mg)","Zinc, Zn (mg)",Calcium (mg),Magnesium (mg),"Potassium, K (mg)","Vitamin A, RAE (mcg)",Vitamin B-12 (mcg),
# Vitamin C (mg),Vitamin D (mcg),Omega 3s (mg),Omega 6s (mg),Cholesterol (mg),Sodium (mg)
        for i in read_ob:
            food = Food(i[0], float(i[1]), float(i[2]), float(i[3]), 
                        Carbs(float(i[4]), float(i[5]), float(i[6]), float(i[7])), 
                        Fats(float(i[8]), float(i[9]), float(i[10]), float(i[11]), float(i[12])),
                        MicroNutrients(float(i[13]),float(i[14]),float(i[15]),float(i[16]),float(i[17]),
                                       float(i[18]),float(i[19]),float(i[20]),float(i[21]),float(i[22]),
                                       float(i[23]),float(i[24]),float(i[25]))) #............wow
            loaded_foods.append(food)

        return loaded_foods

def t():
    # This is a test.
    # record_preloaded_food(Food("Daisy Cottage Cheese", 90, 13, Carbs(5, 0, 4, 0), Fats(2, 1.5, 0, 0), 113), CSV_FILE_PATH)

    # new_food = load_preloaded_foods(CSV_FILE_PATH)
    # print(new_food[0])
    pass


#t()
