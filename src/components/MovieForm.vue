<template>
  <div>
    <h2>Add a Movie</h2>
    <div v-if="messages.length" class="alert alert-info">
      <ul>
        <li v-for="(msg, index) in messages" :key="index">{{ msg }}</li>
      </ul>
    </div>
    <form id="movieForm" @submit.prevent="saveMovie">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" name="poster" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

let csrf_token = ref('')
let messages = ref([])

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token
    })
}

function saveMovie() {
  const movieForm = document.getElementById('movieForm')
  const form_data = new FormData(movieForm)

  fetch('/api/v1/movies', {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.errors) {
        messages.value = data.errors.map((error) => Object.values(error).join())
      } else {
        messages.value = [data.message]
        movieForm.reset()
      }
    })
    .catch((error) => {
      console.error(error)
      messages.value = ['An error occurred while submitting the form.']
    })
}

onMounted(() => {
  getCsrfToken()
})
</script>

<style scoped>
.alert {
  margin-top: 1rem;
}
</style>
