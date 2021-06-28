import random
from datetime import datetime
from app.infra.db.daos.recipe import LikeRecipeDao, RecipeCommentDao, RecipeDao, RecipeRatingDao
from app.infra.db.models.recipe import RecipeIngredientModel, RecipeModel, LikeRecipeModel, CommentModel, RatingModel
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao
from app.infra.db.models.ingredient import IngredientModel
from app.infra.db.daos.user import UserDao, AddressDao, AccountDao
from app.infra.db.models.user import UserModel, AddressModel, AccountModel
from app.infra.db.daos.cart import CartDao, CartItemDao, CommandDao
from app.infra.db.models.cart import CartModel, CartItemModel, CommandModel

userDao = UserDao()
ingredientDao = IngredientDao()
cartItemDao = CartItemDao()
recipeDao = RecipeDao()
quantityUnitDao = QuantityUnitDao()
ratingDao = RecipeRatingDao()
commentDao = RecipeCommentDao()
likeRecipeDao = LikeRecipeDao()
adressDao = AddressDao()
accountDao = AccountDao()
commandDao = CommandDao()
cartDao = CartDao()

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi pulvinar pharetra bibendum. Ut eget risus nec risus finibus hendrerit in non tortor. Pellentesque maximus ligula et turpis faucibus cursus. Donec vel nunc metus. Quisque sagittis mattis dui vel varius. Aliquam iaculis interdum lacinia. Nam euismod lectus id maximus sodales. Nam id magna dictum, semper nisl vel, ornare ligula. Sed condimentum metus quis leo pharetra, quis semper urna aliquam. Fusce consectetur accumsan augue sit amet iaculis. Suspendisse volutpat urna vitae fermentum eleifend. Maecenas sapien leo, gravida vitae pellentesque quis, efficitur in erat. Maecenas elementum euismod hendrerit. Mauris sagittis massa a orci."
words = ["Hogym", "Celloggimbur", "Laglesgim", "Sylcyllis", "Morbir", "Limgem", "Silgimculnir", "Narmar", "Solgamberthi", "Cyllig", "Thalomorn", "Rluggum", "Ornbar", "Merhosyl", "Callisthunir", "Thaligber", "Limbarmar", "Lishalllumcal", "Berthe", "Hathulemhe", "Colmorhi", "Salthalegorn", "Birmircyl", "Bermor", "Morlag", "Barbirorn", "Burmir", "Humarhamur", "Leglam", "Hugimirn", "Berburthamur", "Lasloglum", "Gomlamthi", "Narmarborern", "Lomlos", "Urnlasho", "Hical", "Hisol", "Leshe", "Gumsalculsil", "Morcalsul", "Barlugha", "Salhu", "Celmorgember", "Byrhebyr", "Birhogim", "Helisloshi", "Syllas", "Gymcalhober", "Gimcullegirn", "Borlessil", "Thitha", "Cylcelnor", "Borbyrhulys", "Loglistha", "Silbartha", "Orncilbirgom", "Lasnormer", "Lumsolthalig", "Burlyscul", "Murgomhellhi", "Thatheluslag", "Lyshallluslam", "Mirborcil", "Nircalbur", "Barlugarn", "Gimcul", "Thulam", "Hecolha", "Ornmur", "Lamber", "Sulleshe", "Lomlember", "Loscal", "Calornthilog", "Limlesgam", "Thigomcul", "Laglyslomlis", "Erngomlig", "Gamlusmorcol", "Syllag", "Hothoirnlug", "Hesolmar", "Lugcul", "Thicolthu", "Narlescul", "Nirmersolurn", "Logcel", "Lasloglag", "Lessellamyrn", "Gymlys", "Thasal", "Silurnsellag", "Hallloslysbur", "Ligbir", "Burcylcel", "Narlisho" ,"Hosal","Liscal", "Sulbarmornar", "Tyfoxe", "Xusini", "Kidoxa", "Piphafy", "Chirra", "Rrobysu", "Jasu", "Quacy", "Laqui", "Nophe", "Mmyjyhe", "Quelli", "Jazo", "Mmichera", "Rroky", "Mmelli", "Girre", "Kibi", "Zafu", "Nowomi", "Dunummo", "Phasone", "Gipho", "Kyjado", "Senoze", "Gocahy", "Mmoha", "Mata", "Vupo", "Lochu", "Zeto", "Cycaci", "Llollace", "Cuphiwa", "Thexe", "Billu", "Matuko", "Rruxigu", "Bogu", "Vesi", "Wetu", "Jegi", "Gake", "Chullene", "Rruno", "Hyza", "Poru", "Nyxichi", "Fadylu", "Lajyse", "Phuxu", "Thehyko", "Quovavu", "Lleji", "Kynugy", "Mmyte", "Pakufa", "Sychecha", "Thine", "Sidemi", "Mmeka", "Jyfybo", "Mmuquoby", "Vuci", "Raci", "Zyhi", "Sujytho", "Cukemo", "Mixevo", "Thyxuwu", "Muphaba", "Pehide", "Thaserra", "Byjuwi", "Geka", "Zurruca", "Hymmy", "Thuju", "Rydu", "Jeduty", "Lluzali", "Rroce", "Sala", "Sipehu", "Pazasi", "Hagyga", "Nophy", "Rrammyca", "Kevygu", "Hellu", "Jimiru", "Llommiga", "Fasopy", "Navede", "Wireju", "Kotherru", "Cuphu", "Lloto", "Lledagy", "Syqua", "Zajerry", "Wipugo", "Sixare", "Gyka", "Bibowo", "Poje", "Mechiwi", "Juzuke", "Nyjige", "Zycu", "Govopy", "Nibo", "Tysy", "Viri", "Mmoxuby", "Boxemmi", "Xathe", "Mmocho", "Rycho", "Pijoly", "Mexo", "Thytha", "Gequo", "Rycypy", "Boquirri", "Zapu", "Gichu", "Rethu", "Gully", "Quoquafa", "Vozella", "Fibonu", "Dodyra", "Theky", "Sozawy", "Cehypy", "Rrotyhu", "Mowe", "Chusuny", "Pyru", "Dypu", "Juhuta", "Polo", "Phikotho", "Polymmo", "Hyse", "Suquajo", "Lletyjo", "Phata", "Fille", "Medy", "Cephellu", "Wogaha", "Quarrythy", "Mmanure", "Tumu", "Rothe", "Hapha", "Loxocho", "Coquawi", "Bonephe", "Suchu", "Mmiweso", "Mallyzy", "Wimma", "Rriwufi", "Nopho", "Pima", "Gyki"]
addr = ["St", "Ave", "Blvd", "Rd"]

