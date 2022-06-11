// 서버 호스트
const HOST = 'http://localhost:8000/'

// local app
const ACCOUNTS = 'accounts/'
const TEAMS = 'teams/'

export default {
  // accounts
  accounts: {
    // 로그인
    login: () => HOST + 'account/login/',
    // 로그아웃
    logout: () => HOST + 'account/logout/',
    // 회원가입
    signup: () => HOST + 'account/signup/',
    // 회원탈퇴
    signout: () => HOST + 'accounts/signout/',
    // 사용자 조회/수정
    mypage: () => HOST + ACCOUNTS + `${userId}/mypage/`, 
    // 북마크 조회/등록/해제
    bookmark: () => HOST + ACCOUNTS + `${userId}/bookmark/`,
    // 개별 사용자 조회
    userprofile: () => HOST + ACCOUNTS + `${userId}/`,

  },
  
  // teams
  teams: {
    // 전체 팀 조회
    teams: () => HOST + TEAMS,
    // 개별 팀 조회 및 수정
    myteam: () => HOST + TEAMS + `${teamId}/`,
    // 팀 생성
    teamcreate: () => HOST + TEAMS + 'create/',

  }
}