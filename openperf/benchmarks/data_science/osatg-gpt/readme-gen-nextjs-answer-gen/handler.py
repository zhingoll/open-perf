import json

with open('./meta-sample-data.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

output_lines = []

for item in data:
	sentences = item.get("question", "")
	answer = item.get("answer", "")

	if sentences and answer:
		output_item = {
			"sentences": sentences,
			"answer": answer
		}
		output_lines.append(json.dumps(output_item, ensure_ascii=False))

with open('fine-turning-sample-data.json', 'w', encoding='utf-8') as file:
	for line in output_lines:
		file.write(line + '\n')

print(f"JSON data has been written")
