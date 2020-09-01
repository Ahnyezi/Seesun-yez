# 시선 (Seesun, 視先) 

## 1. 데이터 전처리
###  1-a) 신호등
####   >>  사용한 dataset
- AI HUB 인도보행영상 데이터셋 Bbox_1
- 구글 이미지 검색
- 직접 촬영한 영상 캡처

####   >>  데이터셋 문제점
- 신호등 모양에 뚜렷한 특징이 없음.
- 종류가 다양함
- 빛 번짐 등의 문제로 선명하지 않은 이미지가 다수 포함되어 있음

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

횡단보도의 전처리 필요여부는  1차 정확도  확인 후 결정


<br/>

## 2. Weight 파일 생성을 위한 기본설정

#### 2-a) 기본 파일 세팅
1. 학습에 사용할 모든 이미지의 경로가 담긴 all_train.txt 생성
2. 보다 정확한 학습을 위해 all_train.txt를 random하게 shuffle한 shuffled.txt 생성
3. shuffled.txt를 weight파일 생성용(train.txt)과 확인용(validation.txt)으로 분류

#### 2-b) 학습 환경 세팅
1. `Colab Notebooks`에 `darknet-master` 배치

2. `darknet-master/data/obj`에 학습에 사용할 이미지 배치 <br/>
<img src="https://user-images.githubusercontent.com/62331803/91841952-21838500-ec8e-11ea-8d7a-880b441f3c4c.png" width="20%"> <br/>

3. `darknet-master/`에 폴더 `custom` 생성
  -  yolov3-tiny.weights | yolo pre-trained weight 파일<br/>
     - 다운경로: https://pjreddie.com/darknet/yolo/

- yolov3-tiny.conv.15 | 커스텀 데이터 맞춤 yolo pre-trained tiny 모델 (추후 설명)
 
  - train.txt | **2-a**에서 생성한 훈련용 데이터 텍스트 파일<br/>
 
  - validation.txt | **2-a**에서 생성한 확인용 데이터 텍스트 파일<br/>
  
  - obj.names | 만들고자하는 weight 파일에서 분류할 class들의 이름<br/>
    <details>
	    <summary>보기</summary>	
  </details>
    
  - obj.data | <br/>
   <details>
	    <summary>보기</summary>  
  </details>

  - v3-all.cfg | 구축할 모델의 layer 세부설정 <br/>
   <details>
	    <summary>보기</summary>  
	- line 1 [net layer] `max batches (반복횟수)`  : 사용할 class개수 * 2000
	- line 1 [net layer] `steps` : max batches의 0.8배, max batches의 0.9배
	- line 123, 167 [Convolutional layer] `filters` : (사용할 class개수 + 5) * 3
	- line 132, 174 [yolo layer] `anchors` :  커스텀 데이터 맞춤 anchor로 설정 (추후 설명)
	- line 132, 174 [yolo layer] `classes` : 사용할 class개수
	
  </details>
   <details>
	    <summary>전체내용확인</summary>  
  </details>

<br/>

## 3. Colab에서 학습파일 생성하기
#### 3-a) 디렉토리 변경, darknet 접근 권한 부여
#### 3-b) darknet 빌드파일 생성
#### 3-c) cfg에 설정할 anchor값 구하기
#### 3-d) 커스텀 데이터에 맞춘 yolo tiny.conv.15 파일 생성
#### 3-e) 훈련 | weight 파일 생성
#### 3-f)  테스트 | validation 파일로 정확도 확인



