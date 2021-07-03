# Refactor - API

## Recipes

- ### `GET /recipes`

  Get all recipes, with filters

  **Response**

  ```ts
  {
    recipes: [
      {
        id: string,
        title: string,
        description: string
      }
    ]
  }
  ```

- ### `GET /recipes/:recipeId`

  Get single recipe.

  > Note: no need to show user infos. These will be available with the /user/:id endpoint,
  > and it will be the UIs job to correctly map the ids for favorites, ratings, etc.

  **Response**

  ```ts
  {
    id: string,
    title: string,
    description: string,
    author: {
      username: string,
      id: string
    },
    ingredients: [
      {
        id: string,
        name: string,
        measurement: string,
        quantity: number
      }
    ],
    directives: string,
    comments: [
      {
        author: {
          username: string,
          id: string
        },
        message: string
      }
    ],
    globalRating: number
  }
  ```

- ### `POST /recipes`

  Create a recipe.

  **Response**

  ```ts
  {
    title: string,
    description: string,
    directives: string,
    ingredients: [
      id: string,
      quantity: number
    ]
  }
  ```

## Users

- ### `GET /users/:userId`

  Get single user infos

  **Response**

  ```ts
  {
    id: string,
    username: string,
    favoritedRecipes: [
      {
        id: string,
        title: string,
        description: string
      }
    ],
    createdRecipes: [
      {
        id: string,
        title: string,
        description: string
      }
    ]
  }
  ```
