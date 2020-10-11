from sanic import Sanic
from sanic.response import json, html
from sanic_cors import CORS, cross_origin
from SpotMicro import SpotMicroDriver
import os

driver = SpotMicroDriver(2)

app = Sanic("jetson_host")
CORS(app)
app.static('/', './dist')
app.static('/_nuxt', './dist/_nuxt')

@app.route("/")
async def test(request):
    template = open(os.getcwd() + "/dist/index.html")
    return html(template.read())

@app.route("/power", methods=["POST", "OPTIONS"])
async def test_power(request):
    board = request.json["board"]
    channel = request.json["channel"]
    angle = request.json["angle"]
    driver.set_servo_angle(board, channel, angle)
    return json({"angle": angle, "board": board, "channel": channel})

@app.route("/rest", methods=["POST", "OPTIONS"])
async def set_configuration(request):
    servos_1 = request.json["PCA9865_1"]
    servos_2 = request.json["PCA9865_2"]
    servo_list_1 = [_ for _ in servos_1]
    servo_list_2 = [_ for _ in servos_2]
    large_list = servo_list_1 + servo_list_2
    for servo in large_list:
        driver.set_servo_angle(servo["board"], servo["port"], servo["angle"])
    return json({}, status=200)

@app.route("/profile", methods=["POST", "OPTIONS"])
async def set_profile(request):
    servos = request.json["servos"]
    for servo in servos:
        print(servo)
        angle = servo["rest_angle"]
        board_id = servo["board"]
        port = servo["channel"]
        driver.set_servo_angle(board_id, port, angle)
    return json({}, status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


