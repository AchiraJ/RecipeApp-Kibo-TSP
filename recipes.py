from models import Recipes

def populate_data(db):
    # create sample recipes
    breakfast_recipe = Recipes(name='Eggs Benedict', category='Breakfast',
                              ingredients='eggs, English muffins, Canadian bacon, hollandaise sauce',
                              instructions='1. Toast the muffins. 2. Fry the bacon. 3. Poach the eggs. 4. Make the sauce. 5. Assemble the ingredients.')
    lunch_recipe = Recipes(name='BLT Sandwich', category='Lunch',
                          ingredients='bacon, lettuce, tomato, mayonnaise, bread',
                          instructions='1. Fry the bacon. 2. Toast the bread. 3. Assemble the sandwich.')
    dinner_recipe = Recipes(name='Spaghetti Bolognese', category='Dinner',
                           ingredients='spaghetti, ground beef, onion, garlic, tomato sauce, red wine, Parmesan cheese',
                           instructions='1. Cook the spaghetti. 2. Brown the beef. 3. Add the onion and garlic. 4. Add the tomato sauce and wine. 5. Simmer for 30 minutes. 6. Serve over spaghetti with Parmesan cheese.')

    dessert_recipe = Recipes(name='Chocolate Cake', category ='Dessert',
                            ingredients='flour, sugar, cocoa powder, baking powder, eggs, milk, vegetable oil, vanilla extract',
                            instructions='1. Preheat the oven. 2. Mix the dry ingredients. 3. Beat the eggs with the milk, oil, and vanilla. 4. Combine the wet and dry ingredients. 5. Bake for 30 minutes. 6. Cool and serve.')

    # add the recipes to the database
    db.session.add(breakfast_recipe)
    db.session.add(lunch_recipe)
    db.session.add(dinner_recipe)
    db.session.add(dessert_recipe)
    db.session.commit()
    
