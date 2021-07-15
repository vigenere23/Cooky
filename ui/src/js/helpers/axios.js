import axios from 'axios'
import { EventBus } from '@/js/eventbus'
import Cookies from 'js-cookie'
import { router } from '@/js/router'
import { store } from '@/js/store'

async function parseErrors (request) {
  try {
    const response = await request()
    if (response.data.error) {
      return handleErrors(response)
    }
    return response.data
  } catch (error) {
    handleErrors(error.response)
  }
}

function handleErrors (response) {
  const message = response.data.error
    ? response.data.error
    : response.data
  console.error(message)
  const status = response.status
  if (status === 404) {
    EventBus.$emit('toast', { type: 'error', message: 'Ressource not found' })
  } else if (status === 500) {
    EventBus.$emit('toast', { type: 'error', message: 'An unexpected error occured' })
  } else if (status === 401) {
    EventBus.$emit('toast', { type: 'error', message })
    store.commit('user/clear')
    Cookies.remove('cooky_token')
    router.push('/login')
  } else {
    EventBus.$emit('toast', { type: 'error', message })
  }
  return null
}

function getHeaders () {
  const token = Cookies.get('cooky_token')
  return token
    ? { Authorization: token }
    : null
}

export class AxiosHelper {
  static axiosGet (url, options) {
    const headers = getHeaders()
    options = { ...options, headers }
    return parseErrors(() => axios.get(url, options))
  }

  static axiosPost (url, body, options) {
    const headers = getHeaders()
    options = { ...options, headers }
    return parseErrors(() => axios.post(url, body, options))
  }

  static axiosPut (url, body, options) {
    const headers = getHeaders()
    options = { ...options, headers }
    return parseErrors(() => axios.put(url, body, options))
  }

  static axiosPatch (url, body, options) {
    const headers = getHeaders()
    options = { ...options, headers }
    return parseErrors(() => axios.patch(url, body, options))
  }

  static axiosDelete (url, body, options) {
    const headers = getHeaders()
    options = { ...options, data: body, headers }
    return parseErrors(() => axios.delete(url, options))
  }
}
