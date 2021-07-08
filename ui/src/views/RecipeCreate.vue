<template>
  <div class="recipe-create-page">
    <h1>Create a recipe</h1>
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
      <IngredientEditor @change="updateIngredients" />
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

  name: 'RecipeCreate',

  components: {
    LabelInput,
    IngredientEditor,
    Button
  },

  computed: {
    enableButton () {
      return this.name && this.directives && this.ingredients.length
    }
  },

  data () {
    return {
      name: '',
      description: '',
      directives: '',
      ingredients: []
    }
  },

  methods: {
    async submit () {
      const response = await API.addRecipe(this.name, this.description, this.directives, this.ingredients)
      if (response) {
        this.$router.push(`/recipes/${response.id}`)
      }
    },
    updateIngredients (ingredients) {
      this.ingredients = ingredients
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.recipe-create-page {
  .form {
    width: 100%;
    max-width: 600px;
    margin: auto;
  }
}
</style>
