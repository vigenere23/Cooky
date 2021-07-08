<template>
  <div class="account-page">
    <h1> Account </h1>
    <div>
      <h2> FirstName : {{ firstname }} </h2>
    </div>
    <div>
      <h2> LastName : {{ lastname }} </h2>
    </div>
    <div>
      <h2> Email : {{ email }} </h2>
    </div>
    <div>
      <h2> Username : {{ username }} </h2>
    </div>
    <div>
      <h2> Address : {{ doorNumber }} {{ street }} </h2>
    </div>
    <div>
      <h2> Appartement : {{ apartment }} </h2>
    </div>
    <div>
      <h2> City : {{ city }} </h2>
    </div>
    <div>
      <h2> Country : {{ country }} </h2>
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        @click="editAccount"
      >
        Edit info
      </Button>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import Button from '@/components/buttons/Button'
import { mapState } from 'vuex'

export default {
  name: 'Account',

  components: {
    Button
  },

  computed: mapState('user', ['userId']),

  data () {
    return {
      firstname: '',
      lastname: '',
      email: '',
      username: '',
      doorNumber: '',
      apartment: '',
      street: '',
      city: '',
      country: ''
    }
  },
  methods: {
    editAccount () {
      this.$router.push(`/account/edit`)
    }
  },
  async beforeMount () {
    let data = await API.getUserById(this.userId)
    this.username = data.username

    let dataAccount = await API.getAccount()
    if (dataAccount && !dataAccount.error) {
      this.email = dataAccount.email
      this.firstname = dataAccount.firstName
      this.lastname = dataAccount.lastName
    }

    let dataAddress = await API.getAddress()
    if (dataAddress && !dataAddress.error) {
      this.apartment = dataAddress.apartment
      this.city = dataAddress.city
      this.country = dataAddress.country
      this.doorNumber = dataAddress.number
      this.street = dataAddress.street
    }
  }
}
</script>

<style>

</style>
