import os

def Rename():
    address = "d:\text" #เลือกไดร์
    dir_list = os.listdir(address)
    os.chdir(address)
    i = 1

    for filename in dir_list:
        newname = "Text "  # ชื่อที่จะนำมาใส่แทนชื่อเดิม
        name = "{}_{:03d}.png".format(newname, i) #{:01d}ใช้กำหนดความยาวตัวเลข
        os.rename(filename , name)
        
        i +=1
    print(f"\n\n\nChange_Name_Success\n   \m/*.*\m/\n\n\n")
if __name__ == "__main__" :
     Rename()