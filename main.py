# Imports for tkinter, the main interface
import tkinter as tk
from tkinter import ttk

# Imports for plotting
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Imports for utility features
import csv
import datetime as dt
import os

# Imports for data classes
import food_class as fc

PRELOADED_FILE_PATH = "/Users/itaymevorach/Documents/personal project/cal:macro track/preloaded.csv"
TRACK_FILE_PATH = "cal:macro track/track.csv"
    
class FoodApp:
    def __init__(self, root, intake_app):
        self.root = root
        self.intake_app = intake_app
        self.recorded_foods = []  # Define recorded_foods as an attribute
        self.root.title("Calorie Tracker")

        ttk.Label(root, text="Food Name, Brand:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(root, width=27)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Calories (kcal):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.cals_entry = ttk.Entry(root, width=27)
        self.cals_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Protein (g):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.protein_entry = ttk.Entry(root, width=27)
        self.protein_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Carbohydrates (g):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.carbs_entry = ttk.Entry(root, width=27)
        self.carbs_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Fiber (g):").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.fiber_entry = ttk.Entry(root, width=27)
        self.fiber_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Total Sugars (g):").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.sugars_entry = ttk.Entry(root, width=27)
        self.sugars_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Added Sugars (g):").grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.added_sugars_entry = ttk.Entry(root, width=27)
        self.added_sugars_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Total Fats (g):").grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.total_fats_entry = ttk.Entry(root, width=27)
        self.total_fats_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Saturated Fats (g):").grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.saturated_fats_entry = ttk.Entry(root, width=27)
        self.saturated_fats_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Trans Fats (g):").grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.trans_fats_entry = ttk.Entry(root, width=27)
        self.trans_fats_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Polyunsaturated Fats (g):").grid(row=10, column=0, padx=5, pady=5, sticky="w")
        self.polyunsaturated_fats_entry = ttk.Entry(root, width=27)
        self.polyunsaturated_fats_entry.grid(row=10, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Monounsaturated Fats (g):").grid(row=11, column=0, padx=5, pady=5, sticky="w")
        self.monounsaturated_fats_entry = ttk.Entry(root, width=27)
        self.monounsaturated_fats_entry.grid(row=11, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(root, text="Serving Size (g/mL):").grid(row=12, column=0, padx=5, pady=5, sticky="w")
        self.serving_size_entry = ttk.Entry(root, width=27)
        self.serving_size_entry.grid(row=12, column=1, padx=5, pady=5, sticky="w")

        # Adds foods
        add_button = ttk.Button(root, text="Add Food", command=self.add_food)
        add_button.grid(row=13, column=0, padx=5, pady=5)
        
        # Clears text boxes
        clear_button = ttk.Button(root, text="Clear", command=self.clear_entries)
        clear_button.grid(row=13, column=1, columnspan=2, padx=5, pady=5)

        # Initialize button for food loading and recording
        goals_button = ttk.Button(root, text="Save Food to Records", command=self.record_food)
        goals_button.grid(row=14, column=0, padx=0, pady=5)

        load_recorded_button = ttk.Button(root, text="Load Recorded Food", command=self.load_recorded_food)
        load_recorded_button.grid(row=14, column=1, padx=0, pady=5)

        # Create and place result label
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=15, column=0, columnspan=2, padx=5, pady=5)

    def add_food(self):
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

        food_item = fc.Food(name, cals, protein, carb, fat, grams)
        self.result_label.config(text="Food added successfully:\n" + str(food_item))

        self.intake_app.add_food_item(food_item)
        self.intake_app.update_progress()

    def record_food(self):
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

        food_item = fc.Food(name, cals, protein, carb, fat, grams)
        self.result_label.config(text="Food loaded to records:\n" + str(food_item))

        fc.record_preloaded_food(food_item, PRELOADED_FILE_PATH)

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

    def load_recorded_food(self):
        # Read the recorded foods from the preloaded.csv file
        self.recorded_foods = []
        with open(PRELOADED_FILE_PATH, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                cals, grams, name, protein, carbs, fiber, total_sugar, added_sugar, fats, sat, trans, poly, mono = row
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
                # Append the converted data to recorded_foods
                self.recorded_foods.append((cals, grams, name, protein, carbs, fiber, total_sugar, added_sugar, fats, sat, trans, poly, mono))
        
        # Create a new window to display the recorded foods
        recorded_food_window = tk.Toplevel(self.root)
        recorded_food_window.title("Recorded Foods")

        # Create a frame with a vertical scrollbar
        frame = ttk.Frame(recorded_food_window)
        frame.pack(fill=tk.BOTH, expand=1)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


        """
        I have a certain cancer that I must eliminate from this program....
        I suspect it has something to do with my self.recorded_foods......
        I am tired....
        """

        # Create a listbox to display the recorded foods
        recorded_food_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=50)
        for food in self.recorded_foods:
            recorded_food_listbox.insert(tk.END, food[2])  # Display only the names of the recorded foods

        recorded_food_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Set the scrollbar to scroll the listbox
        scrollbar.config(command=recorded_food_listbox.yview)

        # Double-click event handler to fill macronutrients and calories into FoodApp
        recorded_food_listbox.bind("<Double-1>", lambda event: self.fill_food_entry(recorded_food_listbox, event))

    def fill_food_entry(self, recorded_food_listbox, event):
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
                    self.name_entry.insert(0, food[2])
                    self.cals_entry.insert(0, food[0])
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
                    self.serving_size_entry.insert(0, food[1])
                    break

class DailyIntakeApp:
    def __init__(self, root, menu):
        self.root = root
        self.root.title("Daily Intake")
        self.menu = menu

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

        ttk.Label(root, text="Calories Goal:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="Protein Goal (g):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="Carbs Goal (g):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="Fats Goal (g):").grid(row=3, column=0, padx=5, pady=5, sticky="w")

        ttk.Entry(root, textvariable=self.calories_goal, width=30).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(root, textvariable=self.protein_goal, width=30).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(root, textvariable=self.carbs_goal, width=30).grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(root, textvariable=self.fats_goal, width=30).grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Create a button to update progress
        ttk.Button(root, text="Update Progress/Set Goals", command=self.update_progress).grid(row=4, column=0, padx=5, pady=5)

        # Create a button to track today's intake
        ttk.Button(root, text="Track Today's Intake", command=self.track_intake).grid(row=4, column=1, padx=5, pady=5)

        # Create a frame to contain the pie charts
        self.progress_frame = ttk.Frame(root)
        self.progress_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Load today's data if available
        self.load_today_data()

    def load_today_data(self):
        # Get today's date as a string
        today_date = str(dt.date.today().strftime("%Y-%m-%d"))

        # Check if today's date exists in the track.csv file
        with open(self.menu.user_track_file, "r") as file:
            reader = file.readlines()
            lines = len(reader)
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
        fig.suptitle('Daily Intake Progress')

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

        # We are assuming this file exists which might get problematic... (this feels like foreshadowing)
        rows_to_keep = []
        with open(self.menu.user_track_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                # Check if the date in the first column matches today's date
                if row[0] != today_date:
                    rows_to_keep.append(row)

        # Write data to track.csv
        with open(self.menu.user_track_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_keep)
            writer.writerow(data)


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")

        # Create labels and entry boxes for username and password
        ttk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry = ttk.Entry(root, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(root, show="*", width=30)  # Show '*' instead of actual password
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # login button
        ttk.Button(root, text="Login", command=self.login).grid(row=2, column=1, padx=5, pady=5, sticky="e")

        # Create a User button
        ttk.Button(root, text="Create User", command=self.create_user).grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # Text widget to display error messages
        self.error_text = tk.Text(root, width=50, height=3, wrap=tk.WORD, state="disabled")
        self.error_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def update_error_message(self, message):
        # Enable the text widget, clear any existing text, set the new message, and disable the widget
        self.error_text.config(state="normal")
        self.error_text.delete(1.0, tk.END)
        self.error_text.insert(tk.END, message)
        self.error_text.config(state="disabled")

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the user directory exists
        self.user_directory = os.path.join("cal:macro track/users/", username)
        if not os.path.exists(self.user_directory):
            self.update_error_message("Username does not exist")
            return

        # Set csv file
        self.user_track_file = os.path.join("cal:macro track/users/", f"{username}/track.csv")

        # Check if the password matches the one stored in the user file
        password_check = os.path.join("cal:macro track/users/", f"{username}/{username}.txt")
        with open(password_check, "r") as file:
            stored_password = file.readline().strip()  # Read the stored password
            if password == stored_password:
                # Close the main menu window
                self.root.destroy()

                # Open the FoodApp and DailyIntakeApp windows
                root_food = tk.Tk()
                root_intake = tk.Toplevel(root_food)

                daily_intake_app = DailyIntakeApp(root_intake, self)
                food_app = FoodApp(root_food, daily_intake_app)

                root_food.mainloop()
            else:
                self.update_error_message("Wrong password")

        """
        self.root.destroy()

        root_food = tk.Tk()
        root_intake = tk.Toplevel(root_food)

        daily_intake_app = DailyIntakeApp(root_intake)
        food_app = FoodApp(root_food, daily_intake_app)

        root_food.mainloop()
        """

    def create_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username already exists
        user_directory = os.path.join("cal:macro track/users/", username)

        if os.path.exists(user_directory):
            self.update_error_message("Username already exists")
            return

        os.makedirs(user_directory, exist_ok=True)

        # Write the password to the user file in the user directory
        with open(os.path.join(user_directory, f"{username}.txt"), "w") as file:
            file.write(password)
            self.update_error_message(f"User: {username} created")

        # Create the track.csv file in the user directory
        user_track_file = os.path.join(user_directory, "track.csv")
        with open(user_track_file, "w") as track_file:
            track_file.write("Date,Calories (kcal),Protein (g),Carbs (g),Fats (g),Calories Goal,Protein Goal,Carbs Goal,Fats Goal\n")

        # Clear username and password entries after user creation
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)



def main():
    root_menu = tk.Tk()
    main_menu = MainMenu(root_menu)
    root_menu.mainloop()


if __name__ == "__main__":

    main()
