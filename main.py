from tkinter import *
from tkinter import messagebox


# recipe class

class Recipe:
    def __init__(self, name, ingredients, instructions, cookingTime, dietaryInfo):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.cookingTime = cookingTime
        self.dietaryInfo = dietaryInfo

# recipe book class


class RecipeBook:
    def __init__(self):
        self.recipes = {
            "Chicken Curry": Recipe("Chicken Curry", ["chicken", "curry powder", "onion", "garlic", "salt", "oil"], "1. Mix all ingredients. \n2. Cook for 30 minutes.", "30 Minutes", "Contains Meat"),
            "Fried Rice": Recipe("Fried Rice", ["rice", "egg", "onion", "soy sauce", "oil"], "1. Fry the onion. \n2. Add the rice and egg. \n3. Add soy sauce and cook for 10 minutes.", "10 Minutes", "Vegetarian"),
            "Pancakes": Recipe("Pancakes", ["flour", "egg", "milk", "sugar", "baking powder", "salt"], "1. Mix all ingredients. \n2. Cook each pancake for 2 minutes on each side.", "10 Minutes", "Vegetarian"),
            "Spaghetti Bolognese": Recipe("Spaghetti Bolognese", ["spaghetti", "minced meat", "onion", "garlic", "tomato sauce", "oil", "salt"], "1. Cook the spaghetti. \n2. Cook the minced meat with onion, garlic, and tomato sauce. \n3. Serve the spaghetti with the sauce.", "30 Minutes", "Contains Meat"),
            "Beef Stir Fry": Recipe("Beef Stir Fry", ["beef", "bell peppers", "onion", "soy sauce", "oil", "salt"], "1. Fry the onion and bell peppers. \n2. Add the beef and soy sauce. \n3. Cook for 15 minutes.", "15 Minutes", "Contains Meat"),
            "Cheese Pizza": Recipe("Cheese Pizza", ["pizza dough", "tomato sauce", "mozzarella cheese", "basil", "olive oil"], "1. Roll out the dough. \n2. Add the sauce, cheese, and basil. \n3. Cook in a preheated oven for 15 minutes.", "15 Minutes", "Vegetarian"),
            "Grilled Salmon": Recipe("Grilled Salmon", ["salmon fillet", "lemon", "dill", "salt", "pepper", "oil"], "1. Season the salmon. \n2. Grill for 10 minutes on each side. \n3. Serve with lemon and dill.", "20 Minutes", "Pescatarian"),
            "Veggie Tacos": Recipe("Veggie Tacos", ["tortillas", "black beans", "corn", "avocado", "lettuce", "salsa"], "1. Heat the tortillas. \n2. Fill with beans, corn, avocado, and lettuce. \n3. Top with salsa.", "15 Minutes", "Vegan"),
            "Lentil Soup": Recipe("Lentil Soup", ["lentils", "carrots", "onion", "celery", "broth", "salt"], "1. Cook all ingredients in a pot. \n2. Simmer for 45 minutes.", "45 Minutes", "Vegan"),
            "Shrimp Scampi": Recipe("Shrimp Scampi", ["shrimp", "garlic", "butter", "white wine", "parsley"], "1. Cook garlic in butter. \n2. Add the shrimp and wine. \n3. Cook for 10 minutes. \n4. Serve with parsley.", "10 Minutes", "Pescatarian"),
            "Garden Salad": Recipe("Garden Salad", ["lettuce", "tomatoes", "cucumbers", "carrots", "salad dressing"], "1. Combine all ingredients in a bowl. \n2. Toss with dressing.", "10 Minutes", "Vegan"),
            "Peanut Butter Sandwich": Recipe("Peanut Butter Sandwich", ["bread", "peanut butter", "jam"], "1. Spread peanut butter and jam on bread. \n2. Combine two slices.", "5 Minutes", "Vegetarian"),
            "Oatmeal": Recipe("Oatmeal", ["oats", "milk", "honey", "fruit"], "1. Cook oats and milk. \n2. Sweeten with honey. \n3. Top with fruit.", "10 Minutes", "Vegetarian"),
            "Roast Chicken": Recipe("Roast Chicken", ["whole chicken", "butter", "herbs", "salt", "pepper"], "1. Rub chicken with butter and herbs. \n2. Roast in oven for 90 minutes.", "90 Minutes", "Contains Meat"),
            "Hamburger": Recipe("Hamburger", ["beef patty", "bun", "lettuce", "tomato", "ketchup"], "1. Grill the beef patty. \n2. Assemble the hamburger.", "15 Minutes", "Contains Meat"),
            "Fish and Chips": Recipe("Fish and Chips", ["cod", "flour", "potatoes", "salt", "oil"], "1. Fry the cod in batter. \n2. Fry the potatoes. \n3. Serve with salt.", "30 Minutes", "Pescatarian"),
            "Veggie Burger": Recipe("Veggie Burger", ["veggie patty", "bun", "lettuce", "tomato", "ketchup"], "1. Grill the veggie patty. \n2. Assemble the burger.", "15 Minutes", "Vegetarian"),
            "Baked Ziti": Recipe("Baked Ziti", ["ziti", "tomato sauce", "mozzarella cheese", "ricotta cheese", "parmesan cheese"], "1. Cook ziti. \n2. Mix with sauce and cheese. \n3. Bake for 20 minutes.", "30 Minutes", "Vegetarian"),
            "Tofu Stir Fry": Recipe("Tofu Stir Fry", ["tofu", "bell peppers", "onion", "soy sauce", "oil", "salt"], "1. Fry the onion and bell peppers. \n2. Add the tofu and soy sauce. \n3. Cook for 15 minutes.", "15 Minutes", "Vegan"),
            "Chocolate Cake": Recipe("Chocolate Cake", ["flour", "sugar", "cocoa powder", "baking powder", "eggs", "milk", "butter", "vanilla extract"], "1. Mix dry ingredients. \n2. Add wet ingredients. \n3. Bake for 30 minutes.", "45 Minutes", "Vegetarian"),
        }
