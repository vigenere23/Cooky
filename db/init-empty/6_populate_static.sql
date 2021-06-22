USE projet;


/*---------- STATIC TABLES ----------*/

INSERT INTO `IngredientType` (`id`,`name`) VALUES
(NULL, 'Dairy products'),
(NULL, 'Oils'),
(NULL, 'Fruits and vegetables'),
(NULL, 'Confectionery'),
(NULL, 'Cereal products'),
(NULL, 'Meat products'),
(NULL, 'Fish products'),
(NULL, 'Egg products'),
(NULL, 'Spices'),
(NULL, 'Beverages'),
(NULL, 'Salads'),
(NULL, 'Prepared foods'),
(NULL, 'Others');


INSERT INTO `QuantityType` (`id`,`name`) VALUES
(NULL, 'Volume'),
(NULL, 'Weight'),
(NULL, 'Unit');


INSERT INTO `QuantityUnit` (`id`,`id_QuantityType`,`name`,`abbreviation`) VALUES
(NULL, 1, 'teaspoon', 'tsp'),
(NULL, 1, 'tablespoon', 'tbsp'),
(NULL, 1, 'fluid ounce', 'fl oz'),
(NULL, 1, 'cup', 'cup'),
(NULL, 1, 'milliliter', 'mL'),
(NULL, 1, 'liter', 'L'),
(NULL, 1, 'deciliter', 'dL'),
(NULL, 2, 'pound', 'lb'),
(NULL, 2, 'ounce', 'oz'),
(NULL, 2, 'miligram', 'mg'),
(NULL, 2, 'gram', 'g'),
(NULL, 2, 'kilogram', 'kg'),
(NULL, 3, 'unit', 'unit');
