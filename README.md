# 딥러닝 프로젝트 | 시선 (Seesun, 視先) 

### 목차
#### 1. 프로젝트 개요
<br/>

#### 2. 개발절차
##### 2-1)  [신호등/횡단보도 탐지 YOLO  커스텀 파일 생성](#2-1---신호등/횡단보도-탐지-YOLO--커스텀-파일-생성)
##### 2-2)  Android로 YOLO 돌리기
##### 2-3)  TTS(Text To Speech)로 음성안내
##### 2-4)  횡단보도 방향 탐지
##### 2-5) Tesseract로 신호등 잔여시간 탐지


<br/><br/>

## 1. 프로젝트 개요

<br/>

## 2 . 개발절차
### 2-1)  신호등/횡단보도 탐지 YOLO  커스텀 파일 생성

#### A. 신호등/횡단보도 데이터 수집
1.  [AI HUB | 인도보행 영상 데이터셋](#http://www.aihub.or.kr/aidata/136)<br/>
<img src = "https://user-images.githubusercontent.com/62331803/92255342-23a74700-ef0d-11ea-8af3-c494e689811e.png" width="70%"> <br/>
   - 이미지 예시 <br/>
   <img src = "https://user-images.githubusercontent.com/62331803/92255689-a7613380-ef0d-11ea-8992-5892a0e4d2bb.png" width="50%"> <br/>

2.  [중국 횡단보도 이미지 | ImVisible 데이터셋 ](#https://github.com/samuelyu2002/ImVisible)<br/>
<img src = "https://user-images.githubusercontent.com/62331803/92256060-2b1b2000-ef0e-11ea-8276-499e0285258a.png" width="70%"> <br/>

3.  핸드폰으로 직접 촬영한 이미지<br/>
<img src = "https://user-images.githubusercontent.com/62331803/92256313-89480300-ef0e-11ea-8b06-dc7292d33740.png" width="30%"> 

<br/>

#### B. YOLO 커스텀 파일 생성을 위한 기본설정
> Weight 파일 생성을 위한 기본설정

#### > 기본 파일 세팅
1. 학습에 사용할 모든 이미지의 경로가 담긴 all_train.txt 생성
2. 보다 정확한 학습을 위해 all_train.txt를 random하게 shuffle한 shuffled.txt 생성
3. shuffled.txt를 weight파일 생성용(train.txt)과 확인용(validation.txt)으로 분류


#### > 학습 환경 세팅
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

	- line 1 [net layer] `max batches (반복횟수)`  : 사용할 class개수 * 2000
	- line 1 [net layer] `steps` : max batches의 0.8배, max batches의 0.9배
	- line 123, 167 [Convolutional layer] `filters` : (사용할 class개수 + 5) * 3
	- line 132, 174 [yolo layer] `anchors` :  커스텀 데이터 맞춤 anchor로 설정 (추후 설명)
	- line 132, 174 [yolo layer] `classes` : 사용할 class개수

   <details>
	    <summary>전체내용확인</summary>  
  </details>

<br/>

> Colab에서 학습파일 생성하기
1. 디렉토리 변경, darknet 접근 권한 부여
2. darknet 빌드파일 생성
3. cfg에 설정할 anchor값 구하기
4. 커스텀 데이터에 맞춘 yolo tiny.conv.15 파일 생성
5. 훈련 | weight 파일 생성
6. 테스트 | validation 파일로 정확도 확인

<br/>

#### C. 신호등/횡단보도 YOLO 커스텀 파일 학습시키기

> 1,2차시도 | custom1,2 <br/>
#### > 학습계획
- 각 데이터를 정제없이 사용하여, 신호등과 횡단보도 yolo 모델을 각각 생성
  - 신호등 데이터: 인도보행영상의 Bbox_1, Bbox_2, Bbox_3, Bbox_4
  - 횡단보도 데이터: ImVisible 데이터셋
 
####  > 내 데이터 학습 결과 (TEST용)
<details>
	<summary> 보기 </summary>
			
  - **비정상적**인 정확도 곡선 : 학습 중간에 급하강
  - 최종 정확도(인식률): **custom1(42%)**, **custom2(39%)** 

-  1차 <br/>
		<img src = "https://user-images.githubusercontent.com/62331803/92257422-2bb4b600-ef10-11ea-9e6c-7701acf877fe.png" width="60%">  <br/>
-  2차 (동일한 데이터를  all_train.txt 셔플해서 시도) <br/>
		<img src = "https://user-images.githubusercontent.com/62331803/92257998-1be9a180-ef11-11ea-9926-a7a9a2914df2.png" width="60%">
</details>

#### > 은소리 데이터 학습 결과
   
   - 횡단보도 : 정확도 **70~80%** 
   - 신호등 : 정확도 **50%** 내외
#### > 결론 | 신호등 데이터 학습에 문제가 있다
- 문제점 찾기 : 정제되지 않은 데이터 사용?
[참고블로그 | CNN 을 이용하여, 얼굴을 분류해보자](#https://crystalcube.co.kr/192) <br/>
   - 내가 만드려는 모델에 맞는 데이터만 추려서 사용
   - 학습에 사용하는 이미지 데이터를 비슷하게 맞춰주기 ex. 사진 내에서 신호등의 위치
   - 학습에 적합한 수준의 선명한 사진만 사용?

<br/>

> 3차시도  | custom3 <br/>
#### > 학습 계획
- **횡단보도와 신호등을 한번에 detect**할 수 있는 모델을 생성
   - detect할 객체(class) 종류: cross walk(0), red light(1), green light(2), black(3)
   - 4개의 class를 가진 yolo 학습파일을 만들어보자
- 2차시도에서 정확도가 양호했던 **횡단보도 데이터는 정제없이 그대로 사용**
#### > 신호등 데이터셋 정제 절차
  1. 인도보행영상 데이터셋의 Bbox_1만 사용<br/>
  2. Bbox_1내의 모든 신호등 이미지를 clear(선명한 이미지), neutral(양호한 이미지), ambiguous(애매한 이미지)로 분류<br/>
  3. 신호등 이미지 수정:  사진에서 신호등이 있는 부분만 확대하고, 신호등이 사진의 정중앙에 오도록 수정<br/>
  4. 수정된 이미지를 `red(빨간불)`, `green(초록불)`, `black(비어있는 상태)` 3개의 class로 구분지어 라벨링 
<img src = "https://user-images.githubusercontent.com/62331803/92262346-ef845400-ef15-11ea-939f-f41f7b42ac2e.png" width="22%">
<img src = "https://user-images.githubusercontent.com/62331803/92262378-fad77f80-ef15-11ea-9d0d-67313556edf3.png" width="20%">
<img src = "https://user-images.githubusercontent.com/62331803/92262301-e1363800-ef15-11ea-8088-9901f50226d0.png" width="18%">

  5. 	버전을 3개로 나눠서 모델 학습
        - version1(clear이미지만 학습) | 혜정 
        - version2(clear+neutral이미지만 학습) | 은소리
        - version3(clear+neutral+ambiguous 모든 이미지 학습) | 예지
   - [참고 | 이미지 라벨링 툴](#https://www.makesense.ai/)
<img src = "https://user-images.githubusercontent.com/62331803/92261632-be575400-ef14-11ea-91ee-a74b4cfcdf77.png" width="60%"> 

#### > 학습결과 
   - version2  (clear+neutral) **정확도 91%**
   - version3 (clear+neutral+ambiguous) **정확도 87%**
 <details>
<summary>version3 학습차트 확인 </summary>
<br/>

- train 결과 <br/>
<img src = "https://user-images.githubusercontent.com/62331803/92263583-d1b7ee80-ef17-11ea-98f3-71b4a31684c1.png" width="50%"> <br/>

- 학습차트 <br/>
<img src = "https://user-images.githubusercontent.com/62331803/92263220-39216e80-ef17-11ea-93e5-6405bde7d9e2.png" width="50%"> <br/>

</details>

#### > version3 학습모델 시연 영상


#### > 결론 | 낮은 정확도는 데이터셋 퀄리티의 문제였다
- 개선할 부분
   -  신호등 정확도 여전히 낮음
   -  학습에 쓰인 신호등 이미지가 너무 큰 탓일까?

<br/>

> 4,5차시도 | custom4 ,5 <br/>
#### > 학습 계획

> 6차시도 | 

