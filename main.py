# Imports for tkinter, the main interface
import tkinter as tk
from tkinter import ttk

# Imports for plotting
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd

# Imports for utility features
import csv
import datetime as dt
import os

# Imports for data classes
import food_class as fc

PRELOADED_FILE_PATH = "/Users/itaymevorach/Documents/personal project/cal:macro track/preloaded.csv"
    
class FoodApp:
    def __init__(self, root, macro_intake_app, micro_intake_app, progress_app):
        self.root = root
        self.macro_intake_app = macro_intake_app
        self.micro_intake_app = micro_intake_app
        self.progress_app = progress_app
        self.recorded_foods = []  # Define recorded_foods as an attribute


        self.root.title("Calorie Tracker")
        
        width = 15

        # -- Entry Boxes -- Coloumn 1 --

        ttk.Label(root, text="Serving Size (g/mL):").grid(row=0, column=0, padx=5, pady=5)
        self.serving_size_entry = ttk.Entry(root, width=width)
        self.serving_size_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Food Name, Brand:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(root, width=width)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="Calories (kcal):").grid(row=2, column=0, padx=5, pady=5)
        self.cals_entry = ttk.Entry(root, width=width)
        self.cals_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(root, text="Protein (g):").grid(row=3, column=0, padx=5, pady=5)
        self.protein_entry = ttk.Entry(root, width=width)
        self.protein_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(root, text="Carbohydrates (g):").grid(row=4, column=0, padx=5, pady=5)
        self.carbs_entry = ttk.Entry(root, width=width)
        self.carbs_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(root, text="Fiber (g):").grid(row=5, column=0, padx=5, pady=5)
        self.fiber_entry = ttk.Entry(root, width=width)
        self.fiber_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(root, text="Total Sugars (g):").grid(row=6, column=0, padx=5, pady=5)
        self.sugars_entry = ttk.Entry(root, width=width)
        self.sugars_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(root, text="Added Sugars (g):").grid(row=7, column=0, padx=5, pady=5)
        self.added_sugars_entry = ttk.Entry(root, width=width)
        self.added_sugars_entry.grid(row=7, column=1, padx=5, pady=5)

        ttk.Label(root, text="Total Fats (g):").grid(row=8, column=0, padx=5, pady=5)
        self.total_fats_entry = ttk.Entry(root, width=width)
        self.total_fats_entry.grid(row=8, column=1, padx=5, pady=5)

        ttk.Label(root, text="Saturated Fats (g):").grid(row=9, column=0, padx=5, pady=5)
        self.saturated_fats_entry = ttk.Entry(root, width=width)
        self.saturated_fats_entry.grid(row=9, column=1, padx=5, pady=5)

        ttk.Label(root, text="Trans Fats (g):").grid(row=10, column=0, padx=5, pady=5)
        self.trans_fats_entry = ttk.Entry(root, width=width)
        self.trans_fats_entry.grid(row=10, column=1, padx=5, pady=5)

        ttk.Label(root, text="Polyunsaturated Fats (g):").grid(row=11, column=0, padx=5, pady=5)
        self.polyunsaturated_fats_entry = ttk.Entry(root, width=width)
        self.polyunsaturated_fats_entry.grid(row=11, column=1, padx=5, pady=5)

        ttk.Label(root, text="Monounsaturated Fats (g):").grid(row=12, column=0, padx=5, pady=5)
        self.monounsaturated_fats_entry = ttk.Entry(root, width=width)
        self.monounsaturated_fats_entry.grid(row=12, column=1, padx=5, pady=5)

        # -- Entry Boxes -- Coloumn 2 --
