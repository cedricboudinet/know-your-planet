<template>
  <section>
    <br />

    <h2>
      Tous les auteurs&nbsp;
      <span v-if="authors" class="text-secondary"><small>{{ authors.length }}</small></span>
    </h2>

    <br />

    <div v-if="authors && authors.length === 0">
      Pas d'auteurs :(
    </div>

    <div v-if="authors && authors.length > 0">
      <router-link class="no-decoration" v-for="author in authors" :key="author.name" :to="{ name: 'author-detail', params: { authorName: author.name } }">
        <span class="category">
          <h3>{{ author.name }}</h3>
          <p><strong>{{ author.question_count }}</strong> question<span v-if="author.question_count > 1">s</span></p>
        </span>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AuthorListPage',
  components: {
  },

  data () {
    return {
      // authors: null,
    }
  },

  computed: {
    authors () {
      return this.$store.state.authors;
    },
  },

  mounted () {
  },

  methods: {
  }
}
</script>

<style scoped>
.category {
  width: 300px;
  display: inline-block;
  border: 1px solid #f3993f;
  border-radius: 5px;
  margin: 2.5px;
  padding: 5px;
  cursor: pointer;
}
</style>
