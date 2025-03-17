<template>
  <div class="orientation">
    <div class="purpose-summary">
      <div class="prompt">{{ purposePrompt }}</div>
      <div class="lead-in">Here's what you've said in the past</div>
      <div class="summary">{{ summary }}</div>
      <div class="lead-in">{{ reflectionPrompt }}</div>
      <div class="response">
        <textarea v-model="reflection" class="thought" placeholder="Today, my purpose my purpose feels most aligned to...">{{ reflection }}</textarea>
      </div>
    </div>
    <div class="action">
      <button @click="continueFlow">Continue</button>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue';

const purposePrompt = ref<string>("What do you want to orient yourself towards in your life?");
const summary = ref<string>("Submit your first orientation reflection to see a summary here.");

const reflectionPrompt = ref<string>("What guiding orientation resonates with you today?");
const reflection = ref<string>("");

function continueFlow() {
  console.log("Continue");
}
</script>


<style scoped>
.orientation {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1em;
}

.prompt {
  font-size: large;
  font-weight: bold;
}

.lead-in {
  font-size: medium;
  font-style: italic;
  margin-top: 2em;
}

div {
  margin: 0.5em;
}

textarea {
  width: 100%;
  min-width: 600px;
  height: 100px;
  border: 0;
  resize: none;
}
</style>