# 1. 마이크와 스피커 설정 
# https://diy-project.tistory.com/88 위 링크에서 마이크만 설정하면 됨

# pygame 설치, rpi.gpio 설치
# 구글 STT 프로젝트 활성화 방법
# https://console.actions.google.com/ 으로 들어가서 New Project를 클릭
![1](https://user-images.githubusercontent.com/72368472/100541428-4daba380-3287-11eb-98ac-f596f4b41bf2.jpg)
# 영어로 프로젝트 이름을 입력한뒤 언어와 국가를 한국으로 설정하고 CREATE PROJECT 클릭
# 프로젝트 종류를 고르는 창에서 맨 밑으로 내려가 device registration 을 클릭
# https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview 에서 검색창에 speech 를 검색해 STT를 활성화
# 그리고 결제수단을 등록해야 한다.
# 활성화후 왼쪽 메뉴의 사용자 인증 정보 클릭후 OAuth 동의화면으로 넘어가 정보를 적은뒤 저장을 누르기
# https://myaccount.google.com/activitycontrols 로 들어가 Web & App Activity, Device Information, Voice & Audio Activity 활성화
# 다시 Google Action Console로 돌아와서 왼쪽 메뉴바의 Device registration을 클릭한다.
![2](https://user-images.githubusercontent.com/72368472/100541431-4edcd080-3287-11eb-9316-557237936f14.jpg)
# 그곳에서 Device type는 적당하게 Light로 설정하고 REGISTER MODEL을 클릭해 넘어가면 된다.
# 다음 화면에서 Download OAuth 2.0 credentials를 클릭해 .json파일을 내려받은 후 컴퓨터 적당한 곳에 저장해두자. 단 반드시 파일의 이름을 변경해서는 안된다.
# 또 다음화면에서는 모델 ID를 잘 기억해 두자



# 2. 구글 stt를 실행시키기 위해서 다음과 같은 명령어를 실행(가상환경 설정)
#      $ sudo apt-get update

#      $ sudo apt-get install python3-dev python3-venv

#      $ python3 -m venv env

#      $ env/bin/python -m pip install --upgrade pip setuptools wheel

# 서비스 계정키 만들기
# https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.40899618.-1016148464.1531368544 로 들어가서 새 서비스 계성을 누르고 키 유형은 JSON을 선택한다. 이때 #역활은 프로젝트의 소유자로 설정한다. 완료되면 생성 버튼을 누른다. 그 후 파일을 라즈베리파이의 바탕화면으로 옮긴다.

# 3. pyaudio 설치 방법  
#    $ sudo apt-get update

 #   $ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
 #   $ sudo apt-get install python-dev

# 방법 1.
 #   $ sudo pip install pyaudio
 
 
# $ source env/bin/activate 로 가상환경을 킨다

# (env) $ cd osscap2020/samples/microphone 으로 디렉토리를 옮긴다

#  (env) $ pip install -r requirements.txt 을 쳐서 설치를 끝낸다.

# 그후 googlestt.py 에 있는 os.system('export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/Desktop/FILES"') 에서 FILES 부분에 아까 받은 .json 파일의 이름을 쓰고 저장한다.

# 그리고 난뒤 (env) $ led_galaga.py 를 실행하면 된다.