#,
        ttk.Label(root, text="Iron, Fe (mg):").grid(row=0, column=2, padx=5, pady=5)
        self.iron_entry = ttk.Entry(root, width=width)
        self.iron_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(root, text="Zinc, Zn (mg):").grid(row=1, column=2, padx=5, pady=5)
        self.zinc_entry = ttk.Entry(root, width=width)
        self.zinc_entry.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(root, text="Calcium (mg):").grid(row=2, column=2, padx=5, pady=5)
        self.calcium_entry = ttk.Entry(root, width=width)
        self.calcium_entry.grid(row=2, column=3, padx=5, pady=5)

        ttk.Label(root, text="Magnesium (mg):").grid(row=3, column=2, padx=5, pady=5)
        self.magnesium_entry = ttk.Entry(root, width=width)
        self.magnesium_entry.grid(row=3, column=3, padx=5, pady=5)

        ttk.Label(root, text="Potassium, K (mg):").grid(row=4, column=2, padx=5, pady=5)
        self.potassium_entry = ttk.Entry(root, width=width)
        self.potassium_entry.grid(row=4, column=3, padx=5, pady=5)

        ttk.Label(root, text="Vitamin A, RAE (mcg):").grid(row=5, column=2, padx=5, pady=5)
        self.vitA_entry = ttk.Entry(root, width=width)
        self.vitA_entry.grid(row=5, column=3, padx=5, pady=5)

        ttk.Label(root, text="Vitamin B-12 (mcg):").grid(row=6, column=2, padx=5, pady=5)
        self.vitB12_entry = ttk.Entry(root, width=width)
        self.vitB12_entry.grid(row=6, column=3, padx=5, pady=5)

        ttk.Label(root, text="Vitamin C (mg):").grid(row=7, column=2, padx=5, pady=5)
        self.vitC_entry = ttk.Entry(root, width=width)
        self.vitC_entry.grid(row=7, column=3, padx=5, pady=5)

        ttk.Label(root, text="Vitamin D (mcg):").grid(row=8, column=2, padx=5, pady=5)
        self.vitD_entry = ttk.Entry(root, width=width)
        self.vitD_entry.grid(row=8, column=3, padx=5, pady=5)

        ttk.Label(root, text="Omega 3s (mg):").grid(row=9, column=2, padx=5, pady=5)
        self.omega3_entry = ttk.Entry(root, width=width)
        self.omega3_entry.grid(row=9, column=3, padx=5, pady=5)

        ttk.Label(root, text="Omega 6s (mg):").grid(row=10, column=2, padx=5, pady=5)
        self.omega6_entry = ttk.Entry(root, width=width)
        self.omega6_entry.grid(row=10, column=3, padx=5, pady=5)

        ttk.Label(root, text="Cholesterol (mg):").grid(row=11, column=2, padx=5, pady=5)
        self.cholesterol_entry = ttk.Entry(root, width=width)
        self.cholesterol_entry.grid(row=11, column=3, padx=5, pady=5)

        ttk.Label(root, text="Sodium (mg):").grid(row=12, column=2, padx=5, pady=5)
        self.sodium_entry = ttk.Entry(root, width=width)
        self.sodium_entry.grid(row=12, column=3, padx=5, pady=5)

        # -- BUTTONS --

        # Adds foods
        add_button = ttk.Button(root, text="Add Food", width= width, command=self.add_food)
        add_button.grid(row=13, column=0, padx=3, pady=5)

        # Clears text boxes
        clear_button = ttk.Button(root, text="Clear", width= width, command=self.clear_entries)
        clear_button.grid(row=13, column=1, padx=3, pady=5)

        # Opens the recorded foods window (hooray)
        load_recorded_button = ttk.Button(root, text="Load Recorded Food", width= width, command=self.load_recorded_food)
        load_recorded_button.grid(row=13, column=2, padx=0, pady=5)

        # Adjusts Serving Size
        serving_size_button = ttk.Button(root, text="Adjust Serving Size", width= width, command=self.adjust_serving_size)
        serving_size_button.grid(row=13, column=3, padx=3, pady=5)

        # Add a new button to show Daily Macronutrient Progress
        self.show_progress_button = ttk.Button(root, text="Toggle Macronutrient Intake", width= width, command=self.macro_intake_app.toggle_visibility)
        self.show_progress_button.grid(row=14, column=0, padx=3, pady=5)

        # Add a new button to show Daily Micronutrient Progress
        self.show_progress_button = ttk.Button(root, text="Toggle Micronutrient Intake", width= width, command=self.micro_intake_app.toggle_visibility)
        self.show_progress_button.grid(row=14, column=1, padx=3, pady=5)

        self.track_intake_button = ttk.Button(root, text="Track Today's Intake", width= width, command=self.track_intake)
        self.track_intake_button.grid(row=14, column=2, padx=3, pady=5)

       

    def track_intake(self):
        # Forward the command over
        self.macro_intake_app.track_intake()
        self.micro_intake_app.track_intake()

    def save_serving_size(self, new_serving_size: str):
        try:            
            new_serving_size = float(new_serving_size)
            original_serving_size = float(self.serving_size_entry.get())

            if original_serving_size < 0:
                raise ValueError("Original serving size must not be negative.")

            ratio = new_serving_size / original_serving_size
            self.serving_size_entry.delete(0, tk.END)
            self.serving_size_entry.insert(0, str(new_serving_size))

            # List of entry widgets to be scaled
            entries_to_scale = [
                self.cals_entry, self.protein_entry, self.carbs_entry,
                self.fiber_entry, self.sugars_entry, self.added_sugars_entry,
                self.total_fats_entry, self.saturated_fats_entry, self.trans_fats_entry,
                self.polyunsaturated_fats_entry, self.monounsaturated_fats_entry, self.iron_entry,
                self.zinc_entry, self.calcium_entry, self.magnesium_entry, self.potassium_entry,
                self.vitA_entry, self.vitB12_entry, self.vitC_entry, self.vitD_entry, self.omega3_entry,
                self.omega6_entry, self.cholesterol_entry, self.sodium_entry
            ]

            for entry in entries_to_scale:
                current_value = float(entry.get())
                new_value = current_value * ratio
                entry.delete(0, tk.END)
                entry.insert(0, str(new_value))

            return True  # Indicate success to on_save

        except ValueError as e:
            print("Error:", e)
            return


    def adjust_serving_size(self):
        if self.name_entry.get() == "":
            print("Please add food information")
            return

        adjust_serving_size_window = tk.Toplevel(self.root)
        adjust_serving_size_window.title("Adjust Serving Size")

        ttk.Label(adjust_serving_size_window, text="New Serving Size (g/mL):").grid(row=0, column=0, padx=0, pady=5)
        new_serving_size_entry = ttk.Entry(adjust_serving_size_window, width=27)
        new_serving_size_entry.grid(row=1, column=0, padx=0, pady=5)

        def on_save():
            if self.save_serving_size(new_serving_size_entry.get()):
                adjust_serving_size_window.destroy()
            else:
                print("Failed to update serving size. Check input.")

        save_serving_size_button = ttk.Button(adjust_serving_size_window, text="Save Serving Size", command=on_save)
        save_serving_size_button.grid(row=2, column=0, padx=0, pady=5)


    def add_food(self):
        if self.name_entry.get() == "":
            print("Please add food information")
            return

        # Getting data to construct food object
        name = self.name_entry.get()
        grams = float(self.serving_size_entry.get())
        cals = float(self.cals_entry.get())
        protein = float(self.protein_entry.get())
        
        # Getting data to construct carb object
        carb = float(self.carbs_entry.get())
        fiber = float(self.fiber_entry.get())
        sugars = float(self.sugars_entry.get())
        added_sugars = float(self.added_sugars_entry.get())
        
        carb = fc.Carbs(carb, fiber, sugars, added_sugars)
        
        # Getting data to construct fat object
        total_fats = float(self.total_fats_entry.get())
        saturated_fats = float(self.saturated_fats_entry.get())
        trans_fats = float(self.trans_fats_entry.get())
        polyunsaturated_fats = float(self.polyunsaturated_fats_entry.get())
        monounsaturated_fats = float(self.monounsaturated_fats_entry.get())
        
        fat = fc.Fats(total_fats, saturated_fats, trans_fats, polyunsaturated_fats, monounsaturated_fats)

        # Gretting data to construct micronutrient object
        iron = float(self.iron_entry.get())
        zinc = float(self.zinc_entry.get())
        calcium = float(self.calcium_entry.get())
        magnesium = float(self.magnesium_entry.get())
        potassium = float(self.potassium_entry.get())
        vitaminA = float(self.vitA_entry.get())
        vitaminB12 = float(self.vitB12_entry.get())
        vitaminC = float(self.vitC_entry.get())
        vitaminD = float(self.vitD_entry.get())
        omega3 = float(self.omega3_entry.get())
        omega6 = float(self.omega6_entry.get())
        cholesterol = float(self.cholesterol_entry.get())
        sodium = float(self.sodium_entry.get())

        micro = fc.MicroNutrients(iron, zinc, calcium, magnesium, potassium, vitaminA, 
                                  vitaminB12, vitaminC, vitaminD, omega3, omega6, cholesterol, sodium)

        food_item = fc.Food(name, cals, grams, protein, carb, fat, micro)

        # self.result_label.config(text="Food added successfully:\n" + str(food_item))

        self.macro_intake_app.add_food_item(food_item)
        self.macro_intake_app.update_progress()

        self.micro_intake_app.add_food_item(food_item)
        self.micro_intake_app.update_progress()

    """
    def record_food(self):
        if self.name_entry.get() == "":
            print("Please add food information")
            return

        name = self.name_entry.get()
        cals = float(self.cals_entry.get())
        protein = float(self.protein_entry.get())
        carb = float(self.carbs_entry.get())
        fiber = float(self.fiber_entry.get())
        sugars = float(self.sugars_entry.get())
        added_sugars = float(self.added_sugars_entry.get())
        total_fats = float(self.total_fats_entry.get())
        saturated_fats = float(self.saturated_fats_entry.get())
        trans_fats = float(self.trans_fats_entry.get())
        polyunsaturated_fats = float(self.polyunsaturated_fats_entry.get())
        monounsaturated_fats = float(self.monounsaturated_fats_entry.get())
        grams = float(self.serving_size_entry.get())

        fat = fc.Fats(total_fats, saturated_fats, trans_fats, polyunsaturated_fats, monounsaturated_fats)
        carb = fc.Carbs(carb, fiber, sugars, added_sugars)  # Not taking fiber, sugars, and added sugars as input currently

        food_item = fc.Food(name, grams, cals, protein, carb, fat)
        # self.result_label.config(text="Food loaded to records:\n" + str(food_item))

        fc.record_preloaded_food(food_item, PRELOADED_FILE_PATH)
    """
        
    def clear_entries(self):
        # Clear all text box entries
        self.name_entry.delete(0, tk.END)
        self.cals_entry.delete(0, tk.END)
        self.protein_entry.delete(0, tk.END)
        self.carbs_entry.delete(0, tk.END)
        self.fiber_entry.delete(0, tk.END)
        self.sugars_entry.delete(0, tk.END)
        self.added_sugars_entry.delete(0, tk.END)
        self.total_fats_entry.delete(0, tk.END)
        self.saturated_fats_entry.delete(0, tk.END)
        self.trans_fats_entry.delete(0, tk.END)
        self.polyunsaturated_fats_entry.delete(0, tk.END)
        self.monounsaturated_fats_entry.delete(0, tk.END)
        self.serving_size_entry.delete(0, tk.END)
        self.iron_entry.delete(0, tk.END)
        self.zinc_entry.delete(0, tk.END)
        self.calcium_entry.delete(0, tk.END)
        self.magnesium_entry.delete(0, tk.END)
        self.potassium_entry.delete(0, tk.END)
        self.vitA_entry.delete(0, tk.END)
        self.vitB12_entry.delete(0, tk.END)
        self.vitC_entry.delete(0, tk.END)
        self.vitD_entry.delete(0, tk.END)
        self.omega3_entry.delete(0, tk.END)
        self.omega6_entry.delete(0, tk.END)
        self.cholesterol_entry.delete(0, tk.END)
        self.sodium_entry.delete(0, tk.END)

    def load_recorded_food(self):
        # Read the recorded foods from the preloaded.csv file
        self.recorded_foods = []
        with open(PRELOADED_FILE_PATH, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # print(row)
                name, cals, grams, protein, carbs, fiber, total_sugar, added_sugar, fats, sat, trans, poly, mono, iron, zinc, calcium, magnesium, potassium, vitaminA, vitaminB12, vitaminC, vitaminD, omega3, omega6, cholesterol, sodium = row

                # Convert the appropriate fields to their respective types
                cals = float(cals)
                grams = float(grams)
                protein = float(protein)
                carbs = float(carbs)
                fiber = float(fiber)
                total_sugar = float(total_sugar)
                added_sugar = float(added_sugar)
                fats = float(fats)
                sat = float(sat)
                trans = float(trans)
                poly = float(poly)
                mono = float(mono)
                iron = float(iron)
                zinc = float(zinc)
                calcium = float(calcium)
                magnesium = float(magnesium)
                potassium = float(potassium)
                vitaminA = float(vitaminA)
                vitaminB12 = float(vitaminB12)
                vitaminC = float(vitaminC)
                vitaminD = float(vitaminD)
                omega3 = float(omega3)
                omega6 = float(omega6)
                cholesterol = float(cholesterol)
                sodium = float(sodium)


                # Append the converted data to recorded_foods
                self.recorded_foods.append((cals, grams, name, protein, carbs, fiber, total_sugar, added_sugar, fats, sat, trans, poly, mono, iron, zinc, calcium, magnesium, potassium, vitaminA, vitaminB12, vitaminC, vitaminD, omega3, omega6, cholesterol, sodium))
        
        # New window to display the recorded foods
        recorded_food_window = tk.Toplevel(self.root)
        recorded_food_window.title("Recorded Foods")

        # Entry widget for the search bar
        search_var = tk.StringVar()
        search_entry = ttk.Entry(recorded_food_window, textvariable=search_var)
        search_entry.pack(padx=5, pady=5, fill=tk.X)

        # Frame with a vertical scrollbar
        frame = ttk.Frame(recorded_food_window)
        frame.pack(fill=tk.BOTH, expand=1)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox to display recorded foods
        recorded_food_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=50)
        for food in self.recorded_foods:
            recorded_food_listbox.insert(tk.END, food[2])  # Display only names of the foods

        recorded_food_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Set the scrollbar to scroll the listbox
        scrollbar.config(command=recorded_food_listbox.yview)

        # Function to update listbox based on search query
        def update_listbox(event=None):
            search_query = search_var.get().lower()
            recorded_food_listbox.delete(0, tk.END)
            for food in self.recorded_foods:
                if search_query in food[2].lower():
                    recorded_food_listbox.insert(tk.END, food[2])

        # Bind the search function to the search bar's <<KeyRelease>> event
        search_var.trace_add("write", lambda *args: update_listbox())

        # Double-click event handler to fill macronutrients and calories into FoodApp
        recorded_food_listbox.bind("<Double-1>", lambda event: self.fill_food_entry(recorded_food_listbox, recorded_food_window, event))

    def fill_food_entry(self, recorded_food_listbox, recorded_food_window, event):
        # Clear any prior entries
        self.clear_entries()

        # Get the selected food item from the listbox
        selected_index = recorded_food_listbox.curselection()
        if selected_index:
            selected_food = recorded_food_listbox.get(selected_index)
            # Find the selected food in the recorded foods list
            for food in self.recorded_foods:
                if food[2] == selected_food:
                    # Fill the entry fields with the selected food's macronutrients and calories
                    self.cals_entry.insert(0, food[0])
                    self.serving_size_entry.insert(0, food[1])
                    self.name_entry.insert(0, food[2])
                    self.protein_entry.insert(0, food[3])
                    self.carbs_entry.insert(0, food[4])
                    self.fiber_entry.insert(0, food[5])
                    self.sugars_entry.insert(0, food[6])
                    self.added_sugars_entry.insert(0, food[7])
                    self.total_fats_entry.insert(0, food[8])
                    self.saturated_fats_entry.insert(0, food[9])
                    self.trans_fats_entry.insert(0, food[10])
                    self.polyunsaturated_fats_entry.insert(0, food[11])
                    self.monounsaturated_fats_entry.insert(0, food[12])
                    self.iron_entry.insert(0, food[13])
                    self.zinc_entry.insert(0, food[14])
                    self.calcium_entry.insert(0, food[15])
                    self.magnesium_entry.insert(0, food[16])
                    self.potassium_entry.insert(0, food[17])
                    self.vitA_entry.insert(0, food[18])
                    self.vitB12_entry.insert(0, food[19])
                    self.vitC_entry.insert(0, food[20])
                    self.vitD_entry.insert(0, food[21])
                    self.omega3_entry.insert(0, food[22])
                    self.omega6_entry.insert(0, food[23])
                    self.cholesterol_entry.insert(0, food[24])
                    self.sodium_entry.insert(0, food[25])
                    break

        recorded_food_window.destroy()