def generateUsers():
    for i in range(100):
        userModel = UserModel(
            username=words[i],
        )
        userDao.save(userModel)

def generateIngredients():
    for i in range(100):
        ingredientModel = IngredientModel(
            id_IngredientType=random.randint(1, 13),
            id_QuantityUnit=random.randint(1, 13),
            name=words[i],
            baseCost=round(random.random() * 15, 2),
            baseQuantity=random.randint(1, 12)
        )
        ingredientDao.save(ingredientModel)

def generateCartItems():
    for i in range(1, 101):
        added_ingredients = []
        for _ in range(random.randint(5, 20)):
            ingredient_id = random.randint(1, 100)
            while ingredient_id in added_ingredients:
                ingredient_id = random.randint(1, 100)
            added_ingredients.append(ingredient_id)

            cartItemModel = CartItemModel(
                id_Ingredient=ingredient_id,
                id_Cart=i
            )
            cartItemDao.save(cartItemModel)

def generateRecipes():
    for i in range(100):
        ingredients = []
        ingredient_ids = []
        for _ in range(random.randint(5, 10)):
            ingredient_id = random.randint(1, 100)
            while ingredient_id in ingredient_ids:
                ingredient_id = random.randint(1, 100)
            ingredient_ids.append(ingredient_id)

            quantities = quantityUnitDao.getAllQuantityUnitsByIngredientId(ingredient_id)
            quantity_ids = [q.id for q in quantities]

            recipeIngredientModel = RecipeIngredientModel(
                id_Ingredient=ingredient_id,
                id_QuantityUnit=random.choice(quantity_ids),
                totalQuantity=random.randint(1, 10)
            )
            ingredients.append(recipeIngredientModel)

        recipeModel = RecipeModel(
            id_User=random.randint(1, 100),
            name=words[i],
            directives=lorem,
            description=lorem
        )
        recipeDao.save(recipeModel, ingredients)

