# API Refactor

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

  Get single recipe

  **Response**

  ```ts
  {
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
        quantity: string
      }
    ],
    steps: string[],
    comments: [
      {
        author: {
          username: string,
          id: string
        }
      }
    ],
    globalRating: number,
    personalInfos: {
      favorited: boolean,
      rating?: number
    }
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
        title: string,
        ...
      }
    ],
    createdRecipes: [
      {
        title: string,
        ...
      }
    ]
  }
  ```