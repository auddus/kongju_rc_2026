from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from car_controller import CarController
from camera_controller import CameraController
from sound_controller import SoundController
import time

app = Flask(__name__)
CORS(app)

car = CarController()
cam = CameraController()
snd = SoundController()

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "running",
        "speed": car.speed,
        "steering": car.steering,
        "pan": cam.pan,
        "tilt": cam.tilt
    })

@app.route('/api/drive', methods=['POST'])
def joystick_drive():
    data = request.json or {}
    speed = int(float(data.get('y', 0)) * 100)
    angle = int(float(data.get('x', 0)) * 45)
    car.set_motor(speed)
    car.set_steering(angle)
    return jsonify({"message": "success"})

@app.route('/api/camera/pan_tilt', methods=['POST'])
def control_pan_tilt():
    data = request.json or {}
    p, t = cam.set_pan_tilt(int(data.get('pan', 90)), int(data.get('tilt', 90)))
    return jsonify({"pan": p, "tilt": t})

@app.route('/api/sound/tts', methods=['POST'])
def speak_tts():
    data = request.json or {}
    snd.speak_tts(data.get('text', 'hello'))
    return jsonify({"message": "success"})

@app.route('/api/stop', methods=['POST'])
def stop_car():
    car.stop()
    return jsonify({"message": "Emergency Stop"})

@app.route('/video_feed')
def video_feed():
    # 실제 카메라가 연결되면 OpenCV 프레임을 전송하는 로직으로 교체됨
    def gen():
        while True:
            time.sleep(0.1)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + b'DUMMY_DATA' + b'\r\n')
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    