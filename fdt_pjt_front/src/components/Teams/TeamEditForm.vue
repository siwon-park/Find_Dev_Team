<template>
  <div>
    <h4>팀 수정 폼</h4>
    <p>{{ currentUser }}</p>
    <form @submit.prevent="onSubmit()" action="POST">
      <div>
        팀 명:
        <label for="name"></label>
        <input type="text" v-model="newTeam.name" placeholder="name" id="name">
      </div>
      <div>
        팀 소개:
        <label for="intro"></label>
        <input type="text" v-model="newTeam.intro" placeholder="intro" id="intro">
      </div>
      <div>
        <v-card
          color="blue-grey darken-1"
          dark
          :loading="isUpdating"
        >
          <template v-slot:progress>
            <v-progress-linear
              absolute
              color="green lighten-3"
              height="4"
              indeterminate
            ></v-progress-linear>
          </template>
          <v-img
            height="200"
            src="https://cdn.vuetifyjs.com/images/cards/dark-beach.jpg"
          >
            <v-row>
              <v-col
                class="text-right"
                cols="12"
              >
                <v-menu
                  bottom
                  left
                  transition="slide-y-transition"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      icon
                      v-bind="attrs"
                      v-on="on"
                    >
                      <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <v-list-item @click="isUpdating = true">
                      <v-list-item-action>
                        <v-icon>mdi-cog</v-icon>
                      </v-list-item-action>
                      <v-list-item-content>
                        <v-list-item-title>Update</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </v-col>
              <v-row
                class="pa-4"
                align="center"
                justify="center"
              >
                <v-col class="text-center">
                  <h3 class="text-h5">
                    {{ name }}
                  </h3>
                  <span class="grey--text text--lighten-1">{{ title }}</span>
                </v-col>
              </v-row>
            </v-row>
          </v-img>
          <v-form>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="name"
                    :disabled="isUpdating"
                    filled
                    color="blue-grey lighten-2"
                    label="Name"
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="title"
                    :disabled="isUpdating"
                    filled
                    color="blue-grey lighten-2"
                    label="Title"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-autocomplete
                    v-model="friends"
                    :disabled="isUpdating"
                    :items="people"
                    filled
                    chips
                    color="blue-grey lighten-2"
                    label="Select"
                    item-text="name"
                    item-value="name"
                    multiple
                  >
                    <template v-slot:selection="data">
                      <v-chip
                        v-bind="data.attrs"
                        :input-value="data.selected"
                        close
                        @click="data.select"
                        @click:close="remove(data.item)"
                      >
                        <v-avatar left>
                          <v-img :src="data.item.avatar"></v-img>
                        </v-avatar>
                        {{ data.item.name }}
                      </v-chip>
                    </template>
                    <template v-slot:item="data">
                      <template v-if="typeof data.item !== 'object'">
                        <v-list-item-content v-text="data.item"></v-list-item-content>
                      </template>
                      <template v-else>
                        <v-list-item-avatar>
                          <img :src="data.item.avatar">
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title v-html="data.item.name"></v-list-item-title>
                          <v-list-item-subtitle v-html="data.item.group"></v-list-item-subtitle>
                        </v-list-item-content>
                      </template>
                    </template>
                  </v-autocomplete>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
          <v-divider></v-divider>
          <v-card-actions>
            <v-switch
              v-model="autoUpdate"
              :disabled="isUpdating"
              class="mt-0"
              color="green lighten-2"
              hide-details
              label="Auto Update"
            ></v-switch>
            <v-spacer></v-spacer>
            <v-btn
              :disabled="autoUpdate"
              :loading="isUpdating"
              color="blue-grey darken-3"
              depressed
              @click="isUpdating = true"
            >
              <v-icon left>
                mdi-update
              </v-icon>
              Update Now
            </v-btn>
          </v-card-actions>
        </v-card>


        <!-- 팀 멤버:
        <label for="team_member"></label>
        <input type="text" v-model="newTeam.team_member" placeholder="team_member" id="team_member"> -->
      </div>
      <div>
        팀 주제:
        <label for="theme"></label>
        <input type="text" v-model="newTeam.theme" placeholder="theme" id="theme">
      </div>
      <div>
        팀 공통 흥미:
        <label for="common_interest"></label>
        <input type="text" v-model="newTeam.common_interest" placeholder="common_interest" id="common_interest">
      </div>
      <div>
        팀 모집 인원:
        <label for="total_number"></label>
        <select v-model="total_number" aria-label="인원수를 선택하세요" class="form-select">
          <option value="0">모집 인원 선택(최대 6명)</option>
          <option value="5">5</option>
          <option value="6">6</option>
        </select>
      </div>
      <div>
        팀 카카오 오픈챗:
        <label for="kakao_chat"></label>
        <input type="text" v-model="newTeam.kakao_chat" placeholder="kakao_chat" id="kakao_chat">
      </div>
      <input type="submit">
    </form>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'TeamForm',
  props:{
    team: Object,
    action: String,
  },
  data(){
    return {
      newTeam:{
        name: this.team.name,
        intro: this.team.intro,
        leader: this.team.leader,
        team_member: this.team.team_member,
        theme: this.team.theme,
        common_interest: this.team.common_interest,
        number: this.team.number,
        kakao_chat: this.team.kakao_chat,
      },

      total_number: this.team.total_number,
      autoUpdate: true,
        friends: [],
        isUpdating: false,
        name: 'Midnight Crew',
        people: [
          { header: 'Group 1' },
          { name: 'Sandra Adams', group: 'Group 1'},
          { name: 'Ali Connors', group: 'Group 1'},
          { name: 'Trevor Hansen', group: 'Group 1'},
          { name: 'Tucker Smith', group: 'Group 1'},
          { divider: true },
          { header: 'Group 2' },
          { name: 'Britta Holt', group: 'Group 2'},
          { name: 'Jane Smith ', group: 'Group 2'},
          { name: 'John Smith', group: 'Group 2'},
          { name: 'Sandra Williams', group: 'Group 2'},
        ],
        title: 'The summer breeze',
    }
  },

  computed: {
    ...mapGetters(['currentUser',])
  },

  watch: {
      isUpdating (val) {
        if (val) {
          setTimeout(() => (this.isUpdating = false), 3000)
        }
      },
    },


  methods: {
    ...mapActions(['updateTeam', 'fetchCurrentUser',]),
    onSubmit(){
      const payload = {
        id: this.team.id,
        leader: this.currentUser.id,
        total_number: this.total_number,
        ...this.newTeam,
      }
      this.updateTeam(payload)
      alert("수정되었습니다.")
      }
    },
    remove (item) {
        const index = this.friends.indexOf(item.name)
        if (index >= 0) this.friends.splice(index, 1)
      },

  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style>

</style>