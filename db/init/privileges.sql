use projet;

GRANT SELECT, INSERT, UPDATE, DELETE
ON `Recipe` TO 'api'@'%';

GRANT SELECT, INSERT, UPDATE, DELETE
ON `CartItem` TO 'api'@'%';

GRANT SELECT, INSERT, UPDATE, DELETE
ON `Recipe` TO 'api'@'%';

GRANT SELECT, INSERT, UPDATE
ON `Rating` TO 'api'@'%';

GRANT SELECT, INSERT, DELETE
ON `LikeRecipe` TO 'api'@'%';

GRANT SELECT, INSERT, UPDATE
ON `Account` TO 'api'@'%';

GRANT SELECT, INSERT, UPDATE
ON `Address` TO 'api'@'%';

GRANT SELECT, INSERT, UPDATE
ON `Cart` TO 'api'@'%';

GRANT SELECT, INSERT
ON `User` TO 'api'@'%';

GRANT SELECT, INSERT
ON `RecipeIngredient` TO 'api'@'%';

GRANT SELECT, INSERT
ON `Command` TO 'api'@'%';

GRANT SELECT, INSERT
ON `Comment` TO 'api'@'%';

GRANT SELECT
ON `Ingredient` TO 'api'@'%';

GRANT SELECT
ON `IngredientType` TO 'api'@'%';

GRANT SELECT
ON `QuantityUnit` TO 'api'@'%';

GRANT SELECT
ON `QuantityType` TO 'api'@'%';


GRANT UPDATE
ON `Command` TO 'provider'@'%';
