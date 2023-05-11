from models import Recipes
from app import db

def clear_database():
    db.session.query(Recipes).delete()
    db.session.commit()

def add_recipe(db, name, category, ingredients, instructions):
    # Check if recipe already exists in database
    recipe = Recipes.query.filter_by(name=name).first()
    if recipe:
        # Delete existing recipe and related data from the database
        db.session.delete(recipe)

    # Delete all related data that matches the existing recipe name
    Recipes.query.filter_by(name=name).delete()

    # Add new recipe to database
    new_recipe = Recipes(name=name, category=category, ingredients=ingredients, instructions=instructions)
    db.session.add(new_recipe)
    db.session.commit()



def populate_data(db):
    # create sample recipes
    add_recipe(db,'Eggs Benedict', 
                  'Breakfast',
                  'eggs, English muffins, Canadian bacon, hollandaise sauce',
                  '1. Toast the muffins. 2. Fry the bacon. 3. Poach the eggs. 4. Make the sauce. 5. Assemble the ingredients.')
    add_recipe(db, 'Moi-moi',
                    'Breakfast',
                    'black-eyed peas or honey beans also known as Ewa oloyin, pepers, onions, crayfish, vegetable oil/palm oil, chicken bouillon cubes, fish, hard boiled eggs, boiled beef liver, salt.',
                    '1. Soak the beans for about 10 to 15 minutes, drain and pour the soaked beans into the food processor, pulse a couple of times to remove the skin and pour the beans into a large bowl. Add enough water to cover the beans and swirl around till the skin flaots, then pour off the skin. Repeat process a couple of times until all the skin comes off. 2. Sieve the skin of the beans out after peeling and wash the beans to sieve out the skin until you get clean beans. The skin will float and the seeds will sink to the bottom of the bowl. You can the soak the beans for 10 minutes more to make them softer. 3. Blend the beans with other ingredients by adding the beans , pepper, onions, bouillon cubes, salt and crafish into the blender, then add some water to blend. 4. Pour the batter into a bowl and mix with groundnut oil. 5. Add fish chunks or liver and add boiled fish already cut into chunks or pour liver cut into small pieces as you keep mixing. 6. Prepare the bowls and portion the batter into the bowls and add boiled egg on top of the batter. 7. Put the pot on the stove and add boiled water, then arrange the moi moi in the pot and cover. 8. Allow it to steam for 45 minutes while topping up the water as it dries up in the pot. Carefully remove the moi moi from the plate and enjoy.')  
    add_recipe (db, 'Rice porridge with bread', 
                    'Breakfast', 
                    '1 cup rice, 5 cups water, salt (to taste), 1 pinch nutmeg, sugar/honey, evaporated milk', 
                    '1. Wash the rice until the water is clear, then drain. 2. Place the rice in a bowl and add 5 cups of water. 3. Cook the rice until tender for about 15 minutes. Use more water, if necessary to obtain a soft and sticky rice. 4. Add a pinch of salt. 5. Using the flat side of a wooden spoon, crush the rice until it is soft and flattens. 6. Add more water to soften to the desired thickness and consistency. 7. Serve the hot rice water with a pinch of nutmeg, evaporated milk, sugar/honey, and add toasted nuts, coconut flakes or other ingredients of your choice')
    add_recipe (db,'Akara and pap',
                    'Breakfast', 
                    '2 cups of beans, 1/2 small onions, 1 scotch bonnet, salt, vegetable oil', 
                    '1. Pick through the beans. 2. Wash and remove the beans coat by hand, using a blender or a food processor. 3. Grind beans to a very smooth paste using a blender or commercial mill, adding just enough water to et the blender blades moving. 4. Pour beans into a bowl and with a wooden spoon, stir vigorously until light, fluffy and doubled in size. You can also use a mortar and pestle, an electric whisk or food processor. This is considered a very important step. 5. Very finely chop onions and scotch bonnet adn set aside. 6. Place a frying pan over medium heat and add enough vegetable oil for deep frying. 7. Line a plate with kitchen napkins and set aside. 8. Add oni0ons, pepper and some salt to your beans paste, stir very well and if you can, taste a tiny bit for salt content. 9. When the oil is hot, use a tablespoon or your hand and spoon your batter into the hot oil. 10. Fry on one side then flip your Akara to fy the other side. 11. Drain into the lined plate. 12. Serve your akara with pap or semolina')
    add_recipe (db,'Hausa kooko', 
                    'Breakfast',
                    'millet, ground dried pepper, ginger, cloves, 1 tin milk, salt, sugar',
                    '1. Wash off the water used to soak the millet. 2. Soak the cloves in water for about 10 minutes. 3. Wash and clean ginger and add to the millet. 4. Add the cloves to the millet too and pour the mixture into a blender. 5. Add a small pinch of salt. 6. Blend till you obtain a smooth consistency, alternatively you can take the mixture to the mill for blending. 7. Strain in a fine strainer. 8. Blend the chaff and strain again. 9. Heat water in a saucepan or cooking pot under medium heat. 10. Set some of the boiled water aside. 11. Pour the desired about of the blended content into the boiling water and stir till the color changes to dark brown. 12. You can add some of the water you set aside to dilute if it is thick. 13. Keep adding some of the blended mixture and stir together with the wooden spatula. 14. Allow it to boil for few minutes and pu tthe fire off. 15. Add milk and sugar to taste. ')
    add_recipe(db, 'fufu and light soup', 
                    'lunch',
                    'fresh tomatoes, meat/fish/chicken/lamb according to preference, tomato puree, chili peppers, onion, salt, seasoning cube and spice, bay leaf, ginger and garlic, 4 pieces of okro, fresh cassava, unripe plantain',
                    '1. We start off by preparign the soup, first of all clean your meat/fish/chicken/lamb in clean water and set aside. Thereafter, wash the meat and equally keep it aside. 2. Secondly, blend your ginger, garlic, onion, seasoning cube, salt, and spices then scoop some quantity into the meat/fish/chicken/lamb to marinate and set aside. 3. Add the tomato puree, salt, bay leaf, with more water, cover and cook for about 10 minutes. 4. Wash your tomatoes, onions and pepper. 5. Place fresh tomatoes, onions, and pepper into a clean pot and pour 1 cup of water into the pot and bring to boil. 6. Remove the fresh tomatoes, pepper and onions from the pot and blend. Ensure you dont discard the boiled water from the tomatoes, rather use it to blend the tomatoes; or pour into the meat and add more water. 7. Bring the soup to a simmer over low heat for like 15 minutes then clean the okra/okro and add into the cooking pot, cover and cook till done. 8. Once the soup is done, peel the skin of your cassava tuber and plantains then boil fo rabout 25 - 30 minutes till tender. 9. Use the mortar and pestle which is the major instrument for local pounding, or use a yam pounder machine to pound it. 10. Start with the plantain, thereafter add the cassava, sprinkle some water as you pound for easy pounding until a smooth paste is achieved. Your smooth fufu is ready to be served with the delicious soup' )
    add_recipe (db, 'Ugali', 
                    'lunch',
                    '4 cups water, 1 tsp salt, 2 cups White cornmeal finely ground',
                    '1. Bring the water and salt to a boil in a heavy-bottomed saucepan. 2. Stir in the cornmeal slowly, letting it fall through the fingers of your hand. 3. Reduce heat to medium-low and continue stirring regularly, smashing any lumps with a spoon, until the mush pulls away from the sides of the pot and becomes very thick, about 10 minuts. 4. Remove from heat and allow to cool somewhat. 5. Place the Ugali into a large serving bowl. 6. Wet your hands with water, form into a ball, and serve with traditional vegetables, stew or kale')
    add_recipe (db, 'BLT Sandwich',
                    'Lunch',
                    'bacon, lettuce, tomato, mayonnaise, bread',
                    '1. Fry the bacon. 2. Toast the bread. 3. Assemble the sandwich.')
    
    add_recipe (db, 'Nyama Choma', 
                    'Lunch', 
                    '5.5 lbs goat meat, 10 cloves garlic, 1 bulb whole garlic cut across in the middle, 1 red or white large onion, 1 juiced lemon, 1/3 piece of ginger, 1/2 cup of extra virgin olive oil or preferred cooking oil, 1 tablespoon ground paprika, 1 tablespoon of salt, 2 stock cubes, 2 bird-eye de-seeded chillis, 3/4 tablespoon of salt, 6 sprigs of fresh rosemary',
                    '1. In a bowl, combine garlic, ginger, onion, lemon juice, olive oil, cumin, paprika, salt, stock cubes, rosemary, and chilli. Use a food processor or blender to save time but take care not to process it too much. it should still retain some texture. 2. Place the meat in a large bowl and toss it with half of the marinade. Set the otehr marinade aside to be used iin basting the nyama choma. 3. Use a knife to make slits of 2 inches or 5 cm apart on the goat leg and massage the marinade into the meat, making sure to als o cover the lsits. Cover the meat with aluminium foil and allow to marinate overnight or for at least 2 hours. 4. Remove the marnated goat meat from the fridge and allow it to come to room temperature for at least an hour before setting it on the barbecue. During this time, prepare your grill and set it to high and cover your grill with ashes if using a charcoal grill, to prevent it from getting too hot. 5. Grill the meat on high heat fo rapproximately 3 minutes on each side or until it attains a proper color then transfer to a triple layer of foil paper. 6. Place two sprigs of rosemary and the bulb of garlic on top of the goat leg. Cover the meat loosely with foil so it resembles a tent. 7. Set it ona baking tray or grilling rack and transfer to the barbecue grill the cover the lid, tryign to maintain the temperature at medium -low. Grill at medium -low for one and a half hours while turning it from time to time. 8. Once the time is up, mix the honoey with 2-3 tabespoons of hot water, uncover the meat and baste it withthe honey glaze. Continue to grill for a fruther 15  minutes or until the desired brownness has been achieved and the juices run clear, or it has an internal temperature of at least 150 -160 degrees F. 9. Once cooked, transfer the meat to a tray and allow it to rest fo r10 minutes before carving. 10. Serve nyama choma hot with ugali and Kachumbari')
    
    add_recipe (db,'Eba and Egusi', 
                    'lunch', 
                    '1 cup blended onions (about 3-5 and fresh chillies, to taste), 4 cups egusi (melon seeds, ground or milled), half cup of palm oil, 2 teaspoons fresh Une (iru, locust beans) salt, ground crayfish, 7-8 cups stock, cooked meat and fish, 2 cups cut pumpkin leaves, 1 cup cut waterleaf, 3 tablespoons bitter leaf',
                    'Preparing the soup:, 1. Prepare the egusi paste. 2. Blend egusi seeds and onion mixture and set aside. 3. In a large pot, heat the palm oil on medium for a minute and the add the une. 4 Slowly add teh stock ad set on low heat to simmer. 5. Scoop teaspoon sized balls of the egusi paste mixture into the stock and be sure to keep ball shape. 6. Leave to simmer for 20 - 30 minutes so teh balls cook through. 7. Add the meat and fish and other bits which you will like to use. 8. Add cut up pumpkin leaves. 9. Add the waterleaf. 10. Stir and put a lid on the pot and allow to cook for 7 -10 minutes till the leaves wilt. 11. Stir and check for seasoning and adjust accordingly. Prepare the Eba: 1. Pour your gari (cassava flakes) into a hot boiling water. 2. add some salt to taste. 3. Keep stirring into a pulp. 4. Roll into a ball and enjoy your delicacy with your soup. ')
    add_recipe (db, 'Spaghetti Bolognese', 
                    'Dinner',
                    'spaghetti, ground beef, onion, garlic, tomato sauce, red wine, Parmesan cheese',
                    '1. Cook the spaghetti. 2. Brown the beef. 3. Add the onion and garlic. 4. Add the tomato sauce and wine. 5. Simmer for 30 minutes. 6. Serve over spaghetti with Parmesan cheese.')
    add_recipe (db, 'bitter leaf soup', 
                    'lunch',
                    '3 pounds of assorted meat/chicken/beef/smoked fish or smoked turkey, 1/2 cup cooking oil, 1/2 large sliced onions, 2 sliced tomatoes, 2 teaspoons of minced garlic, 1/2 cup ground crayfish, 1/2 cup ground egusi, 2 cups washed bitterleaf, 3 cups fresh chopped spinach, 1 tablespoon buillon/maggi cubes, salt and pepper to taste',
                    '1. In a large pan, season meat or chicken with salt, maggi and onions and boil until tender depending on the choice of meat. You should have about 3 cups of stock from the meat and smoked fish. Reserve the rest or freeze it. 2. While chicken is cooking, slice tomatoes, onions and mince the garlic. 3. Heat the oil in a heavy saucepan over medium heat and add teh onions. Saute the onion until it is translucent. Season with salt, and pepper, to taste. 4. Stir in the tomatoes with their juices, garlic and crayfish. Add the chicken/beef pieces, then add ground egusi with chicken stock and bring to a simmer. 5. Add bitter leaf, followed by spinach and let it simmer for about 2 minutes. Serve warm with fufu or accompaniment of choice. ')
    add_recipe (db, 'Jollof rice with plantain', 
                    'dinner',
                    '400ml passata, 3 tbsp tomato puree, 2 fresh red scotch bonnet chillies, 2 chopped onions, 2 chopped red peppers, 8 garlic cloves, 1 tbsp fresh thyme leaves, 2 tsp ground coriander, 1/2 tsp sweet smoked paprika, 50ml oz olive oil, 150g cherry tomatoes, 800ml pints chicken stock or vegetable stock, 2 bay leaves, 500g long-grain rice, 2 tbsp sunflower oil, 2 ripe plantains, small handful of roughly chopped coriander leaves, sea salt, freshly ground black pepper, and green salad',
                    '1. Put the passata, tomato puree, chillies, onions, peppers, garlic rosemary, thyme, ground coriander and paprika in a blender or food processor and blend until smooth. 2. Heat the olive oil in a large saucepan over a medium heat, add the cherry tomatoes and the blended tomato sauce. Bring to a boil and reduce the heat slightly and simmer for 5 minutes, stirring occasionally. 3. Add the stock, bay leaves, rice, one half teaspoons salt and a large pinch of black pepper, stir to compbine and bring to a boil and reduce the heat to simmer for 10 - 12 minutes while stirring frequently to prevent the rice from sticking together. Turn off the heat, cover the lid and leave to steam for 15 minutes. 4. Meanwhile, heat the sunflower oil in a frying pan over a medium heat, fry the sliced plantain for a few minutes on each side until golden and tender. 5. Spoon the jollof rice onto warmed plates and add the plantain on teh side. Garnish with the chipped coriander and serve with a green salad alongside. ')
    add_recipe (db, 'Chocolate Cake',
                    'Dessert',
                    'flour, sugar, cocoa powder, baking powder, eggs, milk, vegetable oil, vanilla extract',
                    '1. Preheat the oven. 2. Mix the dry ingredients. 3. Beat the eggs with the milk, oil, and vanilla. 4. Combine the wet and dry ingredients. 5. Bake for 30 minutes. 6. Cool and serve.')
    
    add_recipe(db, 'Mandazi', 
                    'Dessert',
                    '3 cups self raising flour (plus more to dust),   3/4 cup sugar grated lemon rind or zest,   1/2 teaspoon cardomom (iliki), 1/4 teaspoon salt,   one and half cups warm water (use more or less, until you obtain a firm dough),   oil for fying',
                    '1. In a bowl, soft the self-raising flour sugar, cardamom, and salt. Add the grated lemon zest then make a well in the center to add the warm water. Add the water a little at a time and use your hands to knead until all the ingredients come together, and the dough is smooth, taking care not to overwork it. 2. Cover the bowl with saran wrap (cling film), or a slightly damp kitchen cloth and place it in a warm place in your kitchen, to rest for at least 20 minutes.  3. Once the dough has rested, transfer it to a floured rolling board or a clean kitchen countertop. Divide the dough into 4 portions, and roll each portion between the palms of your hands to form a ball. Roll out each ball of dough to a circle about 20cm in diameter and cut into 8 triangles. 4. Heat the oil in a large pot to 180 degrees celsius and fry each mandazi for 3 - 5 minutes on each side or until golden brown. Transfer them to a kitchen paper towel -lined bowl to drain excess oil. Serve your Kenyna mandazi with a cup of chai ,coffee or simply enjoy them as they are.  ')
    
    
