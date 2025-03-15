<template>
  <div class="thoughts">
    <aside class="sidebar">
      <thought-list :thoughts="thoughts" @selectThought="selectThought" />
    </aside>
    <main class="editor">
      <thought-editor :thought="thought" />
    </main>
  </div>
</template>


<script setup lang="ts">
import ThoughtEditor from '@/components/ThoughtEditor.vue';
import ThoughtList from '@/components/ThoughtList.vue';
import type Thought from '@/types/Thought';
import { ref } from 'vue';

const thoughts = ref<Thought[]>([
  { id: '1', title: 'Thought 1 is short', body: 'This is the first thought' },
  { id: '2', title: 'Thought 2 is a bit longer', body: 'This is the second thought' },
  { id: '3', title: 'Thought 3 have a very long and title for reasons sake. Darn it, that is not what I was hoping for', body: 'This is the third thought' },
]);

const thought = ref<Thought | null>(null);

function selectThought(selectedThought: Thought) {
  thought.value = selectedThought;
}

</script>

<style scoped>
.thoughts {
  display: flex;
  flex-direction: row;
  overflow-y: auto;
}

.sidebar {
  border: 1px solid black;
  min-width: 250px;
  max-width: 30%;
}

.editor {
  border: 1px solid black;
  padding: 1em 0.5em;
  min-width: 400px;
  width: 100%;
  display: flex;
  flex-direction: row;
}
</style>