# function to create recipe

    def create_recipe(self, name, ingredients, instructions, cookingTime, dietaryInfo):
        self.recipes[name] = Recipe(
            name, ingredients, instructions, cookingTime, dietaryInfo)

# function to get recipe
    def get_recipe(self, name):
        matching_recipes = []
        for recipe_name, recipe in self.recipes.items():
            if name.lower() in recipe_name.lower():
                matching_recipes.append(recipe)
            else:
                for ingredient in recipe.ingredients:
                    if name.lower() in ingredient.lower():
                        matching_recipes.append(recipe)
                        break
        return matching_recipes

# function to delete recipe
    def delete_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
        else:
            raise ValueError(f"No recipe found with the name {name}")


# recipe interface
class RecipeApp:
    def __init__(self, root):
        self.recipe_book = RecipeBook()
        self.root = root
        self.root.geometry("1000x1000")
        self.root.title("Group B Recipe Book")

        Label(root, text="Recipe Name").grid(row=0)
        Label(root, text="Ingredients").grid(row=1)
        Label(root, text="Instructions").grid(row=2)
        Label(root, text="Cooking Time").grid(row=3)
        Label(root, text="Dietary Information").grid(row=4)

        self.e1 = Text(root, height=1, padx=5, pady=5)
        self.e2 = Text(root, height=3, padx=5, pady=5)
        self.e3 = Text(root, height=8, padx=5, pady=5)
        self.e4 = Text(root, height=1, padx=5, pady=5)
        self.e5 = Text(root, height=1, padx=5, pady=5)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)

        self.button_frame = Frame(root)
        self.button_frame.grid(row=5, column=0, columnspan=30, sticky='ew')

    # Configure the columns of the button frame
        for i in range(30):
            self.button_frame.grid_columnconfigure(i, weight=1)

# Buttons for Add, show, clear, delete and update
        Button(self.button_frame, text='Add Recipe', command=self.add_recipe).grid(
            row=6, column=0, sticky=NW, pady=4)
        Button(self.button_frame, text='Show All', command=self.show_recipe).grid(
            row=6, column=1, sticky=NW, pady=4)
        Button(self.button_frame, text='Vegetarian Recipes', command=self.show_veg_recipe).grid(
            row=6, column=2, sticky=NW, pady=4)
        Button(self.button_frame, text='Vegan Recipes', command=self.show_vegan_recipe).grid(
            row=6, column=3, sticky=NW, pady=4)
        Button(self.button_frame, text='Delete Recipe', command=self.delete_recipe).grid(
            row=6, column=4, sticky=NW, pady=4)
        Button(self.button_frame, text='Clear Text', command=self.clear_box).grid(
            row=6, column=5, sticky=NW, pady=4)
        Button(self.button_frame, text='Update Recipe', command=self.update_recipe).grid(
            row=6, column=6, sticky=NW, pady=4)

