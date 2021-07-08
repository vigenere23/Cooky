<template>
  <div class="commands-page">
    <h1>Commands</h1>
    <DataTable
      v-if="commands"
      :columns="columns"
      :items="commands"
    />
  </div>
</template>

<script>
import DataTable from '@/components/lists/DataTable'
import { API } from '@/js/api/api'

export default {

  name: 'Commands',

  components: {
    DataTable
  },

  data () {
    return {
      columns: [
        { name: 'creationDate', text: 'Created', sortable: true, parser: this.parseDate, defaultSorting: 'desc', initiallySorted: true },
        { name: 'arrivalDate', text: 'Arrived', sortable: true, parser: this.parseDate },
        { name: 'totalCost', text: 'Total ($)', sortable: true }
      ],
      commands: null
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
      this.commands = null
      this.commands = await API.getUserCommands()
    },
    parseDate: (date) => {
      return date ? date.split(' ').slice(0, 4).join(' ') : '---'
    }
  }

}
</script>