def generateRatings():
    for i in range(1, 101):
        rated_recipes = []
        for _ in range(random.randint(0, 10)):
            recipe_id = random.randint(1, 100)
            while recipe_id in rated_recipes:
                recipe_id = random.randint(1, 100)
            rated_recipes.append(recipe_id)

            ratingModel = RatingModel(
                id_Recipe=recipe_id,
                id_User=i,
                value=random.randint(1, 5)
            )
            ratingDao.save(ratingModel)

def generateComments():
    for _ in range(100):
        commentModel = CommentModel(
            id_Recipe=random.randint(1, 100),
            id_User=random.randint(1, 100),
            text=lorem
        )
        commentDao.save(commentModel)

def generateLikes():
    for i in range(1, 101):
        added_recipes = []
        for _ in range(random.randint(0, 10)):
            recipe_id = random.randint(1, 100)
            while recipe_id in added_recipes:
                recipe_id = random.randint(1, 100)
            added_recipes.append(recipe_id)

            likeRecipeModel = LikeRecipeModel(
                id_Recipe=recipe_id,
                id_User=i
            )
            likeRecipeDao.save(likeRecipeModel)

def generateAdresses():
    for _ in range(100):
        apartment = None if (random.randint(1,4) % 2 == 0) else (random.randint(0, 1000))
        addressModel = AddressModel(
            number=random.randint(1, 99),
            apartment=apartment,
            street=random.choice(words) + " " + random.choice(addr),
            city=random.choice(words),
            country=random.choice(words)
        )
        adressDao.save(addressModel)

def generateAccounts():
    for i in range(1, 101):
        lastName = random.choice(words)
        firstName = random.choice(words)
        accountModel = AccountModel(
            id_User=i,
            id_Address=i,
            firstName=firstName,
            lastName=lastName,
            email=firstName + "." + lastName + "@gmail.com",
            password=random.choice(words)+random.choice(words)+random.choice(words)
        )
        accountDao.save(accountModel)

def generateCommands():
    for _ in range(100):
        cartModel = CartModel(id_User=random.randint(1, 100))
        cart = cartDao.save(cartModel)

        current_time = datetime.now()
        commandModel = CommandModel(
            id_Cart=cart.id,
            creationDate=current_time,
            arrivalDate=current_time
        )
        commandDao.save(commandModel)


if __name__ == "__main__":
    print(' - 1/10 generating users...')
    generateUsers()
    print(' - 2/10 generating ingredients...')
    generateIngredients()
    print(' - 3/10 generating cart items...')
    generateCartItems()
    print(' - 4/10 generating recipes...')
    generateRecipes()
    print(' - 5/10 generating ratings...')
    generateRatings()
    print(' - 6/10 generating likes...')
    generateLikes()
    print(' - 7/10 generating comments...')
    generateComments()
    print(' - 8/10 generating adresses...')
    generateAdresses()
    print(' - 9/10 generating accounts...')
    generateAccounts()
    print(' - 10/10 generating commands...')
    generateCommands()