# listbox to show recipe names
        self.list_box = Listbox(root, height=18, width=40)
        self.list_box.grid(row=7, column=0, columnspan=3)
        self.list_box.bind('<Double-1>', self.load_recipe)

        self.show_all_recipes()

    # function to process input and call create recipe function
    def add_recipe(self):
        name = self.e1.get('1.0', 'end').strip()
        ingredients = self.e2.get('1.0', 'end').strip().split(',')
        instructions = self.e3.get('1.0', 'end').strip()
        cookingTime = self.e4.get('1.0', 'end').strip()
        dietaryInfo = self.e5.get('1.0', 'end').strip()
        self.recipe_book.create_recipe(
            name, ingredients, instructions, cookingTime, dietaryInfo)
        self.show_all_recipes()
        messagebox.showinfo("Recipe Book", "Recipe added successfully!")
        self.e1.delete('1.0', 'end')
        self.e2.delete('1.0', 'end')
        self.e3.delete('1.0', 'end')
        self.e4.delete('1.0', 'end')
        self.e5.delete('1.0', 'end')
    # function to show all recipes

    def show_all_recipes(self):
        self.list_box.delete(0, END)
        for recipe_name in self.recipe_book.recipes.keys():
            self.list_box.insert(END, recipe_name)

    # function to clear text
    def clear_box(self):
        self.e1.delete('1.0', 'end')
        self.e2.delete('1.0', 'end')
        self.e3.delete('1.0', 'end')
        self.e4.delete('1.0', 'end')
        self.e5.delete('1.0', 'end')

    # function to load a recipe for editing
    def load_recipe(self, event=None):
        selected_name = self.list_box.get(self.list_box.curselection())
        recipe = self.recipe_book.get_recipe(selected_name)[0]
        self.e1.delete('1.0', 'end')
        self.e2.delete('1.0', 'end')
        self.e3.delete('1.0', 'end')
        self.e4.delete('1.0', 'end')
        self.e5.delete('1.0', 'end')
        self.e1.insert('end', recipe.name)
        self.e2.insert('end', ', '.join(recipe.ingredients))
        self.e3.insert('end', recipe.instructions)
        self.e4.insert('end', recipe.cookingTime)
        self.e5.insert('end', recipe.dietaryInfo)

    # function to update recipes from amended text

    def update_recipe(self):
        name = self.e1.get('1.0', 'end').strip()
        ingredients = self.e2.get('1.0', 'end').strip().split(',')
        instructions = self.e3.get('1.0', 'end').strip()
        cookingTime = self.e4.get('1.0', 'end').strip()
        dietaryInfo = self.e5.get('1.0', 'end').strip()
        if name in self.recipe_book.recipes:
            self.recipe_book.create_recipe(
                name, ingredients, instructions, cookingTime, dietaryInfo)
            self.show_all_recipes()
            messagebox.showinfo("Recipe Book", "Recipe updated successfully!")
        else:
            messagebox.showinfo("Recipe Book", "Recipe not found.")

    # function to delete recipes after selected
    def delete_recipe(self):
        name = self.e1.get('1.0', 'end').strip()
        if name in self.recipe_book.recipes:
            self.recipe_book.delete_recipe(name)
            self.show_all_recipes()
            messagebox.showinfo("Recipe Book", "Recipe deleted successfully!")
            self.clear_box()
        else:
            messagebox.showinfo("Recipe Book", "Recipe not found.")

    # function to show  vegetarian recipes

    def show_veg_recipe(self):
        self.list_box.delete(0, END)
        for recipe_name, recipe in self.recipe_book.recipes.items():
            if "vegetarian" in recipe.dietaryInfo.lower():
                self.list_box.insert(END, recipe_name)

    # function to show  vegan recipes

    def show_vegan_recipe(self):
        self.list_box.delete(0, END)
        for recipe_name, recipe in self.recipe_book.recipes.items():
            if "vegan" in recipe.dietaryInfo.lower():
                self.list_box.insert(END, recipe_name)

    # function to show  all recipes

    def show_recipe(self):
        self.list_box.delete(0, END)
        for recipe_name, recipe in self.recipe_book.recipes.items():
            self.list_box.insert(END, recipe_name)


def main():
    root = Tk()
    app = RecipeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
