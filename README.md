# jiant NLP toolkit

jiant NLP toolkit 를 활용하여
2021 국립국어원 인공지능언어능력평가에 맞게 수정하여 사용하였습니다.

- 대회자료
    - [https://corpus.korean.go.kr](https://corpus.korean.go.kr/task/taskList.do?taskId=1&clCd=ING_TASK&subMenuId=sub01)


jiant 를 수정한 부분은 아래와 같습니다.

### 예제 구성
1. BERT 를 이용한 분류
    - 모델 훈련 : [01_bert_train.py](https://github.com/rightlit/nlp2/blob/main/examples/01_bert_train.py)
      - Google BERT 모델 다운로드, NSMC 데이터셋 전처리 후 구동 (01_bert_train.ipynb 참고)
      - BERT 기본 모델 : https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip
      - NSMC 데이터셋 : https://github.com/e9t/nsmc
    - 모델 시험 : [01_bert_test.py](https://github.com/rightlit/nlp2/blob/main/examples/01_bert_test.py)
      - 학습모델 다운로드 후 구동
2. GPT2를 이용한 챗봇(일반대화)
    - 모델 훈련 : [02_chatbot_kogpt2_train.py](https://github.com/rightlit/nlp2/blob/main/examples/02_chatbot_kogpt2_train.py)
      - Chatbot 데이터셋 전처리 후 구동 (02_chatbot_kogpt2_train.ipynb 참고)
      - Chatbot 데이터셋 : https://github.com/songys/Chatbot_data
    - 모델 시험 : [02_chatbot_kogpt2_test.py](https://github.com/rightlit/nlp2/blob/main/examples/02_chatbot_kogpt2_test.py)
      - 학습모델 다운로드 후 구동
3. GPT2를 이용한 챗봇(건강상담)
    - 모델 훈련 : [03_chatbot_kogpt2_train.py](https://github.com/rightlit/nlp2/blob/main/examples/03_chatbot_kogpt2_train.py)
      - Wellness 데이터셋 전처리 후 구동 (03_chatbot_kogpt2_train.ipynb 참고)
      - Wellness 데이터셋 : https://github.com/nawnoes/WellnessConversation-LanguageModel
    - 모델 시험 : [03_chatbot_kogpt2_test.py](https://github.com/rightlit/nlp2/blob/main/examples/03_chatbot_kogpt2_test.py)
      - 학습모델 다운로드 후 구동
- - -
* 트랜스포머(transformers)를 이용한 챗봇 
    - 모델 훈련 : [11_chatbot_transformer_train.py](https://github.com/rightlit/nlp2/blob/main/examples/11_chatbot_transformer_train.py)
    - 모델 시험 : [11_chatbot_transformer_test.py](https://github.com/rightlit/nlp2/blob/main/examples/11_chatbot_transformer_test.py)
