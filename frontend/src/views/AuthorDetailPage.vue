<template>
  <section>
    <br />

    <h2>
      <router-link class="no-decoration" :to="{ name: 'author-list' }">Auteur:</router-link>&nbsp;
      <span class="text-secondary">{{ currentAuthor }}</span>
    </h2>

    <br />

    <div v-if="questions && questions.length === 0">
      Pas de questions pour cet auteur :(
    </div>

    <!-- Question List -->
    <div v-if="questions && questions.length > 0" class="row">
      <div class="row-item row-item-question" v-for="question in questions" :key="question.id">
        <router-link class="no-decoration" :to="{ name: 'question-detail', params: { questionId: question.id } }">
          <QuestionPreviewCard v-bind:question="question" />
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import QuestionPreviewCard from '../components/QuestionPreviewCard.vue'

export default {
  name: 'AuthorDetailPage',
  components: {
    QuestionPreviewCard,
  },

  data () {
    return {
      // currentAuthor: null,
      // questions: null,
    }
  },

  computed: {
    currentAuthor () {
      return this.$route.params.authorName;
    },
    questions () {
      return this.$store.getters.getQuestionsByAuthorName(this.$route.params.authorName);
    },
  },

  mounted () {
  },

  methods: {
  }
}
</script>

<style scoped>
.row-item-question {
  height: 150px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.1s;
  border: 2px solid var(--primary);
  border-radius: 5px;
  cursor: pointer;
}

@media(hover: hover) and (pointer: fine) {
  .row-item-question:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  }
}
</style>
