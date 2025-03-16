<template>
  <div class="thought-list">
    <div>Thoughts</div>
    <div class="thoughts">
      <div
        v-for="thought in thoughts"
        :key="thought.id"
        @click="$emit('selectThought', thought)"
        class="thought"
      >
        <a class="thought-link">{{ thought.title || 'Untitled' }}</a>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import type Thought from '@/types/Thought';

defineProps<{
  thoughts: Array<Thought>,
}>();

</script>

<style scoped>
.thought-list {
  display: flex;
  padding: 5px;
  flex-direction: column;
}

.thought-link {
  text-decoration: none;
  font-weight: normal;
  font-size: smaller;
  color: #777;
}

.thought {
  border: 1px solid gray;
  margin: 0.2em;
  padding: 0.2em;
}
</style>