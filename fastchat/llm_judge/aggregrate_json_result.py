import os
import json
import sys

prefix = sys.argv[1]
total_score = [0, 0, 0, 0]
write_file = open('mt_bench_70b_evaluative.jsonl', 'w')

superset_d = {}
i, error = 0, 0
for f in os.listdir('data/mt_bench/model_judgment/'):
    if f.startswith(prefix):
        for line in open('data/mt_bench/model_judgment/' + f):
            d = json.loads(line.strip())
            question_id = str(d['question_id']) + '_' + str(d['turn'])
            if question_id not in superset_d:
                superset_d[question_id] = []
            prompt = d['user_prompt']
            if d['turn'] == 1:
                content = prompt.split('[Question]\n')[1].strip()
            else:
                content = prompt
            superset_d[question_id].append((d['score'], content))

average_score_list = []
new_d = {}
for item in superset_d.keys():
    average_score = sum(int(val[0]) for val in superset_d[item]) / 4
    average_score_list.append(average_score)
    new_d['question_id'] = item
    max_val, min_val = -100, 100
    max_item, min_item = None, None
    for stuff in superset_d[item]:
        score, content = stuff
        if score > max_val:
            max_val = score
            max_item = content
        if score < min_val:
            min_val = score
            min_item = content
    new_d['max_score'] = max_val
    new_d['min_score'] = min_val
    new_d['max_value'] = max_item
    new_d['min_value'] = min_item
    if max_val != min_val and max_item == min_item:
        error += 1
    write_file.write(json.dumps(new_d) + '\n')

print(error)
print(round(float(sum(average_score_list)) / len(average_score_list), 2))
