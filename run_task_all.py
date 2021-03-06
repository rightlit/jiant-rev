# run_task_all (cola, copa, wic, boolq)
from jiant.proj.simple import runscript as run
import jiant.scripts.download_data.runscript as downloader

EXP_DIR = "exp"
MODEL_PATH = "monologg/koelectra-base-v3-discriminator"

# predictions to file (cola)
def predict_cola():
    # Download the Data
    downloader.download_data(["cola"], f"{EXP_DIR}/tasks")

    # Set up the arguments for the Simple API
    args = run.RunConfiguration(
       run_name="simple",
       exp_dir=EXP_DIR,
       data_dir=f"{EXP_DIR}/tasks",
       hf_pretrained_model_name_or_path=MODEL_PATH,
       tasks="cola",
       train_batch_size=16,
       num_train_epochs=3,
       write_test_preds=True,
       model_weights_path='model/best_model_cola.p',
       do_train=False,
    )

    # Run!
    run.run_simple(args)

# predictions to file (copa)
def predict_copa():
    # Download the Data
    downloader.download_data(["copa"], f"{EXP_DIR}/tasks")

    # Set up the arguments for the Simple API
    args = run.RunConfiguration(
       run_name="simple",
       exp_dir=EXP_DIR,
       data_dir=f"{EXP_DIR}/tasks",
       hf_pretrained_model_name_or_path=MODEL_PATH,
       tasks="copa",
       train_batch_size=16,
       num_train_epochs=3,
       write_test_preds=True,
       model_weights_path='model/best_model_copa.p',
       do_train=False,
    )

    # Run!
    run.run_simple(args)

# predictions to file (wic)
def predict_wic():
    # Download the Data
    downloader.download_data(["wic"], f"{EXP_DIR}/tasks")

    # Set up the arguments for the Simple API
    args = run.RunConfiguration(
       run_name="simple",
       exp_dir=EXP_DIR,
       data_dir=f"{EXP_DIR}/tasks",
       hf_pretrained_model_name_or_path=MODEL_PATH,
       tasks="wic",
       train_batch_size=16,
       num_train_epochs=3,
       write_test_preds=True,
       model_weights_path='model/best_model_wic.p',
       do_train=False,
    )

    # Run!
    run.run_simple(args)

# predictions to file (boolq)
def predict_boolq():
    # Download the Data
    downloader.download_data(["boolq"], f"{EXP_DIR}/tasks")

    # Set up the arguments for the Simple API
    args = run.RunConfiguration(
       run_name="simple",
       exp_dir=EXP_DIR,
       data_dir=f"{EXP_DIR}/tasks",
       hf_pretrained_model_name_or_path=MODEL_PATH,
       tasks="boolq",
       train_batch_size=16,
       num_train_epochs=3,
       write_test_preds=True,
       model_weights_path='model/best_model_boolq.p',
       do_train=False,
    )

    # Run!
    run.run_simple(args)

# merge prediction(ALL)
# cola, copa, wic, boolq
import json
import os
import jiant.utils.python.io as py_io

def merge_results_all():
    data_dir = 'exp/runs/simple'
    result_files_dic = {'cola':'test_preds.p.cola', 
                'copa':'test_preds.p.copa', 
                'wic':'test_preds.p.wic',
                'boolq':'test_preds.p.boolq'}

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

# BEGIN_MAIN
#
# CoLA
predict_cola()
# COPA
predict_copa()
# WiC
predict_wic()
# BoolQ
predict_boolq()

# merge json output
merge_results_all()
