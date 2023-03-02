import os
import glob
import cv2
import time

class Make_dataset_dir():
  def __init__(self, root_dir):
    '''클래스 내의 인자 생성 함수입니다. 아래의 인자들을 이용하여, 금주의 과제를 해결해주세요.'''
    self.root_path = root_dir+'/' if root_dir[-1] != '/' else root_dir # 현재 진행할 프로젝트 -> root path는 /content/drive/MyDrive/CV_seminar_project/ 가 되어야합니다.
    self.img_path_list = root_dir+'original' # 전달한 이미지들의 상위 경로
    self.trainset_path = root_dir+'train/'
    self.validset_path = root_dir+'valid/'
    self.testset_path = root_dir+'test/'
    self.class_list = ['dolphin', 'shark', 'whale']

  def mk_dir(self):
    '''train, valid, test 폴더를 만들고, 내부에는 클래스 별 폴더를 추가로 만들어 주세요.'''
    dataset_dir_list= [self.trainset_path, self.validset_path, self.testset_path]
    for dataset_dir in dataset_dir_list:
        for cls in self.class_list:
          os.makedirs(dataset_dir+cls, exist_ok=True)
    print('디렉토리 생성 완료')

  def move_img(self):
    '''mk_dir에서 만든 폴더들에 각 클래스에 맞는 이미지를 배당해주세요. train, valid, test에 각각 7: 2: 1'''
    dolphin_img_list = glob.glob('/content/drive/MyDrive/CV_seminar_project/original/dolphin/*')
    shark_img_list = glob.glob('/content/drive/MyDrive/CV_seminar_project/original/shark/*')
    whale_img_list = glob.glob('/content/drive/MyDrive/CV_seminar_project/original/whale/*')

    dic = {'dolphin': dolphin_img_list , 'shark': shark_img_list, 'whale': whale_img_list}
    for key in dic.keys():
      length_list.append([int(len(dic[key])*0.7),int(len(dic[key])*0.2), int(len(dic[key])*0.1)])
   
    for i, key in enumerate(dic.keys()):
      spliting_length= length_list[i]

      for ii ,img_path in enumerate(dic[key]):
        if ii+1 <=spliting_length[0]:
          img=cv2.imread(img_path)
          img_name= img_path.split('/')[-1]
          cv2.imwrite(self.trainset_path+'/'+ key + '/' +img_name,img)      


        elif ii+1 > spliting_length[0] and ii+1 <= spliting_length[0]+ spliting_length[1]:
          img=cv2.imread(img_path)
          img_name= img_path.split('/')[-1]
          cv2.imwrite(self.validset_path+'/'+ key + '/' +img_name,img)
      
        else:
          img=cv2.imread(img_path)
          img_name= img_path.split('/')[-1]
          cv2.imwrite(self.testset_path+'/'+ key + '/' +img_name,img)
    print('데이터 스플릿 완료')

  def run(self):
    '''run 함수를 돌리면, 모든 작업이 완료될 수 있게끔 mk_dir 함수와 move_img 함수를 생성해주시면 됩니다.'''
    start = time.time()
    self.mk_dir()
    self.move_img()
    print('총 소요시간: ', time.time()-start)

  def checking_dirs(self):
    '''데이터가 잘 스플릿 되었는지 확인하는 함수입니다. trian, valid, test 디렉토리에 데이터가 잘 들어가 있는지 개수를 확인하는 함수를 생성해주시면 됩니다.'''
