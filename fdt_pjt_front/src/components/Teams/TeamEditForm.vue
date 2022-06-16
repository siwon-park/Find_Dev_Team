<template>
  <v-app>
    <h4>팀 수정 폼</h4>
    <p>{{ currentUser }}</p>
    <p>{{ allUsers}}</p>
    {{team}}
    {{people}}
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
      <!-- 팀 멤버 등록 -->
      <!-- 팀 멤버:
        <label for="team_member"></label>
        <input type="text" v-model="newTeam.team_member" placeholder="team_member" id="team_member"> -->
      <div>
        <v-card :loading="isUpdating">
          <v-form>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <!-- item-text : 객체의 키를 알려줌, item-value : 객체의 실제 키를 지정 -->
                  <v-autocomplete
                    v-model="newTeam.team_member"
                    :disabled="isUpdating"
                    :items="people" 
                    filled
                    chips
                    label="team_member"
                    multiple
                    item-text="name"
                    item-value="name"
                  >
                  <!-- 이름 목록 -->
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
                        {{ data.item }}
                      </v-chip>
                    </template>
                    
                    <template v-slot:item="data">
                      <template v-if = "typeof data.item !== 'object'">
                        <v-list-item-content v-text="data.item"></v-list-item-content>
                      </template>
                      <template v-else>
                        <v-list-item-avatar>
                          <img :src="data.item.avatar">
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title v-html="data.item.name"></v-list-item-title>
                        </v-list-item-content>
                        
                      </template>
                    </template>
                    
                  </v-autocomplete>

                </v-col>
              </v-row>
            </v-container>
          </v-form>
          <!-- 버튼 -->
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
      </div>
      <!-- 끝 -->
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

  </v-app>
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
      friends: ['박시원'],
      isUpdating: false,
      // 팀 넣고, 사용자 목록 출력
      people: [{id:4, username: "test4"},{id: 10, username: '김철수'}, {id: 11, username: '박영희'}],
        

    }
  },

  computed: {
    ...mapGetters(['currentUser', 'allUsers',]),


  },

  watch: {
      isUpdating (val) {
        if (val) {
          setTimeout(() => (this.isUpdating = false), 3000)
        }
      },
    },


  methods: {
    ...mapActions(['updateTeam', 'fetchCurrentUser', 'fetchAllUsers']),
    onSubmit(){
      const payload = {
        id: this.team.id,
        leader: this.currentUser.id,
        total_number: this.total_number,
        common_interest: this.newTeam.common_interest,
        ...this.newTeam,
      }
      this.updateTeam(payload)
      alert("수정되었습니다.")
      },
      selectOne(item) {
        console.log("hi")
        this.data.select
        this.newTeam.team_member.push(item)
      },

      remove (item) {
        console.log(item)
        const index = this.newTeam.team_member.indexOf(item.name)
        if (index >= 0) this.newTeam.team_member.splice(index, 1)
      },
    },
    // add_user(){
    //   for (const i of this.allUsers) {
    //     people.push(i)
    //   }
    //   return people
    // },


  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style>

</style>