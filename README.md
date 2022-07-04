# Where is My Team

### 🚀프로젝트 개요

- 프로젝트 기획 의도

  - 프로젝트 팀을 찾기 위한 개발자 정보 제공 프로젝트
  - 나의 개발 능력을 나타내고 팀의 역량을 드러내어 쌍방으로 소통할 수 있는 사이트
  - 본인의 개발 역량 정보를 제공하고 다른 사람들의 개발 역량 정보를 확인하여 프로젝트 팀 구성에 도움을 주기 위한 프로젝트

- 기획 의도

  - 사용자가 등록한 개발 역량 표시
  - 팀 구성을 위한 이메일/메시지/DM 기능
  - HTML, CSS, JavaScript, Bootstrap, Vue.js, REST API, Database 등을 활용한 실제 서비스 설계
  - SSAFY 7기 배포
    - 피드백 점검
    - 서비스 관리 및 유지 보수

- 진행 일정 : 22.06.20 ~ 22.07.04

- 주요 기능

  - 팀 멤버 추가를 위한 자동 검색 및 완성 기능
  - 관심있는 팀원을 즐겨찾기하는 기능

- 향후 계획

  - 미흡한 부분 유지보수
  - 배포 후 피드백

  

### 👩🏻‍💻역할

| 이름   | 구현 기능                                                    | Github                        |
| ------ | ------------------------------------------------------------ | ----------------------------- |
| 박시원 | 1. 전체 프론트 기능 구현<br />2. 백엔드 로직 테스트<br />3. 버그 및 성능 개선<br /> | https://github.com/siwon-park |
| 이현정 | 1. DB 설계 및 API 테스트<br />2. 프론트엔드 디자인 설계<br />3. 팀 페이지 및 로그인/로그아웃 프론트 기능 구현<br /> | https://github.com/lhynjn9    |



### 🛠 프로젝트 명세

- Tech Stack

![image](https://user-images.githubusercontent.com/93081720/170559780-a977ed18-e589-4ffd-bb49-2f24d92cdeac.png)



- 기능 명세서 및 API 설계

  ![캡처](https://user-images.githubusercontent.com/97647987/177174607-3b8c0de4-0a36-48b2-b32b-ba86e0d994fd.JPG)

  

- 데이터베이스 모델링(ERD)

  ![image-20220609215301830](https://user-images.githubusercontent.com/97647987/174428289-757c5b86-5a74-4b5b-90b8-c9d70002f214.png)

- 컴포넌트 설계

  ![unknown](https://user-images.githubusercontent.com/97647987/175553416-599fdf93-07fd-4e87-a7f0-0a17cf294698.png)

  

- 서비스 플로우 차트

  ![unknown](https://user-images.githubusercontent.com/97647987/175549772-ef0490ac-26bf-4b1b-aeb8-245ecb88a258.png)

  

- 구현 서비스

![캡처](https://user-images.githubusercontent.com/97647987/177174859-301c3e02-db77-4f72-a68a-da9ad51c0dee.JPG)



- 구현 서비스 소개



### 🚔 프로젝트 회고

- 배운점

  | NO.  | Content                                                      |
  | ---- | ------------------------------------------------------------ |
  | 1    | - OneToOneField : 1:1 외래키 관계 설정                       |
  | 2    | 1. 기본 재정의 : adapter 정보 : 정보 저장용<br />2. 회원 가입 필드는 회원가입에 들어가야 하는 필드만 받아 올 수 있게 새로 serializer 정의(Register serializer 사용)<br />3. static, media file의 차이점<br />- static : 개발자가 준비해놓은 파일<br />- media : 사용자가 업로드한 파일 |
  | 3    | - Related Manager is not Iterable; 예) team.team_member는 related manager이기 떄문에 for 구문으로 반복이 불가능하다. |
  | 4    | - Related Manager와 같은 쿼리셋에는 인스턴스를 넣어야만 한다. 딕셔너리의 출력형태가 인스턴스와 똑같이 생겼다고해서 딕셔너리를 넣을 수는 없다(TypeError발생) |
  |      |                                                              |

  


- 이슈관리

  | No.  | Name | Content                                                      | Solve | follow-up |
  | ---- | ---- | ------------------------------------------------------------ | ----- | --------- |
  | 1    |      | print(team.team_member) = accounts.User.None                 |       |           |
  | 2    |      | team 수정에서 팀 맴버에 다른 유저 추가할 시, DB에 데이터가 들어가지 않음 | Yes   |           |
  | 3    |      | 왜 데이터가 날아가지 않는가?.?                               |       |           |
  |      |      |                                                              |       |           |
  |      |      |                                                              |       |           |

  

- 느낀점

  
