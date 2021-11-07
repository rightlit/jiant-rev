# jiant NLP toolkit

[jiant NLP toolkit](https://github.com/nyu-mll/jiant) 을 활용하여
2021 국립국어원 인공지능언어능력평가에 맞게 수정하여 사용하였습니다.

모델은 koELECTRA 를 사용하였습니다.

- 대회자료
    - [https://corpus.korean.go.kr](https://corpus.korean.go.kr/task/taskList.do?taskId=1&clCd=ING_TASK&subMenuId=sub01)
- 모델자료
    - [monologg/koelectra-small-v3-discriminator](https://github.com/monologg/KoELECTRA)

jiant 를 수정한 부분은 아래와 같습니다.

### 예제 수정
1. ElectraFast 모델/토크나이저 추가 : 
    - 모듈 : ./jiant/shared/model_resolution.py
        - 변수 : TOKENIZER_CLASS_DICT
            - ElectraFastTokenizer 추가
    - 모듈 : ./jiant/proj/main/modeling/primary.py
        - 함수 : @JiantTransformersModelFactory.register()
            - 모델 등록

2. task 데이터셋 로드 : 
    - 모듈 : ./jiant/scripts/download_data/utils.py
        - 함수 : convert_hf_dataset_to_examples()
            - 데이터셋 로드 변경
    - 모듈 : ./jiant/scripts/download_data/dl_datasets/hf_datasets_tasks.py
        - 변수 : HF_DATASETS_CONVERSION_DICT
            - task 데이터셋 칼럼요소 변경(cola, copa, wic, boolq)

3. 평가결과 제출
    - 모듈 : ./jiant/proj/main/components/evaluate.py
        - 함수 : write_preds()
            - ID, 결과 포멧
