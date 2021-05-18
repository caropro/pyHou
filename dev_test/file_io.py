#coding = utf-8



content = "This is test file.\nTo record test infomation.\nJust a Blank Data file."
# with open("test_txt","w+") as tx:
#     tx.write(content)


with open("test_txt","r+") as tx:
    # print tx.readlines()
    for line in tx.readlines():
        print line.rstrip()
