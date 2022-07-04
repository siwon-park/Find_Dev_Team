<template>
  <div>
    <div v-if="this.bookmarkings.bookmarking">
      나의 북마크 모아보기
      <Flicking :options="{ circular: true }">
        <div class="d-flex justify-content-center">
          <BookmarkingList v-for="userId in this.bookmarkings.bookmarking" :key="userId" :userId="userId"></BookmarkingList>
        </div>
      </Flicking>
    </div>
    <div v-if="this.bookmarkings.bookmarking.length === 0">
      {{this.currentUser.username}}님은 현재 북마킹 중인 유저가 없습니다.
    </div>
  </div>
</template>

<script>
import BookmarkingList from '@/components/MyPage/BookmarkingList.vue'
import { mapActions, mapGetters } from 'vuex'
import {Flicking} from "@egjs/vue-flicking"

export default {
  name: 'MyBookmarks',
  components: {
    BookmarkingList,
    Flicking,
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

<style >

</style>