"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he
is not good in maths. Can you help him to find out, how many cakes he could bake
considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients
(also an object) and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar
are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


def cakes(recipe, available):
    # Initialize the minimum cakes to a large number
    min_cakes = float('inf')

    # Loop through each ingredient in the recipe
    for ingredient in recipe:
        # Check if the ingredient is available
        if ingredient in available:
            # Calculate the number of cakes that can be made with the available ingredient
            num_cakes = available[ingredient] // recipe[ingredient]
        else:
            # If the ingredient is not available, no cakes can be made
            num_cakes = 0

        # Update the minimum cakes
        min_cakes = min(min_cakes, num_cakes)

    return min_cakes


# Example usage:
print(
    cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))  # Output: 2
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
            {'sugar': 500, 'flour': 2000, 'milk': 2000}))  # Output: 0
