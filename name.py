import os

# 디렉토리 경로 설정

path = "sign_first/images"
# 디렉토리 내의 모든 파일 이름을 리스트로 저장
dir1_list = os.listdir(path)

f= open("test.txt","w+")
for i in dir1_list:
     f.write("sign_first/images/%s\n" % (i))
# 리스트 내의 요소 출력
# for f in dir1_list:
#   print(f)



