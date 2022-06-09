from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        # super()를 사용하여 부모의 데이터(기본 데이터)를 저장
        user = super().save_user(request, user, form, False)
        # 저장하고자 하는 추가 필드를 아래와 같이 여러 개 정의한 다음 user의 속성 값에 할당
        # user의 속성 값은 우리가 지정한 데이터 필드 이름
        sex = data.get("sex")
        region = data.get("region")
        position = data.get("position")
        major = data.get("major")
        group = data.get("group")
        nickname = data.get("nickname")
        img = data.get("img")
        intro = data.get("intro")
        kakao_chat = data.get("kakao_chat")
        github_url = data.get("github_url")
        portfolio_url = data.get("portfolio_url")
        strength = data.get("strength")
        
        if sex:
            user.sex = sex
        if region:
            user.region = region
        if position:
            user.position = position
        if major:
            user.major = major
        if group:
            user.group = group
        if nickname:
            user.nickname = nickname
        if img:
            user.img = img
        if intro:
            user.intro = intro
        if kakao_chat:
            user.kakao_chat = kakao_chat
        if github_url:
            user.github_url = github_url
        if portfolio_url:
            user.portfolio_url = portfolio_url
        if strength:
            user.strength = strength

        user.save() # 저장
        return user