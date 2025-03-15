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
        {{ thought.title || 'Untitled' }}
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

.thought {
  border: 1px solid gray;
  margin: 5px;
  padding: 5px;
}
</style>