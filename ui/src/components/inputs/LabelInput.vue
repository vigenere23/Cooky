<template>
  <div
    class="label-input"
    :class="{ focused, error }"
  >
    <span class="label">
      {{ label }}
    </span>
    <textarea
      v-if="type === 'textarea'"
      @focus="focus"
      @blur="blur"
      @input="input"
      :placeholder="placeholder"
      :name="label"
      :value="value"
      maxlength="500"
    />
    <input
      v-else
      @focus="focus"
      @blur="blur"
      @input="input"
      :type="type"
      :placeholder="placeholder"
      :name="label"
      :value="value"
    >
  </div>
</template>

<script>
export default {
  name: 'LabelInput',
  props: {
    type: {
      type: String,
      default: 'text'
    },
    label: {
      type: String,
      default: ''
    },
    value: {
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    },
    validate: {
      type: Function,
      default: () => true
    }
  },
  data () {
    return {
      focused: false,
      error: false
    }
  },
  methods: {
    focus () { this.focused = true },
    blur () {
      this.focused = false
      this.error = !this.validate(this.value)
    },
    input (e) {
      this.$emit('input', e.target.value)
    }
  }
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.label-input {
  margin: 16px 0;
  width: 100%;

  input, textarea {
    display: block;
    width: 100%;
    font-family: 'Roboto';
    font-size: 16px;
    line-height: 1.2em;
    padding: 8px 12px;
    padding-right: 48px;
    border-radius: 4px;
    border: $faded-border;
    border-width: 2px;
  }

  .label {
    display: block;
  }

  &.focused {
    input, textarea {
      border-color: $primary-color;
    }

    .label {
      color: $primary-color;
    }
  }

  &:not(.focused).error {
    input, textarea {
      border-color: #d32c2c;
    }

    .label {
      color: #d32c2c;
    }
  }
}
</style>
