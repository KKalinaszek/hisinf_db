import json

# Read data from data.json
with open('data.json') as json_file:
    data = json.load(json_file)

# Copy 'no' and 'page' to answers if not present
for item in data:
    question = item.get('question')
    answers = item.get('answers', [])
    for answer in answers:
        answer['question'] = answer.get('question', question)

# Move all answers to a single array
all_answers = []
for item in data:
    answers = item.get('answers', [])
    for answer in answers:
        all_answers.append(answer)

# Save answers to a new JSON file
output_file = 'all_answers.json'
with open(output_file, 'w', encoding='utf-8') as json_output:
    json.dump(all_answers, json_output, ensure_ascii=False)

print(f"Data saved to {output_file}")
