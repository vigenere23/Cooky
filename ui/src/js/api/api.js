import { AxiosHelper } from '@/js/helpers/axios'
const BASE_URL = process.env.VUE_APP_API_URL || 'http://127.0.0.1:5000'

export class API {
  static async getCurrentUserInfos () {
    const url = `${BASE_URL}/userInfos`
    return AxiosHelper.axiosGet(url)
  }

  static async getUserById (id) {
    const url = `${BASE_URL}/users/${id}`
    return AxiosHelper.axiosGet(url)
  }

  static async getUserByUsername (username) {
    const url = `${BASE_URL}/users/${username}`
    return AxiosHelper.axiosGet(url).id
  }

  static async getRecipesByUser (userId) {
    const url = `${BASE_URL}/users/${userId}/recipes`
    return AxiosHelper.axiosGet(url)
  }

  static async getUserLikes (userId) {
    const url = `${BASE_URL}/users/${userId}/likes`
    return AxiosHelper.axiosGet(url)
  }

  static async getAccount (id) {
    const url = `${BASE_URL}/users/${id}/account`
    return AxiosHelper.axiosGet(url)
  }

  static async getProfile (id) {
    const url = `${BASE_URL}/users/${id}/profile`
    return AxiosHelper.axiosGet(url)
  }

  static async getAddress (id) {
    const url = `${BASE_URL}/users/${id}/address`
    return AxiosHelper.axiosGet(url)
  }

  static async getUserCart () {
    const url = `${BASE_URL}/cart`
    return AxiosHelper.axiosGet(url)
  }

  static async getUserCommands (userId) {
    const url = `${BASE_URL}/users/${userId}/commands`
    return AxiosHelper.axiosGet(url)
  }

  static async getUserRecipeRatings (userId) {
    const url = `${BASE_URL}/users/${userId}/ratings`
    return AxiosHelper.axiosGet(url)
  }

  static async userLikeRecipe (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}/likes`
    return AxiosHelper.axiosPost(url)
  }

  static async userUnlikeRecipe (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}/likes`
    return AxiosHelper.axiosDelete(url)
  }

  static async userRateRecipe (recipeId, rating, alreadyRated) {
    const body = {
      'value': rating
    }
    const url = `${BASE_URL}/recipes/${recipeId}/ratings`
    return alreadyRated
      ? AxiosHelper.axiosPut(url, body)
      : AxiosHelper.axiosPost(url, body)
  }

  static async getRecipes () {
    const url = `${BASE_URL}/recipes`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipeById (id) {
    const url = `${BASE_URL}/recipes/${id}`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipesByName (name) {
    const url = `${BASE_URL}/recipes`
    const params = { name }
    return AxiosHelper.axiosGet(url, { params })
  }

  static async getIngredientFromIdRecipe (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}/ingredients`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipeComments (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}/comments`
    return AxiosHelper.axiosGet(url)
  }

  static async getIngredients () {
    const url = `${BASE_URL}/ingredients`
    return AxiosHelper.axiosGet(url)
  }

  static async getIngredientsByName (name) {
    const url = `${BASE_URL}/ingredients/`
    const params = { name }
    return AxiosHelper.axiosGet(url, { params })
  }

  static async getQuantityUnitsOfIngredient (ingredientId) {
    const url = `${BASE_URL}/ingredients/${ingredientId}/mesures`
    return AxiosHelper.axiosGet(url)
  }

  static async getCartItems () {
    const url = `${BASE_URL}/cart/items`
    return AxiosHelper.axiosGet(url)
  }

  static async addCartItem (ingredientId) {
    const body = {
      'id_Ingredient': ingredientId
    }
    const url = `${BASE_URL}/cart/items`
    return AxiosHelper.axiosPost(url, body)
  }

  static async removeCartItem (ingredientId) {
    const url = `${BASE_URL}/cart/items/${ingredientId}`
    return AxiosHelper.axiosDelete(url)
  }

  static async addRecipe (name, description, directives, ingredients) {
    const body = {
      name,
      description,
      directives,
      ingredients
    }
    const url = `${BASE_URL}/recipes`
    return AxiosHelper.axiosPost(url, body)
  }

  static async modifyRecipe (recipeId, name, directives, ingredients) {
    const body = {
      name,
      directives,
      ingredients
    }
    const url = `${BASE_URL}/recipes/${recipeId}`
    return AxiosHelper.axiosPut(url, body)
  }

  static async addRecipeComment (recipeId, comment) {
    const body = {
      'text': comment
    }
    const url = `${BASE_URL}/recipes/${recipeId}/comments`
    return AxiosHelper.axiosPost(url, body)
  }

  static async createCommand () {
    const url = `${BASE_URL}/cart/command`
    return AxiosHelper.axiosPost(url)
  }

  static async deleteRecipe (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}`
    return AxiosHelper.axiosDelete(url)
  }

  static async modifyRecipeName (recipeId, recipeName) {
    const body = {
      'name': recipeName
    }
    const url = `${BASE_URL}/recipes/${recipeId}/name`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyRecipeDirectives (recipeId, directives) {
    const body = {
      'directives': directives
    }
    const url = `${BASE_URL}/recipes/${recipeId}/directives`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyRecipeIngredientQuantity (recipeId, ingredientId, totalQuantity) {
    const body = {
      'id_Ingredient': ingredientId,
      'totalQuantity': totalQuantity
    }
    const url = `${BASE_URL}/recipes/${recipeId}/ingredientQuantity`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyFirstName (userId, firstName) {
    const body = {
      'firstName': firstName
    }
    const url = `${BASE_URL}/users/${userId}/firstName`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyLastName (userId, lastName) {
    const body = {
      'lastName': lastName
    }
    const url = `${BASE_URL}/users/${userId}/lastName`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyEmail (userId, email) {
    const body = {
      'email': email
    }
    const url = `${BASE_URL}/users/${userId}/email`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyPassword (userId, password) {
    const body = {
      'password': password
    }
    const url = `${BASE_URL}/users/${userId}/password`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyCountry (userId, country) {
    const body = {
      'country': country
    }
    const url = `${BASE_URL}/users/${userId}/country`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyCity (userId, city) {
    const body = {
      'city': city
    }
    const url = `${BASE_URL}/users/${userId}/city`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyStreet (userId, street) {
    const body = {
      'street': street
    }
    const url = `${BASE_URL}/users/${userId}/street`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyApartment (userId, apartment) {
    let apart = apartment
    if (apart.length < 1) {
      apart = null
    }
    const body = {
      'apartment': apart
    }
    const url = `${BASE_URL}/users/${userId}/apartment`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyDoorNumber (userId, number) {
    const body = {
      'number': number
    }
    const url = `${BASE_URL}/users/${userId}/doorNumber`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyCartItemQuantity (ingredientId, multiplier) {
    const body = {
      'multiplier': multiplier
    }
    const url = `${BASE_URL}/cart/items/${ingredientId}`
    return AxiosHelper.axiosPut(url, body)
  }

  static async login (data) {
    const url = `${BASE_URL}/login`
    return AxiosHelper.axiosPost(url, data)
  }

  static async signup (data) {
    const url = `${BASE_URL}/signup`
    return AxiosHelper.axiosPost(url, data)
  }
}
