use projet;

ALTER TABLE `CartItem`
ADD CONSTRAINT UC_CartItem
UNIQUE (`id_Ingredient`, `id_Cart`);

ALTER TABLE `RecipeIngredient`
ADD CONSTRAINT UC_RecipeIngredient
UNIQUE (`id_Recipe`, `id_Ingredient`);

ALTER TABLE `Rating`
ADD CONSTRAINT UC_Rating
UNIQUE (`id_Recipe`, `id_User`);

ALTER TABLE `LikeRecipe`
ADD CONSTRAINT UC_LikeRecipe
UNIQUE (`id_Recipe`, `id_User`);
