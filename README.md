# branch rule
- 반드시 새 branch에서 작업하고, pull request를 통해 merge하도록 합니다.
- PR시에는 운영진에게 review 받도록 합니다.
- 절대로 master branch에 직접 commit하지 않습니다.

# task
1. MVP 테스트를 위한 one-page 사이트를 만듭니다. \
목표는 서비스 설명과 이메일 수집입니다.

2. views.py urls.py templates에서 작업하면 됩니다. example을 참고합니다.
3. 작업 완료 후 master에 merge 되고 나면 `fab deploy` 명령어를 통해 배포합니다.
4. 작업 결과물은 `~/example` 과 같은 url을 가질 수 있도록 합니다.
5. 배포 후에는 http://product.hanqyu.com/example 에서 확인할 수 있습니다.
6. 수집된 이메일은 별도로 전달해드릴 예정입니다.

# 작업시 주의사항
1. static 파일은 `ceos_mvp/static/core/{서비스명}/{파일명}`에 저장합니다.
2. templates 파일은 `ceos_mvp/templates/core/{서비스명}/{파일명}`에 저장합니다.
3. views.py와 urls.py의 함수도 본인의 서비스명을 사용합니다.


# 배포시 필요사항
- slack에 공유된 deploy.json 파일을 자신의 프로젝트 폴더에 복사
- ceos_developers.pem 파일을 자신의 `~/.ssh/` 폴더에 복사


# git 또는 django 초심자라면
1. 이 레포지토리를 적절한 폴더에 clone합니다.
2. `pip install -r requirements.txt` 명령어를 통해 필요한 pip 패키지를 설치합니다
3. `git checkout -b {브랜치명}` 을 통해 새 브랜치를 생성합니다.
4. 개발하면서 결과물은 `python manage.py runserver` 를 통해 확인할 수 있습니다