# 시선 (Seesun, 視先) 


## 1. 데이터 전처리
###  1-a) 신호등
<br/>

####   >>  사용한 dataset
- AI HUB 인도보행영상 데이터셋 Bbox_1
- 구글 이미지 검색
- 직접 촬영한 영상 캡처
<br/>

####   >>  데이터셋 문제점
- 신호등 모양에 뚜렷한 특징이 없음.
- 종류가 다양함
- 빛 번짐 등의 문제로 선명하지 않은 이미지가 다수 포함되어 있음
<br/>

#### >> 해결방법

[ (참고 블로그)데이터 정제방법](#https://crystalcube.co.kr/192) <br/>

**A. 모든 이미지 데이터에 대하여, 선명도를 기준으로 3종류로 분류**  <br/>

   -  매우 선명: clear
   -  선명한 편: neutral
   -  선명하지 않음: ambiguous

**B. 이미지 크기를 비슷한 사이즈로 수정** <br/>

**C. 3종류로 라벨링  (0: 횡단보도)** <br/> 
   - 1 : 빨간불
   - 2 : 초록불
   - 3 : 아무것도 켜지지 않은 상태

###  1-b) 횡단보도

미정


<br/>

## 2. Weight 파일 생성

#### >> 기본 파일 세팅
1. 학습에 사용할 모든 이미지의 경로가 담긴 all_train.txt 생성
2. 보다 정확한 학습을 위해 all_train.txt를 random하게 shuffle한 shuffled.txt 생성
3. shuffled.txt를 weight파일 생성용(train.txt)과 확인용(validation.txt)으로 분류
<br/>

#### >> 학습 환경 세팅
1. Colab Notebooks에 darknet-master 배치
2. darknet-master/data/obj에 학습에 사용할 이미지 배치 <br/>
<img src="https://user-images.githubusercontent.com/62331803/91841952-21838500-ec8e-11ea-8d7a-880b441f3c4c.png" width="40%">
3. darknet-master/에 폴더 'custom' 생성
  -  yolov3-tiny.weights 
  - train.txt
  - validation.txt
  - obj.names
  - obj.data
  - v3-all.cfg
