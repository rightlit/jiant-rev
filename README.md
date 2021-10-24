# jiant NLP toolkit

jiant NLP toolkit 를 활용하여
2021 국립국어원 인공지능언어능력평가에 맞게 수정하여 사용하였습니다.

- 대회자료
    - [https://corpus.korean.go.kr](https://corpus.korean.go.kr/task/taskList.do?taskId=1&clCd=ING_TASK&subMenuId=sub01)


jiant 를 수정한 부분은 아래와 같습니다.

### 예제 수정
1. task 데이터셋 로드 : 
    - 모듈 : ./jiant/scripts/download_data/utils.py
        - 함수 : convert_hf_dataset_to_examples()
            - 데이터셋 로드 변경
    - 모듈 : ./jiant/scripts/download_data/dl_datasets/hf_datasets_tasks.py
        - 변수 : HF_DATASETS_CONVERSION_DICT
            - task 데이터셋 칼럼요소 변경
2. GPT2를 이용한 챗봇(일반대화)
    - 모델 훈련 : [02_chatbot_kogpt2_train.py](https://github.com/rightlit/nlp2/blob/main/examples/02_chatbot_kogpt2_train.py)
    - 모델 시험 : [02_chatbot_kogpt2_test.py](https://github.com/rightlit/nlp2/blob/main/examples/02_chatbot_kogpt2_test.py)
3. GPT2를 이용한 챗봇(건강상담)
    - 모델 훈련 : [03_chatbot_kogpt2_train.py](https://github.com/rightlit/nlp2/blob/main/examples/03_chatbot_kogpt2_train.py)
    - 모델 시험 : [03_chatbot_kogpt2_test.py](https://github.com/rightlit/nlp2/blob/main/examples/03_chatbot_kogpt2_test.py)
- - -
* 트랜스포머(transformers)를 이용한 챗봇 
    - 모델 훈련 : [11_chatbot_transformer_train.py](https://github.com/rightlit/nlp2/blob/main/examples/11_chatbot_transformer_train.py)
    - 모델 시험 : [11_chatbot_transformer_test.py](https://github.com/rightlit/nlp2/blob/main/examples/11_chatbot_transformer_test.py)
