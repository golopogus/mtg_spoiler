def save_pic_as_txt(pics):
    if len(pics) > 0:
        file = open("pics.txt","a")
        file.write('\n' + str(pics))
        file.close()
    