class MacroIntakeApp:
    def __init__(self, root, menu):
        self.root = root
        self.root.title("Macronutrient Intake")
        self.menu = menu
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        self.food_items = []

        self.consumed_calories = 0
        self.consumed_protein = 0
        self.consumed_carbs = 0
        self.consumed_fats = 0

        # Initialize variables to store goals and progress
        self.calories_goal = tk.StringVar()
        self.protein_goal = tk.StringVar()
        self.carbs_goal = tk.StringVar()
        self.fats_goal = tk.StringVar()

        ttk.Label(root, text="Calories Goal:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(root, text="Protein Goal (g):").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(root, text="Carbs Goal (g):").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(root, text="Fats Goal (g):").grid(row=3, column=0, padx=5, pady=5)

        ttk.Entry(root, textvariable=self.calories_goal, width=30).grid(row=0, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.protein_goal, width=30).grid(row=1, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.carbs_goal, width=30).grid(row=2, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.fats_goal, width=30).grid(row=3, column=1, padx=5, pady=5)

        # Button to update progress
        ttk.Button(root, text="Update Progress", command=self.update_progress).grid(row=4, column=1, padx=5, pady=5)

        # self.update_progress()  # Initial update to display the graphs

        # Create a frame to contain the pie charts
        self.progress_frame = ttk.Frame(root)
        self.progress_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Load today's data if available
        self.load_today_data()

    def hide_window(self):
        self.root.withdraw()  # This hides the window instead of closing it

    # Add a method to toggle visibility
    def toggle_visibility(self):
        if self.root.state() == 'withdrawn':
            self.root.deiconify()  # Show the window if it is hidden
        else:
            self.hide_window()  # Hide the window otherwise

    def load_today_data(self):
        # Get today's date as a string
        today_date = str(dt.date.today().strftime("%Y-%m-%d"))

        # Check if today's date exists in the track.csv file
        with open(self.menu.user_macro_track_file, "r") as file:
            reader = file.readlines()
            lines = len(reader)
            if lines == 1:
                self.calories_goal.set(0)
                self.protein_goal.set(0)
                self.carbs_goal.set(0)
                self.fats_goal.set(0)
            else:
                for row_ind in range(len(reader)):
                    row = reader[row_ind].split(",") # This seperates the items in our row, otherwise it is one long string
                    if row[0] == today_date:
                        # Load goals
                        self.calories_goal.set(row[5])
                        self.protein_goal.set(row[6])
                        self.carbs_goal.set(row[7])
                        self.fats_goal.set(row[8])

                        # Load consumed foods
                        self.consumed_calories += float(row[1])
                        self.consumed_protein += float(row[2])
                        self.consumed_carbs += float(row[3])
                        self.consumed_fats += float(row[4])

                        # Update the UI
                        self.update_progress()
                        break  # Stop searching once today's data is found

                    elif row_ind == lines - 1:
                        # Load goals
                        self.calories_goal.set(row[5])
                        self.protein_goal.set(row[6])
                        self.carbs_goal.set(row[7])
                        self.fats_goal.set(row[8])

                        # Update the UI
                        self.update_progress()
                        break  # Stop searching once today's data is found
                

    def add_food_item(self, food_item):
        # Calculate consumed values
        self.consumed_calories += food_item.cals
        self.consumed_protein += food_item.prot
        self.consumed_carbs += food_item.carb.total
        self.consumed_fats += food_item.fat.total

    def update_progress(self):

        # Fetch goals from entry fields
        calories_goal = float(self.calories_goal.get())
        protein_goal = float(self.protein_goal.get())
        carbs_goal = float(self.carbs_goal.get())
        fats_goal = float(self.fats_goal.get())

        # Prepare data for pie charts
        categories = ['Calories', 'Protein', 'Carbs', 'Fats']
        consumed_values = [self.consumed_calories, self.consumed_protein, self.consumed_carbs, self.consumed_fats]
        goal_values = [calories_goal, protein_goal, carbs_goal, fats_goal]

        # Clear any existing pie charts
        for child in self.progress_frame.winfo_children():
            child.destroy()

        # Plotting pie charts
        fig, axs = plt.subplots(2, 2, facecolor='#5A5A5B')
        fig.suptitle('Macronutrient Intake Progress', color="white")

        # Define color map for blue shades
        colors = plt.cm.Blues_r(np.linspace(0.2, 1, 3))

        for i in range(2):
            for j in range(2):
                index = 2 * i + j
                ax = axs[i, j]
                # print(consumed_values[index], goal_values[index])
                if consumed_values[index] <= goal_values[index]:
                    ax.pie([consumed_values[index], goal_values[index] - consumed_values[index]],
                        autopct=lambda p: '{:.0f}'.format(p * sum([consumed_values[index],  goal_values[index] - consumed_values[index]]) / 100),
                        startangle=90, colors=colors)
                    ax.set_title(categories[index], color='white')
                else:
                    ax.pie([1, 0], autopct=lambda p: '{:.0f}'.format(p * sum([consumed_values[index], goal_values[index] - consumed_values[index]]) / 100),
                        startangle=90, colors=[colors[0], 'black'])
                    ax.set_title(categories[index], color='white')


        # Customize subplot background color and text color
        for ax in axs.flat:
            ax.set_facecolor('black')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.title.set_color('white')

        # Embedding the plots into the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.progress_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        plt.close(fig)  # Close the figure to prevent duplicate displays
        

    def track_intake(self):
        # Get today's date
        today_date = dt.date.today().strftime("%Y-%m-%d")

    
        # Fetch goals from entry fields
        calories_goal = float(self.calories_goal.get())
        protein_goal = float(self.protein_goal.get())
        carbs_goal = float(self.carbs_goal.get())
        fats_goal = float(self.fats_goal.get())

        # Prepare data for writing
        data = [today_date, self.consumed_calories, self.consumed_protein, self.consumed_carbs, self.consumed_fats, calories_goal, protein_goal, carbs_goal, fats_goal]

        # We are assuming this file exists which might get problematic... (this feels like foreshadowing) (it was)
        rows_to_keep = []
        with open(self.menu.user_macro_track_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                # Check if the date in the first column matches today's date
                if row[0] != today_date:
                    rows_to_keep.append(row)

        # Write data to track.csv
        with open(self.menu.user_macro_track_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_keep)
            writer.writerow(data)

class MicroIntakeApp:
    def __init__(self, root, menu):
        self.root = root
        self.root.title("Micronutrient Intake")
        self.menu = menu
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)


        # Full set of micronutrients with example daily goals
        self.micronutrients_consumed = {
            'Iron': {'consumed': 0.0, 'goal': 18.0},  # mg/day for an average adult
            'Zinc': {'consumed': 0.0, 'goal': 11.0},  # mg/day
            'Calcium': {'consumed': 0.0, 'goal': 1000.0},  # mg/day
            'Magnesium': {'consumed': 0.0, 'goal': 400.0},  # mg/day
            'Potassium': {'consumed': 0.0, 'goal': 4700.0},  # mg/day
            'Vitamin A': {'consumed': 0.0, 'goal': 900.0},  # mcg/day
            'Vitamin B12': {'consumed': 0.0, 'goal': 2.4},  # mcg/day
            'Vitamin C': {'consumed': 0.0, 'goal': 90.0},  # mg/day
            'Vitamin D': {'consumed': 0.0, 'goal': 20.0},  # mcg/day
            'Omega-3': {'consumed': 0.0, 'goal': 1600.0},  # mg/day
            'Omega-6': {'consumed': 0.0, 'goal': 17000.0},  # mg/day
            'Cholesterol': {'consumed': 0.0, 'goal': 300.0},  # mg/day
            'Sodium': {'consumed': 0.0, 'goal': 2300.0}  # mg/day
        }

        # Create a frame for displaying the progress bars
        self.progress_frame = ttk.Frame(root)
        self.progress_frame.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky="ew")

        # Button to update progress
        ttk.Button(root, text="Update Progress", command=self.update_progress).grid(row=0, column=0, padx=5, pady=5)

        self.update_progress()  # Initial update to display the bars

    def hide_window(self):
        self.root.withdraw()  # This hides the window instead of closing it

    # Add a method to toggle visibility
    def toggle_visibility(self):
        if self.root.state() == 'withdrawn':
            self.root.deiconify()  # Show the window if it is hidden
            self.update_progress()
        else:
            self.hide_window()  # Hide the window otherwise

    def add_food_item(self, food):
        self.micronutrients_consumed["Iron"]["consumed"] += food.micro.iron
        self.micronutrients_consumed["Zinc"]["consumed"] += food.micro.zinc
        self.micronutrients_consumed["Calcium"]["consumed"] += food.micro.calcium
        self.micronutrients_consumed["Magnesium"]["consumed"] += food.micro.magnesium
        self.micronutrients_consumed["Potassium"]["consumed"] += food.micro.potassium
        self.micronutrients_consumed["Vitamin C"]["consumed"] += food.micro.vitaminC
        self.micronutrients_consumed["Omega-3"]["consumed"] += food.micro.omega3
        self.micronutrients_consumed["Omega-6"]["consumed"] += food.micro.omega6
        self.micronutrients_consumed["Cholesterol"]["consumed"] += food.micro.cholesterol
        self.micronutrients_consumed["Sodium"]["consumed"] += food.micro.sodium

        # Convert mcg to mg for Vitamin A, Vitamin B12, and Vitamin D
        self.micronutrients_consumed["Vitamin A"]["consumed"] += food.micro.vitaminA / 1000
        self.micronutrients_consumed["Vitamin B12"]["consumed"] += food.micro.vitaminB12 / 1000
        self.micronutrients_consumed["Vitamin D"]["consumed"] += food.micro.vitaminD / 1000

        # print(self.micronutrients_consumed)
        # self.update_progress()

    def update_progress(self):
        # Clear any existing widgets in the progress frame
        for widget in self.progress_frame.winfo_children():
            widget.destroy()

        app_background_color = '#5A5A5B'

        fig, ax = plt.subplots(figsize=(10, 8), facecolor=app_background_color)  # Adjust size for better visibility and set background color
        nutrients = list(self.micronutrients_consumed.keys())[::-1]
        consumed_values = [(self.micronutrients_consumed[nutrient]['consumed']) for nutrient in nutrients]
        goal_values = [self.micronutrients_consumed[nutrient]['goal'] for nutrient in nutrients]
        ratios = [min(consumed / goal, 1) if goal > 0 else 0 for consumed, goal in zip(consumed_values, goal_values)]

        colors = plt.cm.Blues_r(np.linspace(0.2, 1, len(nutrients)))

        # Creating the bar plot with proportional values
        ax.barh(nutrients, ratios, color=colors)
        for i, (ratio, consumed, goal) in enumerate(zip(ratios, consumed_values, goal_values)):
            ax.text(1.05, i, f' {consumed:.2f}/{goal:.2f} mg', va='center', color='white') 

        ax.set_xlabel('Proportion of Daily Goal', color='white')
        ax.set_title('Micronutrient Intake Progress', color='white')
        ax.set_xlim(0, 1)

        # Customize background and text colors
        ax.set_facecolor(app_background_color)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis.label.set_color('white')
        ax.title.set_color('white')

        plt.tight_layout()

        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.progress_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        plt.close(fig)  # Close the figure to prevent duplicate displays

    def track_intake(self):
        # Get today's date
        today_date = dt.date.today().strftime("%Y-%m-%d")

        data = [
            today_date,
            self.micronutrients_consumed["Iron"]["consumed"],
            self.micronutrients_consumed["Zinc"]["consumed"],
            self.micronutrients_consumed["Calcium"]["consumed"],
            self.micronutrients_consumed["Magnesium"]["consumed"],
            self.micronutrients_consumed["Potassium"]["consumed"],
            self.micronutrients_consumed["Vitamin C"]["consumed"],
            self.micronutrients_consumed["Omega-3"]["consumed"],
            self.micronutrients_consumed["Omega-6"]["consumed"],
            self.micronutrients_consumed["Cholesterol"]["consumed"],
            self.micronutrients_consumed["Sodium"]["consumed"],
            self.micronutrients_consumed["Vitamin A"]["consumed"],
            self.micronutrients_consumed["Vitamin B12"]["consumed"],
            self.micronutrients_consumed["Vitamin D"]["consumed"],
            self.micronutrients_consumed["Iron"]["goal"],
            self.micronutrients_consumed["Zinc"]["goal"],
            self.micronutrients_consumed["Calcium"]["goal"],
            self.micronutrients_consumed["Magnesium"]["goal"],
            self.micronutrients_consumed["Potassium"]["goal"],
            self.micronutrients_consumed["Vitamin C"]["goal"],
            self.micronutrients_consumed["Omega-3"]["goal"],
            self.micronutrients_consumed["Omega-6"]["goal"],
            self.micronutrients_consumed["Cholesterol"]["goal"],
            self.micronutrients_consumed["Sodium"]["goal"],
            self.micronutrients_consumed["Vitamin A"]["goal"],
            self.micronutrients_consumed["Vitamin B12"]["goal"],
            self.micronutrients_consumed["Vitamin D"]["goal"]
        ]

        # We are assuming this file exists which might get problematic... (this feels like foreshadowing) (it was)
        rows_to_keep = []
        with open(self.menu.user_micro_track_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                # Check if the date in the first column matches today's date
                if row[0] != today_date:
                    rows_to_keep.append(row)

        # Write data to track.csv
        with open(self.menu.user_micro_track_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_keep)
            writer.writerow(data)


class ProgressApp:
    def __init__(self, root, menu) -> None:
        self.root = root
        self.root.title("Weekly Progress")
        self.menu = menu
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        # Dropdown for time window selection
        self.progress_window = tk.StringVar(value="1 week")
        ttk.Label(root, text="Select Time Window:").grid(row=0, column=0, padx=5, pady=5)
        ttk.OptionMenu(root, self.progress_window, "1 week", "3 days", "1 week", "2 weeks", "1 month", "1 year", command=self.update_progress).grid(row=0, column=1, padx=5, pady=5)

        # Dropdown for nutrient selection
        self.nutrient_selection = tk.StringVar(value="Calories")
        ttk.Label(root, text="Select Nutrient:").grid(row=1, column=0, padx=5, pady=5)
        self.nutrient_options = ["Calories (kcal)", "Protein (g)", "Carbs (g)", "Fats (g)", "Iron (mg)", "Zinc (mg)", "Calcium (mg)", "Magnesium (mg)", "Potassium (mg)", "VitaminC (mg)", "Omega-3 (mg)", "Omega-6 (mg)", "Cholesterol (mg)", "Sodium (mg)", "VitaminA (mcg)", "VitaminB12 (mcg)", "VitaminD (mcg)"]
        ttk.OptionMenu(root, self.nutrient_selection, *self.nutrient_options, command=self.update_progress).grid(row=1, column=1, padx=5, pady=5)

        # Placeholder for the line graph
        self.figure = plt.Figure(figsize=(8, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)

        # Load data and initialize the graph
        self.update_progress()

    def hide_window(self):
        self.root.withdraw()  # This hides the window instead of closing it

    # Add a method to toggle visibility
    def toggle_visibility(self):
        if self.root.state() == 'withdrawn':
            self.root.deiconify()  # Show the window if it is hidden
        else:
            self.hide_window()  # Hide the window otherwise

    def update_progress(self, *args):
        # Load data from macrotrack.csv and microtrack.csv
        macro_data = pd.read_csv(self.menu.user_macro_track_file)
        micro_data = pd.read_csv(self.menu.user_micro_track_file)
        
        # Combine the dataframes on the Date column
        data = pd.merge(macro_data, micro_data, on="Date")

        # Convert Date column to datetime
        data["Date"] = pd.to_datetime(data["Date"])

        # Filter data based on the selected time window
        today = dt.date.today()
        time_window = self.progress_window.get()
        if time_window == "3 days":
            start_date = today - dt.timedelta(days=3)
        elif time_window == "1 week":
            start_date = today - dt.timedelta(weeks=1)
        elif time_window == "2 weeks":
            start_date = today - dt.timedelta(weeks=2)
        elif time_window == "1 month":
            start_date = today - dt.timedelta(weeks=4)
        elif time_window == "1 year":
            start_date = today - dt.timedelta(weeks=52)
        else:
            start_date = today - dt.timedelta(weeks=1)  # Default to 1 week

        start_date = pd.Timestamp(start_date)
        filtered_data = data[data["Date"] >= start_date]
        # print(data)

        # Plot the selected nutrient
        selected_nutrient = self.nutrient_selection.get()
        self.ax.clear()
        self.ax.plot(filtered_data["Date"], filtered_data[selected_nutrient], marker='o', linestyle='-')
        self.ax.set_title(f'{selected_nutrient} Over Time')
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel(selected_nutrient)
        self.ax.grid(True)
        self.figure.autofmt_xdate()
        self.canvas.draw()



class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")

        # Create labels and entry boxes for username and password
        ttk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = ttk.Entry(root, width=15)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(root, show="*", width=15)  # Show '*' instead of actual password
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # login button
        ttk.Button(root, text="Login", command=self.login).grid(row=0, column=2, padx=5, pady=5, sticky="e")

        # Create a User button
        ttk.Button(root, text="Create User", command=self.create_user).grid(row=1, column=2, padx=5, pady=5, sticky="e")

        # Text widget to display error messages
        self.console_text = tk.Text(root, width=50, height=3, wrap=tk.WORD, state="disabled")
        # self.console_text.grid(row=2, column=0, columnspan=2) # Uncomment this line to display console messages

    def update_error_message(self, message):
        # Enable the text widget, clear any existing text, set the new message, and disable the widget
        self.console_text.config(state="normal")
        self.console_text.delete(1.0, tk.END)
        self.console_text.insert(tk.END, message)
        self.console_text.config(state="disabled")

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the user directory exists
        self.user_directory = os.path.join("users/", username)
        if not os.path.exists(self.user_directory):
            self.update_error_message("Username does not exist")
            return

        # Set tracking files
        self.user_macro_track_file = os.path.join("users/", f"{username}/macrotrack.csv")
        self.user_micro_track_file = os.path.join("users/", f"{username}/microtrack.csv")


        # Check if the password matches the one stored in the user file
        password_check = os.path.join("users/", f"{username}/{username}.txt")
        with open(password_check, "r") as file:
            stored_password = file.readline().strip()  # Read the stored password
            if password == stored_password:
                # Close the main menu window
                self.root.destroy()

                 # Initialize the main FoodApp and IntakeApps
                root_food = tk.Tk()
                root_macro_intake = tk.Toplevel(root_food)
                root_micro_intake = tk.Toplevel(root_food)
                root_prog_app = tk.Toplevel(root_food)

                macro_intake_app = MacroIntakeApp(root_macro_intake, self)
                micro_intake_app = MicroIntakeApp(root_micro_intake, self)
                progress_app = ProgressApp(root_prog_app, self)
                food_app = FoodApp(root_food, macro_intake_app, micro_intake_app, progress_app)

                # Minimize the intake windows on start
                # root_macro_intake.iconify()
                # root_micro_intake.iconify()

                root_food.mainloop()
            else:
                self.update_error_message("Wrong password")

    def create_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username already exists
        user_directory = os.path.join("users", username)

        self.user_macro_track_file = os.path.join(user_directory, "macrotrack.csv")
        self.user_micro_track_file = os.path.join(user_directory, "microtrack.csv")
        print(self.user_macro_track_file, self.user_micro_track_file)


        if os.path.exists(user_directory):
            self.update_error_message("Username already exists")
            return

        os.makedirs(user_directory, exist_ok=True)

        # Write the password to the user file in the user directory
        with open(os.path.join(user_directory, f"{username}.txt"), "w") as file:
            file.write(password)
            self.update_error_message(f"User: {username} created")


        # Create the track.csv file in the user directory
        with open(self.user_macro_track_file, mode="w", newline="") as track_file:
            track_file.write("Date,Calories (kcal),Protein (g),Carbs (g),Fats (g),Calories Goal,Protein Goal,Carbs Goal,Fats Goal\n")

        with open(self.user_micro_track_file, mode="w", newline="") as track_file:
            track_file.write("Date,Iron (mg),Zinc (mg),Calcium (mg),Magnesium (mg),Potassium (mg),VitaminC (mg),Omega-3 (mg),Omega-6 (mg),Cholesterol (mg),Sodium (mg),VitaminA (mcg),VitaminB12 (mcg), VitaminD (mcg),Iron Goal(mg),Zinc Goal(mg),Calcium Goal(mg),Magnesium Goal(mg),Potassium Goal(mg),VitaminC Goal(mg),Omega-3 Goal(mg),Omega-6 Goal(mg),Cholesterol Goal(mg),Sodium Goal(mg),VitaminA Goal(mcg),VitaminB12 Goal(mcg), VitaminD Goal(mcg)\n")


        # Clear username and password entries after user creation
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)



def main():
    root_menu = tk.Tk()
    main_menu = MainMenu(root_menu)
    root_menu.mainloop()


if __name__ == "__main__":
    main()
