import { API } from '@/js/api/api'
import Cookies from 'js-cookie'

export const userModule = {

  namespaced: true,

  state: {
    cartItems: [],
    cart: null,
    userId: null,
    username: '',
    avatar: '',
    userRatings: [],
    userLikes: []
  },

  getters: {
    cartContains: (state) => (ingredientId) => {
      return !!state.cartItems.find(item => item.id_Ingredient === ingredientId)
    },
    avatar: (state) => (user) => {
      if (user) {
        return user.avatar || `${process.env.BASE_URL}images/default-avatar.png`
      }
      return state.avatar || `${process.env.BASE_URL}images/default-avatar.png`
    },
    likesContains: (state) => (recipeId) => {
      return !!state.userLikes.find(recipe => recipe.id === recipeId)
    },
    getUserRecipeRating: (state) => (recipeId) => {
      const rating = state.userRatings.find(rating => rating.id_Recipe === recipeId)
      return rating ? rating.value : 0
    }
  },

  mutations: {
    clear (state) {
      state.userId = state.cart = state.avatar = null
      state.cartItems = state.likes = state.ratings = []
    },
    setCartItems (state, cartItems) {
      if (cartItems) state.cartItems = cartItems
    },
    setCart (state, cart) {
      if (cart) state.cart = cart
    },
    setLikes (state, likes) {
      if (likes) state.userLikes = likes
    },
    setRatings (state, ratings) {
      if (ratings) state.userRatings = ratings
    },
    setUserInfos (state, user) {
      if (user) {
        state.userId = user.id
        state.username = user.username
      }
    }
  },

  actions: {
    async loadAll (context) {
      context.commit('clear')
      await context.dispatch('loadUserInfos')
      if (context.state.userId) {
        await context.dispatch('loadCart')
        await context.dispatch('loadLikes')
        await context.dispatch('loadRatings')
      }
    },
    async loadUserInfos (context) {
      if (Cookies.get('cooky_token')) {
        const user = await API.getCurrentUserInfos()
        context.commit('setUserInfos', user)
      }
    },
    async loadCart (context) {
      const cart = await API.getUserCart()
      if (!cart.error) {
        context.commit('setCart', cart)
      }
      if (context.state.cart) {
        const cartItems = await API.getCartItems(context.state.cart.id)
        if (!cartItems.error) {
          context.commit('setCartItems', cartItems)
        }
      }
    },
    async loadLikes (context) {
      const likes = await API.getUserLikes(context.state.userId)
      context.commit('setLikes', likes)
    },
    async loadRatings (context) {
      const ratings = await API.getUserRecipeRatings(context.state.userId)
      context.commit('setRatings', ratings)
    },
    async addCartItem (context, ingredientId) {
      if (context.state.cart) {
        await API.addCartItem(ingredientId)
        context.dispatch('loadCart')
      }
    },
    async removeCartItem (context, ingredientId) {
      if (context.state.cart) {
        await API.removeCartItem(ingredientId)
        context.dispatch('loadCart')
      }
    },
    async addLike (context, recipeId) {
      await API.userLikeRecipe(recipeId)
      context.dispatch('loadLikes')
    },
    async removeLike (context, recipeId) {
      await API.userUnlikeRecipe(recipeId)
      context.dispatch('loadLikes')
    },
    async addRating (context, { recipeId, rating }) {
      await API.userRateRecipe(
        recipeId,
        rating,
        context.getters.getUserRecipeRating(recipeId) !== 0)
      context.dispatch('loadRatings')
    }
  }

}
