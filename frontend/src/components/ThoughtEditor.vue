<template>
<!-- Form to capture a thought -->
  <div class="editor-container">
    <div class="thought-editor">
      <textarea class="thought-title" v-model="thoughtTitle" placeholder="Thought title..."/>
      <textarea class="thought-body" v-model="thoughtBody" placeholder="What's on your mind?"/>
    </div>
    <div class="new-thought">
      <button @click="createNewThought">+</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const thoughtTitle = ref<string>('')
const thoughtBody = ref<string>('')


function createNewThought() {
  thoughtTitle.value = "";
  thoughtBody.value = "";
}
</script>


<style scoped>
.editor-container {
  display: flex;
  flex-direction: row;
  width: 100%;
}
.thought-editor {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.thought-title {
  border: 0;
  border-bottom: 1px solid grey;
  width: 90%;
  font-size: large;
  resize: none;
}

.thought-body {
  margin: 1em 0;
  width: 90%;
  height: 100%;
  border: 0;
  resize: none;
}
</style>