import json
import quart_cors
import quart
from quart import request, Response
import requests

app = quart_cors.cors(quart.Quart(__name__),
                      allow_origin="https://chat.openai.com")


@app.post("/weather")
async def get_weather():
  req_data = await request.get_json(force=True)
  city = req_data["city"]
  api_key = "YOUR API KEY HERE"
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
  response = requests.get(url)
  return Response(response=json.dumps(response.json()), status=200)


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
  host = request.headers['Host']
  with open("ai-plugin.json") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
  host = request.headers['Host']
  with open("openapi.yaml") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return Response(text, mimetype="text/yaml")


def main():
  app.run(debug=True, host="0.0.0.0", port=5002)


if __name__ == "__main__":
  main()
