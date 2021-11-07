# merge prediction(ALL)
# cola, copa, wic, boolq
import json
import os
import jiant.utils.python.io as py_io

#data_dir = '/content/jiant-rev/exp/runs/simple'
data_dir = './exp/runs/simple'

result_files_dic = {'cola':'test_preds.p.cola', 
                'copa':'test_preds.p.copa', 
                'wic':'test_preds.p.wic',
                'boolq':'test_preds.p.boolq'}

#result_files_dic = { 
#                'wic':'test_preds.p.wic',
#                'boolq':'test_preds.p.boolq'}

preds_output_dic = {}
for task_name, result_file in result_files_dic.items():
    filepath = os.path.join(data_dir, result_file)
    result_dic = py_io.read_json(filepath)
    preds_output_dic[task_name] = result_dic[task_name]
    print('task results added : ', task_name, len(result_dic[task_name]))

output_file = 'test_preds.p.ALL'
output_path = os.path.join('.', output_file)
print('write to output_flle : ', output_path)

with open(output_path, "w") as f:
    json.dump(preds_output_dic, f, indent=2)