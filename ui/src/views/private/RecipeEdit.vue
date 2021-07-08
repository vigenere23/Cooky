<template>
  <div class="recipe-edit-page">
    <h1>Edit recipe</h1>
    <div class="form">
      <LabelInput
        label="name"
        placeholder="Fresh orange juice"
        v-model="name"
        :validate="(value) => !!value"
      />
      <LabelInput
        label="description"
        placeholder="Just the best orange juice in town!"
        type="textarea"
        allow-empty
        v-model="description"
      />
      <LabelInput
        label="directives"
        placeholder="Step 1 : crush the orange inside the recipient."
        type="textarea"
        v-model="directives"
        :validate="(value) => !!value"
      />
      <IngredientEditor
        v-if="ingredients"
        :initial-ingredients="ingredients"
        @change="updateIngredients"
      />
      <Button
        accent
        right
        :disable="!enableButton"
        @click="submit"
      />
    </div>
  </div>
</template>

<script>
import LabelInput from '@/components/inputs/LabelInput'
import IngredientEditor from '@/components/ingredients/IngredientEditor'
import Button from '@/components/buttons/Button'
import { API } from '@/js/api/api'

export default {

  name: 'RecipeEdit',

  components: {
    LabelInput,
    IngredientEditor,
    Button
  },

  computed: {
    enableButton () {
      return this.name && this.directives && this.ingredients && this.ingredients.length
    }
  },

  data () {
    return {
      id: null,
      name: '',
      description: '',
      directives: '',
      ingredients: null
    }
  },

  async created () {
    await this.fetchData()
  },

  watch: {
    '$route': 'fetchData'
  },

  methods: {
    async submit () {
      const response = await API.modifyRecipe(this.id, this.name, this.directives, this.ingredients)
      if (response) {
        this.$router.push(`/recipes/${response.id}`)
      }
    },
    updateIngredients (ingredients) {
      this.ingredients = ingredients
    },
    async fetchData () {
      this.name = this.description = this.directives = ''
      this.ingredients = null
      this.id = Number(this.$route.params.id)
      const recipe = await API.getRecipeById(this.id)
      this.name = recipe.name
      this.description = recipe.description
      this.directives = recipe.directives
      this.ingredients = await API.getIngredientFromIdRecipe(this.id)
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.recipe-edit-page {
  .form {
    width: 100%;
    max-width: 600px;
    margin: auto;
  }
}
</style>
