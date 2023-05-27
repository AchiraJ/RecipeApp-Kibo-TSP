from models import Recipes
from app import db

# def clear_database():
#     db.session.query(Recipes).delete()
#     db.session.commit()

def add_recipe(db, name,image_name, category, ingredients, instructions):
    # Check if recipe already exists in database
    recipe = Recipes.query.filter_by(name=name).first()
    if recipe:
        # Delete existing recipe and related data from the database
        db.session.delete(recipe)

    # Delete all related data that matches the existing recipe name
    Recipes.query.filter_by(name=name).delete()

    # Add new recipe to database
    new_recipe = Recipes(name=name, image_name = image_name,category=category, ingredients=ingredients, instructions=instructions)
    db.session.add(new_recipe)
    db.session.commit()



def populate_data(db):
    # create sample recipes
    add_recipe(db,'Eggs Benedict', 'img_eggs_benedict',
                  'Breakfast',
                  'eggs, English muffins, Canadian bacon, hollandaise sauce',
                  'Toast the muffins, Fry the bacon, Poach the eggs, Make the sauce, Assemble the ingredients')
    add_recipe(db, 'Moi-moi', 'img_moimoi',
                    'Breakfast',
                    'Black-eyed peas or honey beans also known as Ewa oloyin, pepers, onions, crayfish, vegetable oil/palm oil, chicken bouillon cubes, fish, hard boiled eggs, boiled beef liver, salt.',
                    'Soak the beans for about 10 to 15 minutes. Drain and pour the soaked beans into the food processor. Pulse a couple of times to remove the skin and pour the beans into a large bowl. Add enough water to cover the beans and swirl around till the skin flaots then pour off the skin. Repeat process a couple of times until all the skin comes off. Sieve the skin of the beans out after peeling and wash the beans to sieve out the skin until you get clean beans. The skin will float and the seeds will sink to the bottom of the bowl. You can the soak the beans for 10 minutes more to make them softer. Blend the beans with other ingredients by adding the beans , pepper, onions, bouillon cubes, salt and crafish into the blender, then add some water to blend. Pour the batter into a bowl and mix with groundnut oil. Add fish chunks or liver and add boiled fish already cut into chunks or pour liver cut into small pieces as you keep mixing. Prepare the bowls and portion the batter into the bowls and add boiled egg on top of the batter. Put the pot on the stove and add boiled water, then arrange the moi moi in the pot and cover. Allow it to steam for 45 minutes while topping up the water as it dries up in the pot. Carefully remove the moi moi from the plate and enjoy.')  
    add_recipe (db, 'Rice porridge with bread', 'img_riceporridge',
                    'Breakfast', 
                    '1 cup rice, 5 cups water, salt (to taste), 1 pinch nutmeg, sugar/honey, evaporated milk', 
                    'Wash the rice until the water is clear, then drain. Place the rice in a bowl and add 5 cups of water. Cook the rice until tender for about 15 minutes. Use more water, if necessary to obtain a soft and sticky rice. Add a pinch of salt. Using the flat side of a wooden spoon, crush the rice until it is soft and flattens. Add more water to soften to the desired thickness and consistency. Serve the hot rice water with a pinch of nutmeg, evaporated milk, sugar/honey, and add toasted nuts, coconut flakes or other ingredients of your choice')
    add_recipe (db,'Akara and pap', 'img_akara',
                    'Breakfast', 
                    '2 cups of beans, 1/2 small onions, 1 scotch bonnet, salt, vegetable oil', 
                    'Pick through the beans. Wash and remove the beans coat by hand, using a blender or a food processor. Grind beans to a very smooth paste using a blender or commercial mill, adding just enough water to et the blender blades moving. Pour beans into a bowl and with a wooden spoon, stir vigorously until light, fluffy and doubled in size. You can also use a mortar and pestle, an electric whisk or food processor. This is considered a very important step. Very finely chop onions and scotch bonnet adn set aside. Place a frying pan over medium heat and add enough vegetable oil for deep frying. Line a plate with kitchen napkins and set aside. Add onions, pepper and some salt to your beans paste, stir very well and if you can, taste a tiny bit for salt content. When the oil is hot, use a tablespoon or your hand and spoon your batter into the hot oil. Fry on one side then flip your Akara to fy the other side. Drain into the lined plate. Serve your akara with pap or semolina')
    add_recipe (db,'Hausa kooko', 'img_hausa_koko',
                    'Breakfast',
                    'millet, ground dried pepper, ginger, cloves, 1 tin milk, salt, sugar',
                    'Wash off the water used to soak the millet. Soak the cloves in water for about 10 minutes. Wash and clean ginger and add to the millet. Add the cloves to the millet too and pour the mixture into a blender. Add a small pinch of salt. Blend till you obtain a smooth consistency, alternatively you can take the mixture to the mill for blending. Strain in a fine strainer. Blend the chaff and strain again. Heat water in a saucepan or cooking pot under medium heat. Set some of the boiled water aside. Pour the desired about of the blended content into the boiling water and stir till the color changes to dark brown. You can add some of the water you set aside to dilute if it is thick. Keep adding some of the blended mixture and stir together with the wooden spatula. Allow it to boil for few minutes and pu tthe fire off. Add milk and sugar to taste. ')
    add_recipe(db, 'Fufu and light soup', 'img_fufu_soup',
                    'Lunch',
                    'fresh tomatoes, meat/fish/chicken/lamb according to preference, tomato puree, chili peppers, onion, salt, seasoning cube and spice, bay leaf, ginger and garlic, 4 pieces of okro, fresh cassava, unripe plantain',
                    'We start off by preparign the soup, first of all clean your meat/fish/chicken/lamb in clean water and set aside; Thereafter, wash the meat and equally keep it aside. Secondly, blend your ginger, garlic, onion, seasoning cube, salt, and spices then scoop some quantity into the meat/fish/chicken/lamb to marinate and set aside. Add the tomato puree, salt, bay leaf, with more water, cover and cook for about 10 minutes. Wash your tomatoes, onions and pepper. Place fresh tomatoes, onions, and pepper into a clean pot and pour 1 cup of water into the pot and bring to boil. Remove the fresh tomatoes, pepper and onions from the pot and blend. Ensure you dont discard the boiled water from the tomatoes, rather use it to blend the tomatoes; or pour into the meat and add more water. Bring the soup to a simmer over low heat for like 15 minutes then clean the okra/okro and add into the cooking pot, cover and cook till done. Once the soup is done, peel the skin of your cassava tuber and plantains then boil fo rabout 25 - 30 minutes till tender. Use the mortar and pestle which is the major instrument for local pounding, or use a yam pounder machine to pound it. Start with the plantain, thereafter add the cassava, sprinkle some water as you pound for easy pounding until a smooth paste is achieved. Your smooth fufu is ready to be served with the delicious soup' )
    add_recipe (db, 'Ugali', 'img_ugali',
                    'Lunch',
                    '4 cups water, 1 tsp salt, 2 cups White cornmeal finely ground',
                    'Bring the water and salt to a boil in a heavy-bottomed saucepan. Stir in the cornmeal slowly, letting it fall through the fingers of your hand. Reduce heat to medium-low and continue stirring regularly, smashing any lumps with a spoon, until the mush pulls away from the sides of the pot and becomes very thick, about 10 minuts. Remove from heat and allow to cool somewhat. Place the Ugali into a large serving bowl. Wet your hands with water, form into a ball, and serve with traditional vegetables, stew or kale')
    add_recipe (db, 'BLT Sandwich', 'img_blt_sandwich',
                    'Lunch',
                    'Bacon, lettuce, tomato, mayonnaise, bread',
                    'Fry the bacon. Toast the bread. Assemble the sandwich.')
    
    add_recipe (db, 'Nyama Choma', 'img_nyamchom',
                    'Lunch', 
                    '5.5 lbs goat meat, 10 cloves garlic, 1 bulb whole garlic cut across in the middle, 1 red or white large onion, 1 juiced lemon, 1/3 piece of ginger, 1/2 cup of extra virgin olive oil or preferred cooking oil, 1 tablespoon ground paprika, 1 tablespoon of salt, 2 stock cubes, 2 bird-eye de-seeded chillis, 3/4 tablespoon of salt, 6 sprigs of fresh rosemary',
                    'In a bowl, combine garlic, ginger, onion, lemon juice, olive oil, cumin, paprika, salt, stock cubes, rosemary, and chilli. Use a food processor or blender to save time but take care not to process it too much. it should still retain some texture. Place the meat in a large bowl and toss it with half of the marinade. Set the otehr marinade aside to be used iin basting the nyama choma. Use a knife to make slits of 2 inches or 5 cm apart on the goat leg and massage the marinade into the meat, making sure to als o cover the lsits. Cover the meat with aluminium foil and allow to marinate overnight or for at least 2 hours. Remove the marnated goat meat from the fridge and allow it to come to room temperature for at least an hour before setting it on the barbecue. During this time, prepare your grill and set it to high and cover your grill with ashes if using a charcoal grill, to prevent it from getting too hot. Grill the meat on high heat fo rapproximately 3 minutes on each side or until it attains a proper color then transfer to a triple layer of foil paper. Place two sprigs of rosemary and the bulb of garlic on top of the goat leg. Cover the meat loosely with foil so it resembles a tent. Set it ona baking tray or grilling rack and transfer to the barbecue grill the cover the lid, tryign to maintain the temperature at medium -low. Grill at medium -low for one and a half hours while turning it from time to time. Once the time is up, mix the honoey with 2-3 tabespoons of hot water, uncover the meat and baste it withthe honey glaze. Continue to grill for a fruther 15  minutes or until the desired brownness has been achieved and the juices run clear, or it has an internal temperature of at least 150 -160 degrees F. Once cooked, transfer the meat to a tray and allow it to rest fo r10 minutes before carving. Serve nyama choma hot with ugali and Kachumbari')
    
    add_recipe (db,'Eba and Egusi', 'img_ebagusi',
                    'Lunch', 
                    '1 cup blended onions (about 3-5 and fresh chillies, to taste), 4 cups egusi (melon seeds, ground or milled), half cup of palm oil, 2 teaspoons fresh Une (iru, locust beans) salt, ground crayfish, 7-8 cups stock, cooked meat and fish, 2 cups cut pumpkin leaves, 1 cup cut waterleaf, 3 tablespoons bitter leaf',
                    ' Prepare the egusi paste. Blend egusi seeds and onion mixture and set aside. In a large pot, heat the palm oil on medium for a minute and the add the une. Slowly add the stock ad set on low heat to simmer. Scoop teaspoon sized balls of the egusi paste mixture into the stock and be sure to keep ball shape. Leave to simmer for 20 - 30 minutes so teh balls cook through. Add the meat and fish and other bits which you will like to use. Add cut up pumpkin leaves. Add the waterleaf. Stir and put a lid on the pot and allow to cook for 7 -10 minutes till the leaves wilt. Stir and check for seasoning and adjust accordingly. Pour your gari (cassava flakes) into a hot boiling water. Add some salt to taste. Keep stirring into a pulp. Roll into a ball and enjoy your delicacy with your soup. ')
    add_recipe (db, 'Spaghetti Bolognese', 'img_spaghetti',
                    'Dinner',
                    'spaghetti, ground beef, onion, garlic, tomato sauce, red wine, Parmesan cheese',
                    'Cook the spaghetti. Brown the beef. Add the onion and garlic. Add the tomato sauce and wine. Simmer for 30 minutes. Serve over spaghetti with Parmesan cheese.')
    add_recipe (db, 'Bitter leaf soup', 'img_bitter_soup',
                    'Lunch',
                    '3 pounds of assorted meat/chicken/beef/smoked fish or smoked turkey, 1/2 cup cooking oil, 1/2 large sliced onions, 2 sliced tomatoes, 2 teaspoons of minced garlic, 1/2 cup ground crayfish, 1/2 cup ground egusi, 2 cups washed bitterleaf, 3 cups fresh chopped spinach, 1 tablespoon buillon/maggi cubes, salt and pepper to taste',
                    'In a large pan, season meat or chicken with salt, maggi and onions and boil until tender depending on the choice of meat. You should have about 3 cups of stock from the meat and smoked fish. Reserve the rest or freeze it. While chicken is cooking, slice tomatoes, onions and mince the garlic. Heat the oil in a heavy saucepan over medium heat and add teh onions. Saute the onion until it is translucent. Season with salt, and pepper, to taste. Stir in the tomatoes with their juices, garlic and crayfish. Add the chicken/beef pieces, then add ground egusi with chicken stock and bring to a simmer. Add bitter leaf, followed by spinach and let it simmer for about 2 minutes. Serve warm with fufu or accompaniment of choice. ')
    add_recipe (db, 'Jollof rice with plantain', 'img_jollof_rice',
                    'Dinner',
                    '400ml passata, 3 tbsp tomato puree, 2 fresh red scotch bonnet chillies, 2 chopped onions, 2 chopped red peppers, 8 garlic cloves, 1 tbsp fresh thyme leaves, 2 tsp ground coriander, 1/2 tsp sweet smoked paprika, 50ml oz olive oil, 150g cherry tomatoes, 800ml pints chicken stock or vegetable stock, 2 bay leaves, 500g long-grain rice, 2 tbsp sunflower oil, 2 ripe plantains, small handful of roughly chopped coriander leaves, sea salt, freshly ground black pepper, and green salad',
                    'Put the passata, tomato puree, chillies, onions, peppers, garlic rosemary, thyme, ground coriander and paprika in a blender or food processor and blend until smooth. Heat the olive oil in a large saucepan over a medium heat, add the cherry tomatoes and the blended tomato sauce. Bring to a boil and reduce the heat slightly and simmer for 5 minutes, stirring occasionally. Add the stock, bay leaves, rice, one half teaspoons salt and a large pinch of black pepper, stir to combine and bring to a boil and reduce the heat to simmer for 10 - 12 minutes while stirring frequently to prevent the rice from sticking together. Turn off the heat, cover the lid and leave to steam for 15 minutes. Meanwhile, heat the sunflower oil in a frying pan over a medium heat, fry the sliced plantain for a few minutes on each side until golden and tender. Spoon the jollof rice onto warmed plates and add the plantain on teh side. Garnish with the chipped coriander and serve with a green salad alongside. ')
    add_recipe (db, 'Chocolate Cake','img_choc_cake',
                    'Dessert',
                    'flour, sugar, cocoa powder, baking powder, eggs, milk, vegetable oil, vanilla extract',
                    'Preheat the oven. Mix the dry ingredients. Beat the eggs with the milk, oil, and vanilla. Combine the wet and dry ingredients. Bake for 30 minutes. Cool and serve.')
    
    add_recipe(db, 'Mandazi', 'img_mandazi',
                    'Dessert',
                    '3 cups self raising flour (plus more to dust),   3/4 cup sugar grated lemon rind or zest,   1/2 teaspoon cardomom (iliki), 1/4 teaspoon salt,   one and half cups warm water (use more or less, until you obtain a firm dough),   oil for fying',
                    'In a bowl, soft the self-raising flour sugar, cardamom, and salt. Add the grated lemon zest then make a well in the center to add the warm water. Add the water a little at a time and use your hands to knead until all the ingredients come together, and the dough is smooth, taking care not to overwork it. Cover the bowl with saran wrap (cling film), or a slightly damp kitchen cloth and place it in a warm place in your kitchen, to rest for at least 20 minutes. Once the dough has rested, transfer it to a floured rolling board or a clean kitchen countertop. Divide the dough into 4 portions, and roll each portion between the palms of your hands to form a ball. Roll out each ball of dough to a circle about 20cm in diameter and cut into 8 triangles. Heat the oil in a large pot to 180 degrees celsius and fry each mandazi for 3 - 5 minutes on each side or until golden brown. Transfer them to a kitchen paper towel -lined bowl to drain excess oil. Serve your Kenyan mandazi with a cup of chai ,coffee or simply enjoy them as they are.  ')
    
    
