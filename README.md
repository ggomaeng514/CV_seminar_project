# CV_seminar_project
https://github.com/inhovation97/Computer_vision_seminar

## data preprocessing

### 1. Splitting Data

* image_preview [<dataset_image_download_link>](https://drive.google.com/drive/folders/15cHemEJmMHXCe0eBtkCU27FPQaJVpnCW)

  <img src="https://user-images.githubusercontent.com/126471047/222339991-77d36642-e62e-401b-8493-e090d56efee4.jpg"  width="250" height="300"/> <img src="https://user-images.githubusercontent.com/126471047/222339929-327f4d40-c93f-463f-af4b-d83a0467bc93.jpg"  width="310" height="300"/> <img src="https://user-images.githubusercontent.com/126471047/222339815-c43812dc-5cf0-4c8d-96bd-4b9798ca0c70.jpg"  width="310" height="300"/>

* * *
* 3가지 클래스의 이미지셋

dolphin이미지가  373 개 있습니다.

shark이미지가  488 개 있습니다.

whale이미지가  451 개 있습니다.

==============================

dolphin이미지는 trian, valid, test셋에 대해  261 74 37 개씩 배정해주세요.

shark이미지는 trian, valid, test셋에 대해  341 97 48 개씩 배정해주세요.

whale이미지는 trian, valid, test셋에 대해  315 90 45 개씩 배정해주세요.


### 2. resize -> 224,224 (H,W)


### 3. Augumantion [<augmentations.transforms>](https://albumentations.ai/docs/api_reference/augmentations/transforms)

![augumentation](https://user-images.githubusercontent.com/126471047/222348568-830c5b32-e963-426d-a033-f81dcb2f1a9e.png)
* * *


## Modeling
> + Model : pretrained 된 resnet_50
> + Optimizer : Adam
> + epochs = 50
> + lr = 0.0001
> + batch_size = 8



* * *
* using tensorboard
![accuracy](https://user-images.githubusercontent.com/126471047/223669437-97b6a202-f760-4dd0-b5da-976623922b18.PNG)

![loss](https://user-images.githubusercontent.com/126471047/223669486-cabfcfce-4638-48d0-9dfa-d0ca36ae2c65.PNG)
* * *
* using Seaborn
![seaborn](https://user-images.githubusercontent.com/126471047/223682107-e352a76c-f68b-4e1f-9e26-cc02d97dba24.png)


epoch 26에서 Accuracy가 가장 컸고 epoch 44에서 Loss가 가장 낮은 결과를 보였다. 

epochs를 더 늘려 모델을 더 학습시켜야할 필요성이 보여 100 epoch로 수정하여 학습시킨결과 46 epochs에서 Accuracy 94.977.

* * *

##  Test set에 모델 적용

best epoch 46에서의 가중치를 pickle파일로 저장한 뒤 test셋에 적용하여 성능을 테스트 한 결과 Loss : 0.302, Accuracy : 87.116% 달성


