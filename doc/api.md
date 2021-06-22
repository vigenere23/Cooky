### return all users
`GET /users`

### return user account
`GET /users/<id>/account`


### return user by id
`GET /users/<id>`

### return all recipes from user id
`GET /users/<id>/recipes`

### return liked recipes from user id
`GET /users/<id>/likes`

### return profile from user id
`GET /users/<id>/profile`

### return address from user id
`GET /users/<id>/address`

### return all cart from user id
`GET /users/<id>/cart`

### return all recipes
`GET /recipes`

### return recipe from recipe id
`GET /recipes/<id>`

### return recipe from recipe name
`GET /recipes/name/<name>`

### return all ingredients from recipe id
`GET /recipes/<id>/ingredients`

### return all ingredients
`GET /ingredients`

### return ingredient by name
`GET /ingredients/<name>`

### return all carts
`GET /cart`

### return cart items from the cart id
`GET /cart/<id>/cartItems`

### return the command from the cart id
`GET /cart/<id>/command`

### return new command from the cart id
`Post /cart/<id>/command` 

### return the new userId and userName if created
### body : {username: <username>}
`Post /users`



#### return new command
`Post /cart/<cart_id>/command`

### return new cartItem
### body : {
###   id_Address: <id_Address>,
###   firstName: <firstName>,
###   lastName: <lastName>,
###   email: <email>,
###   password: <password>
###}
### Note : create new account
`Post /users/<id>/account`

### return new address
### body : {
###   number: <number>,
###   apartment: <apartment>,
###   street: <street>,
###   city: <city>,
###   country: <country>
###}
`Post /address`

### return new cartItem
### body : {
###   id_Ingredient: <id_Ingredient>,
###   subCost: <subCost>
###}
### Note : always add one item and add to current Cart
`Post /cart/<id>/cartItems`

### return new likeRecipe
### body : {
###   id_User: <id_User>
###}
### Note : always add to current recipe
`Post /recipes/<id_recipe>/like`

### return new ratingRecipe
### body : {
###   id_User: <id_User>,
###   value: <value>
###}
### Note : always add to current recipe
`Post /recipes/<id_recipe>/rate`

### return new comment
### body : {
###   id_User: <id_User>,
###   text: <text>
###}
### Note : always add to current recipe
`Post /recipes/<id_recipe>/comment`

### return new recipe
### body : {
###   id_User: <id_User>,
###   name: <name>,
###   directives: <directives>,
###   ingredients: {
###      "id_Ingredient": [<firstIngredient>, <secondIngredient>, ..., <lastIngredient>],
###      "id_QuantityUnit": [<firstQuantityUnit>, <secondQuantityUnit>, ..., <lastQuantityUnit>],
###      "totalQuantity": [<firstTotalQuantity>, <secondTotalQuantity>, ..., <lastTotalQuantity>]
###   }
###}
### Note: always a string
`Post /recipes`


### body : {
###    "id_Ingredient": <id_Ingredient>
###}
### Note: delete ingredient from current cart
`Delete /cart/<id_cart>/cartItems/<id_ingredient>/ingredient`


### Note: delete recipe
`Delete /recipes/<id_recipe>`

### body: {
### "firstName": <firstName>    
###}
`PUT /users/<id_User>/firstName`

### body: {
### "lastName": <lastName>    
###}
`PUT /users/<id_User>/lastName`

### body: {
### "email": <email>    
###}
`PUT /users/<id_User>/email`

### body: {
### "password": <password>    
###}
`PUT /users/<id_User>/password`

### body: {
### "username": <newUsername>    
###}
`PUT /users/<id_User>`

### body : {
###   "name": <name>,
###}
### Note: modify name
`Put /recipes/<id_recipe>/name`

### body : {
###   "directives": <directives>,
###}
### Note: modify directives
`Put /recipes/<id_recipe>/directives`

### body : {
###     "id_Ingredient": <id_Ingredient>,
###     "totalQuantity": <totalQuantity>
###}
### Note: modify ingredientQuantity from recipe
`Put /recipes/<id_recipe>/ingredientQuantity`

### body : {
###    "multiplier": <multiplier>
###}
### Note: modify the quantity from an ingredient in the cart
`Put /cart/<id_cart>/cartItems/<id_Ingredient>/ingredient`


