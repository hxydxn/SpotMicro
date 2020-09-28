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
    return json({"data": f'{board}-{channel}-{angle}'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)