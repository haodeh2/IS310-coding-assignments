from rich.console import Console
from rich.table import Table
from pathlib import Path

console = Console()


##giving an example of what we're looking for
console.print("Here is some initial cultural dish data:", style="bold cyan")

table = Table(title="Cultural Dishes")
table.add_column("Culture", style="cyan")
table.add_column("Dish Type", style="magenta")
table.add_column("Food Name", style="green")

table.add_row("Palestinian", "Dessert", "Kunafa")
table.add_row("Mexican", "Main Course", "Tacos al Pastor")
table.add_row("Japanese", "Main Course", "Sushi")

console.print(table)


#prompting user to enter food

dishes = []

while True:
    console.print("\nEnter your own cultural dish data:", style="bold yellow")

    culture = input("Enter culture: ")
    dish_type = input("Enter dish type: ")
    food_name = input("Enter food name: ")

    console.print("\nYou entered:", style="bold green")
    console.print(f"Culture: {culture}")
    console.print(f"Dish Type: {dish_type}")
    console.print(f"Food Name: {food_name}")

    confirmation = input("Is this correct? (yes/no): ")

    if confirmation.lower() == "yes":
        dishes.append(f"{culture}, {dish_type}, {food_name}")
        console.print("Dish saved!", style="bold green")

        another = input("Would you like to add another dish? (yes/no): ")

        if another.lower() != "yes":
            break

    else:
        console.print("Please re-enter your information.", style="bold red")

file_path = Path("cultural_dishes.txt")

with open(file_path, "w") as file:
    for dish in dishes:
        file.write(dish + "\n")

console.print("\nYour data has been saved!", style="bold blue")
console.print(f"File location: {file_path.resolve()}")