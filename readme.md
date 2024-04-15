# 인스타그램 클론 프로젝트
- pip install djangorestframework  
- pip install django

- django
    - MVT ( model , view , Template )
        - view : 데이터 처리 
        - model : ex 회원(id,pw,...)

- Migraion 
    - SQL 을 수동으로 작성할 필요없이 데이터베이스 스키마 변경 사항을 처리
    - python manage.py makemigrations ( migration 생성)
    - python manage.py migrate ( migrate 실행 ) -> 코드에 있던 객체들이 db 에 생김( SQLITE , 앱이름 _ 클래스이름.db)

- django rest-framwork 설치
    - pip install djangorestframework
    - url -> views.py -> templates/main.html

- TemplateDoesNotExist 오류 
    - 1. 폴더명이 templates 이 맞는지 확인
    - 2. settings - install apps 에 app 이름 추가 
    - 3. 그래도 안되면 template url 에 비어있는 [] 에 강제로 경로 추가 <- 이렇게 했음. 

- 모달 만들기 

- image 파일 관리하기위해 media 폴더만들고 urlpatterns 추가

- 이제 이미지가 랜덤 파일명으로 db 에 저장되므로 html 에서 {{Feed.image}} 앞에 {% get_media_prefix %} 를 붙여준다. 
    -> 이때 html head 에 {% load static %} 를 명시해주어야 작동한다. 

- BaseUser DB 를 상속받아서 Custom user db 만들기

- 커스텀 유저 모델을 사용하기 위해 settings 설정
    - AUTH_USER_MODEL = 'user.User'
    - models.py 에는 USERNAME_FIELD = 'nickname' ( unique 필드로 설정해야함 )

- 앱별로 url 을 나눠 주었음 ( include 사용 )
    -> 앞에 자동으로 앱 이름이 붙어서 content/upload 나 user/join 인줄 알았는데 앱이름 디폴트로 안붙음. 

- make_password 함수를 사용해서 비밀번호 생성

- 회원 가입 데이터 전송은 json 타입으로 , 타입도 명시해주었음 

- 사진 업로드시 Onchange() : 뭔가 변경사항이 있을때 ( 파일명이 들어온다던지 ) 특정함수 실행가능 

- ajax 로 보낼때 , 매핑된 url 과 다를경우 오류 났음. 그냥 똑같이 맞춰줌