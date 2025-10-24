import json

data = {"nama" : "aufa", "umur" : 17}
json_str = json.dumps(data)
print(json_str)

python_obj = json.loads(json_str)
print(python_obj["nama"])

#nama file jgn sama , misal json.json dan json.py = x
# tp json.json dan belajarjson.py = v