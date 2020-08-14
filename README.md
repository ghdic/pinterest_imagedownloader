# pinterest_imagedownloader
핀터레스트 이미지 다운 받는 확장프로그램 최대 50개밖에 지원안해주길래 만들어봄

## 필요한 모듈설치
```
pip install selenium
pip install keyboard
```

# 사용법
## 방법1
headless로 창크기를 엄청나게 크게하여 사진 로드함, 사진이 모두 로드되는걸 기다렸다가 q를 눌러 url를 가져와서 다운받음

> **※주의※** pinterest 로그인한 remote debugger chrome.exe & User Data 랑 chromedriver.exe 준비(반드시 크롬이 켜질때 핀터레스트 로그인이 되어있어야함)

### 리모트 디버거 설정법(필수는 아님)
이미지 로드가 다되었는지 진행상황을 보기위해 리모트 디버거를 사용한다

1. chrome.exe 바로가기를 만들어서준다
1. 속성 -> 대상을 수정해준다 `<username>`은 현재 본인 유저네임으로 넣어주면된다.
    *  ex) `"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default"`
1. 수정해준 바로가기 파일로 크롬을 켜준다.
1. pinterest 사이트에 들어가 로그인을 한뒤, 껏다켜도 로그인이 유지되는지 확인한다.
1. 로그인이 잘 유지되는 경우 창을 모두 꺼준다(9222포트를 애가 가져가기에 꺼줘야된다)
1. 아까만든 크롬바로가기에 속성 -> 대상에 `--headless`도 추가해주고 실행해준다(화면 없음 옵션이기 때문에 반응이 없을것이다)
1. 기존 크롬을 켜주고 주소창에 localhost:9222를 켰을때 정상적으로 켜지면 ok, 깨진글자가 보이거나 안보이면 x(안되는 경우 다른 방법 사용)
1. try: 밑에 link부분만 바꿔주고 실행 "start" 뜨면 제대로 작동하는거(q버튼 누르지 않도록 주의)
1. localhost:9222 에서 이미지 로드가 다되었나 확인 혹은 ctrl+shift+esc 작업관리자로 크롬이 cpu를 더 이상 잡아 먹지 않는다면 이미지 로드가 끝난것
그럼 q버튼을 눌러서 이미지 다운로드를 실행해주자 끝!

> [※위 설명을 잘못따라하겠으면 참조하세요](https://developers.google.com/web/updates/2017/04/headless-chrome)
  
### 리모트 디버거 시용하지 않는 경우
이 경우는 로그인을 하지 않기 때문에 사진 화질이 좀 더 떨어 질 수 있음, 만약 리모트 디버거 설정중 `127.0.0.1:9222`에서 글씨가 깨진 경우는 2번과정부터 해준다(이 경우 로그인 됨)

1. `options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")` 해당 코드를 지워준다
1. 다운받을 link로 try밑에 `downloadPinterestImages("url을 여기에!!")` url을 적어주자
1. "start"가 뜨면 제대로 작동하는것이다.(q버튼 누르지 않도록 주의)
1. ctrl+shift+esc눌러 작업관리자로 크롬(구분을 위해 기존 크롬은 꺼놓자)이 cpu를 더이상 잡아먹지 않으면 이미지 로드가 끝난것이다. q를 눌러서 이미지 다운로드를 실행해주자


## 방법2
마지막까지 스크롤을 일정치만큼 내려서 그때 그때 이미지 url을 가져오는 방법

1. `downloadPinterestImages("email@email.com", "mypassword", "https://www.pinterest.co.kr/krabel019347/menhera-chan/")` 이 부분에 pinterest 이메일, 비밀번호, 다운받을url주소를 입력해준다
1. 단순하지만 단점이 element 로딩속도에 따라(컴퓨터&인터넷속도) SCROLL_PAUSE_TIME을 조정해줘야 에러가 안난다(기본설정 4초) 만약 에러가 난다면 더 높여준다
    * (보여주고 있는 화면만 element가 로드가 되고 더 이상 보이지 않는건 삭제해버리기 때문에.. 삭제가 되기전에 element들을 긁어와줘야 된다)
> ※ 한번에 너무 많이 스크롤 내릴 경우 화면에 노출되지않은 element(사진)은 다운로드가 안되는 경우가 있을수 있다