import datasets
import os
import tarfile
import urllib
import zipfile

import jiant.utils.python.io as py_io
from jiant.utils.python.datastructures import replace_key


def convert_hf_dataset_to_examples(
    path, name=None, version=None, field_map=None, label_map=None, phase_map=None, phase_list=None
):
    """Helper function for reading from datasets.load_dataset and converting to examples

    Args:
        path: path argument (from datasets.load_dataset)
        name: name argument (from datasets.load_dataset)
        version: version argument (from datasets.load_dataset)
        field_map: dictionary for renaming fields, non-exhaustive
        label_map: dictionary for replacing labels, non-exhaustive
        phase_map: dictionary for replacing phase names, non-exhaustive
        phase_list: phases to keep (after phase_map)

    Returns:
        Dict[phase] -> list[examples]
    """

    #is_ko_model = False
    is_ko_model = True

    print('##### load_dataset(), path=', path, ', name=', name)
    #dataset = datasets.load_dataset(path=path, name=name, version=version)
    if(is_ko_model):
        print('##### is_ko_model : ', is_ko_model)
        if(name == 'cola'):
            # column_names =['source',	'acceptability_label',	'source_annotation',	'sentence']
            dataset = datasets.load_dataset('csv', 
                data_files={'train': '/content/NIKL_CoLA_train.tsv', 'validation': '/content/NIKL_CoLA_dev.tsv'}, 
                delimiter='\t',
                column_names =['source',	'label',	'source_annotation',	'sentence'],
                skiprows=1)
        elif(name == 'copa'):
            # column_names =['ID', 'sentence',	'question',	'1',	'2', 'Answer']
            dataset = datasets.load_dataset('csv', 
                data_files={'train': '/content/SKT_COPA_Train.tsv', 'validation': '/content/SKT_COPA_Dev.tsv'}, 
                delimiter='\t',
                column_names =['idx', 'premise',	'question',	'choice1',	'choice2', 'label'],
                skiprows=1)
        elif(name == 'wic'):
            # column_names =['ID', 'Target',	'SENTENCE1',	'SENTENCE2',	'ANSWER', 'start_s1', 'end_s1', 'start_s2', 'end_s2']
            dataset = datasets.load_dataset('csv', 
                data_files={'train': '/content/NIKL_SKT_WiC_Train.tsv', 'validation': '/content/NIKL_SKT_WiC_Dev.tsv'}, 
                delimiter='\t',
                column_names =['idx', 'word',	'sentence1',	'sentence2',	'label', 'start1', 'end1', 'start2', 'end2'],
                skiprows=1)
        elif(name == 'boolq'):
            # column_names =['ID', 'Text',	'Question',	'Answer']
            dataset = datasets.load_dataset('csv', 
                data_files={'train': '/content/SKT_BoolQ_Train.tsv', 'validation': '/content/SKT_BoolQ_Dev.tsv'}, 
                delimiter='\t',
                column_names =['idx', 'passage',	'question',	'label'],
                skiprows=1)
        else:
            print('unsupported ko_model')
    else:
        dataset = datasets.load_dataset(path=path, name=name, version=version)

    if phase_map:
        for old_phase_name, new_phase_name in phase_map.items():
            replace_key(dataset, old_key=old_phase_name, new_key=new_phase_name)
    if phase_list is None:
        phase_list = dataset.keys()
    examples_dict = {}
    for phase in phase_list:
        phase_examples = []
        cnt = 0
        for raw_example in dataset[phase]:
            if field_map:
                for old_field_name, new_field_name in field_map.items():
                    replace_key(raw_example, old_key=old_field_name, new_key=new_field_name)
                    # field check
                    if(cnt < 3):
                        print('##### replace_key(), phase:', phase, 'old_key:', old_field_name, 'new_key:', new_field_name)
                    cnt = cnt + 1
            if label_map and "label" in raw_example:
                # Optionally use an dict or function to map labels
                label = raw_example["label"]
                if isinstance(label_map, dict):
                    if raw_example["label"] in label_map:
                        label = label_map[raw_example["label"]]
                elif callable(label_map):
                    label = label_map(raw_example["label"])
                else:
                    raise TypeError(label_map)
                raw_example["label"] = label
            phase_examples.append(raw_example)
        examples_dict[phase] = phase_examples
    return examples_dict


def write_examples_to_jsonls(examples_dict, task_data_path):
    os.makedirs(task_data_path, exist_ok=True)
    paths_dict = {}
    for phase, example_list in examples_dict.items():
        jsonl_path = os.path.join(task_data_path, f"{phase}.jsonl")
        py_io.write_jsonl(example_list, jsonl_path)
        paths_dict[phase] = jsonl_path
    return paths_dict


def download_and_unzip(url, extract_location):
    """Downloads and unzips a file, and deletes the zip after"""
    _, file_name = os.path.split(url)
    zip_path = os.path.join(extract_location, file_name)
    download_file(url=url, file_path=zip_path)
    unzip_file(zip_path=zip_path, extract_location=extract_location, delete=True)


def unzip_file(zip_path, extract_location, delete=False):
    """Unzip a file, optionally deleting after"""
    with zipfile.ZipFile(zip_path) as zip_ref:
        zip_ref.extractall(extract_location)
    if delete:
        os.remove(zip_path)


def download_and_untar(url, extract_location):
    """Downloads and untars a file, and deletes the tar after"""
    _, file_name = os.path.split(url)
    tar_path = os.path.join(extract_location, file_name)
    download_file(url, tar_path)
    untar_file(tar_path=tar_path, extract_location=extract_location, delete=True)


def untar_file(tar_path, extract_location, delete=False):
    """Untars a file, optionally deleting after"""
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_location)
    if delete:
        os.remove(tar_path)


def download_file(url, file_path):
    # noinspection PyUnresolvedReferences
    urllib.request.urlretrieve(url, file_path)
