import json
import os

import torch

import jiant.utils.python.io as py_io
import jiant.proj.main.components.task_sampler as jiant_task_sampler

import numpy as np

# added by rightlit
class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def write_val_results(val_results_dict, metrics_aggregator, output_dir, verbose=True):
    full_results_to_write = {
        "aggregated": jiant_task_sampler.compute_aggregate_major_metrics_from_results_dict(
            metrics_aggregator=metrics_aggregator, results_dict=val_results_dict,
        ),
    }
    for task_name, task_results in val_results_dict.items():
        task_results_to_write = {}
        if "loss" in task_results:
            task_results_to_write["loss"] = task_results["loss"]
        if "metrics" in task_results:
            task_results_to_write["metrics"] = task_results["metrics"].to_dict()
        full_results_to_write[task_name] = task_results_to_write

    metrics_str = json.dumps(full_results_to_write, indent=2)
    if verbose:
        print(metrics_str)

    py_io.write_json(data=full_results_to_write, path=os.path.join(output_dir, "val_metrics.json"))

'''
def write_preds(eval_results_dict, path):
    preds_dict = {}
    for task_name, task_results_dict in eval_results_dict.items():
        preds_dict[task_name] = {
            "preds": task_results_dict["preds"],
            "guids": task_results_dict["accumulator"].get_guids(),
        }
    torch.save(preds_dict, path)
'''

def write_preds(eval_results_dict, path, verbose=True):
    preds_dict = {}
    output_preds_dict = {}
    for task_name, task_results_dict in eval_results_dict.items():
        preds_dict[task_name] = {
            "preds": task_results_dict["preds"],
            "guids": task_results_dict["accumulator"].get_guids(),
        }
        print('##### write_preds(), task_name: ', task_name, len(task_results_dict["preds"]))
        print(task_results_dict["preds"])
        print(task_results_dict["accumulator"].get_guids())
        preds_list = task_results_dict["preds"]
        guids_list = task_results_dict["accumulator"].get_guids()
        preds_dic_list = []
        for i, pred in enumerate(preds_list):
            e_dic = {}
            label = int(pred)
            id = guids_list[i]
            e_dic['idx'] = id
            e_dic['label'] = label
            preds_dic_list.append(e_dic)
        print('##### preds_dic_list: ', preds_dic_list)
        output_preds_dict[task_name] = preds_dic_list
        
    #torch.save(preds_dict, path)
    print('##### write_json to : ', path)

    with open(path, "w") as f:
    #json.dump(preds_dic_list, f, indent=2)
    json.dump(output_preds_dict, f, indent=4)

    '''
    #py_io.write_json(data=preds_list_dic, path=path)
    #py_io.write_json(data=preds_dict, path=path)
    dumped = json.dumps(data=preds_list_dic, cls=NumpyEncoder)
    # using py_io
    py_io.write_file(dumped, path)
    '''
    
