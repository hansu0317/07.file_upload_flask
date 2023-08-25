# Flask 및 필요한 모듈 import
from flask_cors import CORS, cross_origin
from flask import Flask, request
import os

# Flask: 웹 애플리케이션을 생성하는데 사용되는 Flask 클래스
# request: HTTP 요청을 다루는 객체
# os: 파일 및 디렉토리 관련 작업을 다루는 모듈

#Flask 애플리케이션 생성:
app = Flask(__name__)
CORS(app)

# app: Flask 애플리케이션 객체를 생성합니다
# CORS적용


#파일 업로드를 위한 디렉토리 설정
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#UPLOAD_FOLDER: 업로드된 파일을 저장할 디렉토리 이름을 지정
#os.makedirs: 디렉토리를 생성
#app.config['UPLOAD_FOLDER']: Flask 애플리케이션의 설정(config)에 파일 업로드 디렉토리 경로를 저장


#파일 업로드를 처리하는 라우트 설정
@app.route('/upload', methods=['POST'])
@cross_origin()  # 해당 라우트에 CORS 허용
def upload_file():
    # 파일이라는 이름 이없다면 실행하는 코드로써 400을 반환
    if 'file' not in request.files:
        return 'No file part', 400
    
    # 클라이언트가 업로드한 파일을 서버에서 받아옴
    file = request.files['file']
    # request.files: 클라이언트가 업로드한 파일들에 접근할 수 있는 객체
    # ['file']: 업로드된 파일을 가져올 때 사용하는 키
    # 클라이언트가 파일을 업로드할 때, 파일의 이름을 name="file"로 설정한 것
    
    # 클라이언트가 업로드한 파일의 이름이 비어있을 경우(파일이 선택되지않는 경우를 뜻함)
    if file.filename == '':
        return 'No selected file', 400
    
    # 클라이언트가 업로드한 파일을 서버에 저장하고 저장이 완료되었음을 알려준다.
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully'

# @app.route('/upload', methods=['POST']): /upload URL로 POST 요청을 처리하는 라우트 등록
# request.files: 업로드된 파일을 다루기 위한 파일 객체를 얻기
# 업로드된 파일을 저장하기 위해 file.save() 메서드를 사용 
# os.path.join()을 사용하여 업로드 디렉토리와 파일 이름을 결합하여 저장 경로를 생성
# 업로드가 성공하면 'File uploaded successfully' 메시지를 반환


# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
# if __name__ == '__main__':: 이 코드 블록은 현재 스크립트가 직접 실행될 때 사용
# app.run(): 개발 서버를 실행 host와 port 매개변수를 사용하여 서버의 주소와 포트를 지정할 수 있습니다. 
#'0.0.0.0'은 모든 IP 주소에 대한 접속을 허용하는 것을 의미