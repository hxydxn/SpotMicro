from sanic import Sanic
from sanic.response import json, html
import os

app = Sanic("jetson_host")
app.static('/', './dist')
app.static('/_nuxt', './dist/_nuxt')

@app.route("/")
async def test(request):
    template = open(os.getcwd() + "/dist/index.html")
    return html(template.read())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)