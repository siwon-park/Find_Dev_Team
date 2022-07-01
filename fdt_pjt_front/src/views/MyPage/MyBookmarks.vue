<template>
  <div>
    <div v-if="this.bookmarkings.bookmarking">
      <BookmarkingList v-for="userId in this.bookmarkings.bookmarking" :key="userId" :userId="userId"></BookmarkingList>
    </div>
    <div v-else>
      {{this.currentUser.username}}님은 현재 북마킹 중인 유저가 없습니다.
    </div>
  </div>
</template>

<script>
import BookmarkingList from '@/components/MyPage/BookmarkingList.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MyBookmarks',
  components: {
    BookmarkingList,
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'bookmarkings',]),
  },
  methods: {
    ...mapActions(['fetchBookmarkings',]),
  },
  created() {
    this.fetchBookmarkings(this.currentUser.id)
  }
}
</script>

<style>

</style>