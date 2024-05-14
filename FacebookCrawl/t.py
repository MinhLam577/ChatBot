import os
#Đọc dữ liệu từ file txt
def readDataFileITxtID(fileName):
    try:
        path = fileName
        if (os.path.isfile(path) == False):
            with open(path, 'a', encoding='utf-8') as f:
                pass
            return []
        else:
            with open(path, 'r', encoding='utf-8') as f:
                data = [line.strip().split(";") for line in f]
                data = [item for sublist in data for item in sublist]
            return data[0:-1]
    except Exception as e:
        print(e)
        
print(readDataFileITxtID(r"D:\Code_school_nam3ki2\TriTueNhanTao\Chat_bot\FacebookCrawl\post_ID_Fanpage.txt"))