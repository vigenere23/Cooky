<template>
  <div
    class="recipe-page"
    v-if="recipe"
  >
    <h1>{{ recipe.name }}</h1>
    <div class="recipe_intro">
      <img src="https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg">
      <p class="recipe_description">
        {{ recipe.description }}
      </p>
      <p class="user">
        by
        <router-link
          tag="a"
          :to="`/users/${recipe.user.id}`"
        >
          {{ recipe.user.username }}
        </router-link>
      </p>
    </div>
    <div class="actions">
      <Like
        v-if="userId !== recipe.user.id"
        :liked="liked"
        @liked="like"
        @unliked="unlike"
      />
      <Rating
        v-if="userId !== recipe.user.id"
        :rating="rating"
        @rated="rate"
      />
      <span v-if="recipe">
        Rated {{ recipe.rating }} stars
      </span>
    </div>
    <div class="recipe_content">
      <div>
        <h2>Ingredients</h2>
        <DataTable
          :columns="columns"
          :items="ingredients"
          :small="true"
          :actions="actions"
        />
      </div>
      <div>
        <h2>Steps</h2>
        <p>{{ recipe.directives }}</p>
      </div>
    </div>
    <Button
      v-if="userId === recipe.user.id"
      danger
      @click="deleteRecipe"
    >
      Delete
    </Button>
    <div v-if="comments">
      <h2>Comments</h2>
      <CommentList
        :comments="comments"
        :owner-id="recipe.user.id"
        @submit="addComment"
      />
    </div>
  </div>
</template>

<script>
import DataTable from '@/components/lists/DataTable'
import CommentList from '@/components/comments/CommentList'
import Rating from '@/components/inputs/Rating'
import Like from '@/components/inputs/Like'
import Button from '@/components/buttons/Button'
import { mapState, mapGetters, mapActions } from 'vuex'
import { API } from '@/js/api/api'

export default {

  name: 'Recipe',

  components: {
    DataTable,
    CommentList,
    Rating,
    Like,
    Button
  },

  computed: {
    ...mapState('user', ['userId', 'userLikes', 'userRatings']),
    ...mapGetters('user', ['cartContains', 'likesContains', 'getUserRecipeRating']),
    rating () {
      return this.getUserRecipeRating(this.id)
    },
    liked () {
      return this.likesContains(this.id)
    }
  },

  data () {
    return {
      id: null,
      recipe: null,
      ingredients: [],
      comments: [],
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' }
      ],
      actions: {
        isSelected: (ingredient) => this.cartContains(ingredient.id),
        onSelection: (ingredient) => this.addCartItem(ingredient.id),
        onDeselection: (ingredient) => this.removeCartItem(ingredient.id)
      }
    }
  },

  created () {
    this.fetchData()
  },

  watch: {
    '$route': 'fetchData'
  },

  methods: {
    async fetchData () {
      this.id = Number(this.$route.params.id)
      this.recipe = null
      this.ingredients = []
      this.fetchRecipe()
      this.fetchIngredients()
      this.fetchComments()
    },
    async fetchRecipe () {
      this.recipe = await API.getRecipeById(this.id)
    },
    async fetchIngredients () {
      this.ingredients = await API.getIngredientFromIdRecipe(this.id)
      this.ingredients.map(x => {
        const ingredient = x
        ingredient.quantity = x.totalQuantity + ' ' + x.quantityUnit.abbreviation
        return ingredient
      })
    },
    async fetchComments () {
      this.comments = await API.getRecipeComments(this.id)
    },
    async like () {
      await this.addLike(this.id)
    },
    async unlike () {
      await this.removeLike(this.id)
    },
    async rate (rating) {
      await this.addRating({ recipeId: this.id, rating })
    },
    async addComment (comment) {
      await API.addRecipeComment(this.id, comment)
      await this.fetchComments()
    },
    async deleteRecipe () {
      await API.deleteRecipe(this.id)
      this.$router.push('/recipes')
    },
    ...mapActions('user', ['addCartItem', 'removeCartItem', 'addRating', 'addLike', 'removeLike'])
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.recipe-page {

  .actions {
    display: flex;
    align-items: center;

    > * {
      flex-shrink: 0;

      &:not(:last-child) {
        margin-right: 16px;
      }
    }

    .like {
      cursor: pointer;
    }
  }

  .recipe_intro {
    width: 100%;
    max-width: 700px;
    margin: auto;

    img {
      width: 100%;
      display: block;
      border-radius: 4px;
      @include mdElevation(2);
    }

    .recipe_description {
      color: $secondary-text-color;
    }

    .user {
      font-size: 16px;

      a {
        color: $primary-color;
        font-weight: 500;
      }
    }
  }

  .recipe_content {
    display: grid;
    margin: auto;
    justify-content: space-around;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 32px;

    > * {
      grid-column: span 1;
    }
  }
}

@media screen and (max-width: $phone-max) {
  .recipe-page {
    .recipe_content {
      > * {
        grid-column: span 2;
      }
    }
  }
}
</style>
