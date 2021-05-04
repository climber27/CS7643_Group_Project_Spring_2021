import json

with open('train2.jsonl', 'r') as json_file:
    json_list = list(json_file)


f = open("memes", "w")

for json_str in json_list:
    result = json.loads(json_str)
    label = result["label"]
    text = result["text"]
    f.write(str(label) + " " + text+"\n")

f.close()
