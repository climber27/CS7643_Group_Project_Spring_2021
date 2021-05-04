import json
import jsonlines
import shutil

with open('train2.jsonl', 'r') as json_file:
    json_list = list(json_file)

additions = []
found = 0
total = 0

with open("meme_adversaries.txt") as f:
    for line in f:
        if "orig sent" in line:
            total += 1
            orig_text = line.split(":	")[1]
            orig_text = orig_text.replace('\?', '').strip('\n')
            #print(f"Orig text: {orig_text}")

            # Find original label
            for json_str in json_list:
                result = json.loads(json_str)
                label = result["label"]
                text = result["text"].strip('\n')
                #print(f"text: {text}")

                if orig_text == text:
                    found += 1
                    break

        if "adv sent" in line:
            adv_text = line.split(":	")[1]
            adv_text = adv_text.replace('\?', '').strip('\n')
            result["text"] = adv_text
            additions.append(result)

print(f"Found {found} out of {total} for {found/total*100} percent")

shutil.copy('train2.jsonl', 'train_adversarial.jsonl')

with jsonlines.open('train_adversarial.jsonl', mode='a') as writer:
    for i in additions:
        writer.write(i)
