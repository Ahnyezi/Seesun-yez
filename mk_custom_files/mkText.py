import os

if __name__ == '__main__':

    folder = 'cw/'
    yolo_path = 'data/obj/cw/' # + img Name

    with open('all_train.txt', 'a') as f:
        for file in os.listdir(folder):
            if 'jpg' in file.lower() or 'png' in file.lower():
                f.write(yolo_path+file+"\n")
    f.close() 