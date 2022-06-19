<template>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">팀 이름: {{ this.eachTeam.name }}</h5>
      <p class="card-text">팀 소개: {{ this.eachTeam.intro }}</p>
    </div>
    <v-row justify="space-around">
      <v-col cols="auto">
        <v-dialog
          transition="dialog-bottom-transition"
          max-width="600"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              v-bind="attrs"
              v-on="on"
            >From the bottom</v-btn>
          </template>
          <template v-slot:default="dialog">
            <v-card>
              <v-toolbar
                color="primary"
                dark
              >Opening from the bottom</v-toolbar>
              <v-card-text>
                <!-- <div class="text-h2 pa-12">Hello world!</div> -->
                <TeamModal :eachTeamData="eachTeam"></TeamModal>
              </v-card-text>
              <v-card-actions class="justify-end">
                <v-btn
                  text
                  @click="dialog.value = false"
                >Close</v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </v-dialog>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import TeamModal from '@/components/MainPage/TeamModal'

export default {
  name: 'TeamList',
  components: {
    TeamModal
  },
  props: {
    eachTeam: {
      type: Object,
    } 
  },
  data() {
    return {
      modalOn: false,
    }
  },
  methods: {
    modalBtn() {
      this.modalOn = !this.modalOn
    }
  },
}
</script>

<style>

</style>