from models import Recipes

def populate_data(db):
    # create sample recipes
    breakfast_recipe = Recipes(name='Eggs Benedict', category='Breakfast',
                              ingredients='eggs, English muffins, Canadian bacon, hollandaise sauce',
                              instructions='1. Toast the muffins. 2. Fry the bacon. 3. Poach the eggs. 4. Make the sauce. 5. Assemble the ingredients.')
    breakfast_recipe = Recipes(name ='Rice porridge with bread', category = 'Breakfast', 
                               ingredients = '1 cup rice, 5 cups water, salt (to taste), 1 pinch nutmeg, sugar/honey, evaporated milk', 
                               instructions = '1. Wash the rice until the water is clear, then drain. 2. Place the rice in a bowl and add 5 cups of water. 3. Cook the rice until tender for about 15 minutes. Use more water, if necessary to obtain a soft and sticky rice. 4. Add a pinch of salt. 5. Using the flat side of a wooden spoon, crush the rice until it is soft and flattens. 6. Add more water to soften to the desired thickness and consistency. 7. Serve the hot rice water with a pinch of nutmeg, evaporated milk, sugar/honey, and add toasted nuts, coconut flakes or other ingredients of your choice')
    breakfast_recipe = Recipes (name = 'Akara and pap', category = 'Breakfast', 
                                ingredients = '2 cups of beans, 1/2 small onions, 1 scotch bonnet, salt, vegetable oil', 
                                instructions = '1. Pick through the beans. 2. Wash and remove the beans coat by hand, using a blender or a food processor. 3. Grind beans to a very smooth paste using a blender or commercial mill, adding just enought water to et the blender blades moving. 4. Pour beans into a bowl and with a wooden spoon, stir vigorously until light, fluffy and doubled in size. You can also use a mortar and pestle, an electric whisk or food processor. This is considered a very important step. 5. Very finely chop onions and scotch bonnet adn set aside. 6. Place a frying pan over medium heat and add enough vegetable oil for deep frying. 7. Line a plate with kitchen napkins and set aside. 8. Add oni0ons, pepper and some salt to your beans paste, stir very well and if you can, taste a tiny bit for salt content. 9. When the oil is hot, use a tablespoon or your hand and spoon your batter into the hot oil. 10. Fry on one side then flip your Akara to fy the other side. 11. Drain into the lined plate. 12. Serve your akara with pap or semolina')
                               

    lunch_recipe = Recipes(name='BLT Sandwich', category='Lunch',
                          ingredients='bacon, lettuce, tomato, mayonnaise, bread',
                          instructions='1. Fry the bacon. 2. Toast the bread. 3. Assemble the sandwich.')
    
    lunch_recipe = Recipes (name = 'Eba and Egusi', category = 'lunch', 
                           ingredients = '1 cup blended onions (about 3-5 and fresh chillies, to taste), 4 cups egusi (melon seeds, ground or milled), half cup of palm oil, 2 teaspoons fresh Une (iru, locust beans) salt, ground crayfish, 7-8 cups stock, cooked meat and fish, 2 cups cut pumpkin leaves, 1 cup cut waterleaf, 3 tablespoons bitter leaf',
                           instructions  = 'Preparing the soup:, 1. Prepare the egusi paste. 2. Blend egusi seeds and onion mixture and set aside. 3. In a large pot, heat the palm oil on medium for a minute and the add the une. 4 Slowly add teh stock ad set on low heat to simmer. 5. Scoop teaspoon sized balls of the egusi paste mixture into the stock and be sure to keep ball shape. 6. Leave to simmer for 20 - 30 minutes so teh balls cook through. 7. Add the meat and fish and other bits which you will like to use. 8. Add cut up pumpkin leaves. 9. Add the waterleaf. 10. Stir and put a lid on the pot and allow to cook for 7 -10 minutes till the leaves wilt. 11. Stir and check for seasoning and adjust accordingly. Prepare the Eba: 1. Pour your gari (cassava flakes) into a hot boiling water. 2. add some salt to taste. 3. Keep stirring into a pulp. 4. Roll into a ball and enjoy your delicacy with your soup. ')
    dinner_recipe = Recipes(name='Spaghetti Bolognese', category='Dinner',
                           ingredients='spaghetti, ground beef, onion, garlic, tomato sauce, red wine, Parmesan cheese',
                           instructions='1. Cook the spaghetti. 2. Brown the beef. 3. Add the onion and garlic. 4. Add the tomato sauce and wine. 5. Simmer for 30 minutes. 6. Serve over spaghetti with Parmesan cheese.')
    
    dinner_recipe = Recipes (name = 'Jollof rice with plantain', category = 'dinner',
                             ingredients = '400ml passata, 3 tbsp tomato puree, 2 fresh red scotch bonnet chillies, 2 chopped onions, 2 chopped red peppers, 8 garlic cloves, 1 tbsp fresh thyme leaves, 2 tsp ground coriander, 1/2 tsp sweet smoked paprika, 50ml oz olive oil, 150g cherry tomatoes, 800ml pints chicken stock or vegetable stock, 2 bay leaves, 500g long-grain rice, 2 tbsp sunflower oil, 2 ripe plantains, small handful of roughly chopped coriander leaves, sea salt, freshly ground black pepper, and green salad',
                             instructions = '1. Put the passata, tomato puree, chillies, onions, peppers, garlic rosemary, thyme, ground coriander and paprika in a blender or food processor and blend until smooth. 2. Heat the olive oil in a large saucepan over a medium heat, add the cherry tomatoes and the blended tomato sauce. Bring to a boil and reduce the heat slightly and simmer for 5 minutes, stirring occasionally. 3. Add the stock, bay leaves, rice, one half teaspoons salt and a large pinch of black pepper, stir to compbine and bring to a boil and reduce the heat to simmer for 10 - 12 minutes while stirring frequently to prevent the rice from sticking together. Turn off the heat, cover the lid and leave to steam for 15 minutes. 4. Meanwhile, heat the sunflower oil in a frying pan over a medium heat, fry the sliced plantain for a few minutes on each side until golden and tender. 5. Spoon the jollof rice onto warmed plates and add the plantain on teh side. Garnish with the chipped coriander and serve with a green salad alongside. ')

    dessert_recipe = Recipes(name='Chocolate Cake', category ='Dessert',
                            ingredients='flour, sugar, cocoa powder, baking powder, eggs, milk, vegetable oil, vanilla extract',
                            instructions='1. Preheat the oven. 2. Mix the dry ingredients. 3. Beat the eggs with the milk, oil, and vanilla. 4. Combine the wet and dry ingredients. 5. Bake for 30 minutes. 6. Cool and serve.')

    # add the recipes to the database
    db.session.add(breakfast_recipe)
    db.session.add(lunch_recipe)
    db.session.add(dinner_recipe)
    db.session.add(dessert_recipe)
    db.session.commit()
    
