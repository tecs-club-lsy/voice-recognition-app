from flask import Flask, render_template
from flask_cors import CORS
from flask_sock import Sock

app = Flask(__name__,
    template_folder='./www',
    static_folder='./www',
    static_url_path='/'
)
CORS(app)  # 모든 도메인에서의 접근을 허용
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

@sock.route('/audio')
def handle_audio(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        
        # 1차 스프린트에서는 간단한 에코 기능만 구현
        ws.send("음성을 수신했습니다. 1차 스프린트에서는 처리하지 않습니다.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
