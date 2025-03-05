<template>
<!-- Form to capture a thought -->
  <div class="thought-form">
    <textarea class="thought" v-model="thoughtText" placeholder="Enter your thought..."/>
    <button @click="submitThought">Log Thought</button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const thoughtText = ref('')

function submitThought() {
  console.log(thoughtText.value)
}

</script>
<style scoped>
.thought-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.thought {
  width: 100%;
  margin: 1em;
}
</style>