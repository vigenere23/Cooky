<template>
  <div class="account-edit-page">
    <h1> Edit Account  </h1>
    <div class="inputs-wrapper">
      <LabelInput
        label="Email"
        v-model="email"
      />
      <Button
        accent
        @click="changeEmail"
      >
        Change email
      </Button>
      <LabelInput
        label="Door number"
        v-model="doorNumber"
      />
      <Button
        accent
        @click="changeDoorNumber"
      >
        Change door number
      </Button>
      <LabelInput
        label="Apartment"
        v-model="apartment"
      />
      <Button
        accent
        @click="changeApartment"
      >
        Change apartment
      </Button>
      <LabelInput
        label="Street"
        v-model="street"
      />
      <Button
        accent
        @click="changeStreet"
      >
        Change street
      </Button>
      <LabelInput
        label="City"
        v-model="city"
      />
      <Button
        accent
        @click="changeCity"
      >
        Change city
      </Button>
      <LabelInput
        label="Country"
        v-model="country"
      />
      <Button
        accent
        @click="changeCountry"
      >
        Change country
      </Button>
      <LabelInput
        label="Password"
        v-model="password"
      />
      <LabelInput
        label="Confirm password"
        v-model="confirmPassword"
      />
      <Button
        accent
        @click="changePassword"
      >
        Change password
      </Button>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import { EventBus } from '@/js/eventbus'
import Button from '@/components/buttons/Button'
import LabelInput from '@/components/inputs/LabelInput'

export default {
  name: 'AccountEdit',

  components: {
    Button,
    LabelInput
  },

  data () {
    return {
      email: '',
      username: '',
      password: '',
      confirmPassword: '',
      doorNumber: '',
      apartment: '',
      street: '',
      city: '',
      country: ''
    }
  },
  methods: {
    async changePassword () {
      if (this.password === this.confirmPassword && this.password.length !== 0) {
        API.modifyPassword(this.password)
        EventBus.$emit('toast', { type: 'success', message: 'Password modified' })
        this.password = ''
        this.confirmPassword = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Passwords do not concord' })
        this.confirmPassword = ''
      }
    },

    async changeCountry () {
      if (this.country.length !== 0) {
        API.modifyCountry(this.country)
        EventBus.$emit('toast', { type: 'success', message: 'Country modified' })
        this.country = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field' })
      }
    },

    async changeCity () {
      if (this.city.length !== 0) {
        API.modifyCity(this.city)
        EventBus.$emit('toast', { type: 'success', message: 'City modified' })
        this.city = ''
      } else {
      }
    },

    async changeStreet () {
      if (this.street.length !== 0) {
        API.modifyStreet(this.street)
        EventBus.$emit('toast', { type: 'success', message: 'Street modified' })
        this.street = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field' })
      }
    },

    async changeApartment () {
      API.modifyApartment(this.apartment)
      EventBus.$emit('toast', { type: 'success', message: 'Apartment modified' })
      this.apartment = ''
    },

    async changeDoorNumber () {
      if (this.doorNumber.length !== 0 && !parseInt(this.doorNumber).isNaN) {
        API.modifyDoorNumber(this.doorNumber)
        EventBus.$emit('toast', { type: 'success', message: 'Door number modified' })
        this.doorNumber = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field or door is not a number' })
      }
    },

    async changeEmail () {
      if (this.email.length !== 0) {
        API.modifyEmail(this.email)
        EventBus.$emit('toast', { type: 'success', message: 'Email modified' })
        this.email = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field' })
      }
    }
  }
}
</script>

<style lang="scss">
.account-edit-page {
  .inputs-wrapper {
    width: 100%;
    max-width: 400px;
    margin: auto;
  }
}
</style>
