import cv2
from cv2 import VideoCapture
import dropbox
import time
import random 
start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print("snapshot taken")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.BG5qWRipJk9RW6Oo-SkfBWM09XsYl4Hr_ZvbAqnDDm9eXIRdY1wnTN27d-TVv7U9EZQGdOp976219VrhWGlKtSix_VNaIUNQkeLoq2Cg5A2cUIhdS-skpU4HypqEJn7GnreQ36U"
    file=img_name
    file_from=file
    file_to="/testFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file Uploded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()
    