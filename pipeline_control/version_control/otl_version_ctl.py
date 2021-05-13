#coding = utf-8
import os
import sys
import shutil
import time
import json

otl_root = r"C:\Users\Administrator\Documents\houdini17.0\otls"
version_root = r"C:\Users\Administrator\Documents\houdini17.0\otls\temp_version"
file_dic = {}

def version_dic(version_root):
    """
    :param version_root:
    :return:
    """
    file_dic = {}
    current_version_filelist = os.listdir(version_root)
    for version_file in sorted(current_version_filelist):
        version_file_fullpath = os.path.join(version_root,version_file)
        version_shortfilename = os.path.splitext(version_file)[0].split("_v")[0]
        file_mtime = os.path.getmtime(version_file_fullpath)
        try:
            file_version = os.path.splitext(version_file)[0].split("_v")[1]
        except:
            file_version = 1
        print(version_shortfilename)
        print(file_version)
        print(file_mtime)
        print(file_dic.get(version_shortfilename),int(file_version))
        if not file_dic.get(version_shortfilename) or file_dic.get(version_shortfilename).get("version")<int(file_version):
            file_dic[version_shortfilename]={}
            file_dic[version_shortfilename]["version"] = int(file_version)
            file_dic[version_shortfilename]["mtime"] = file_mtime
    print file_dic
    return file_dic

def check_NoVersionFiles(noversion_path,version_dic,tar_dir):
    update_record = {}
    #no_version_files
    for no_version_file in os.listdir(noversion_path):
        nv_file_full_path = os.path.join(noversion_path,no_version_file)
        if os.path.isdir(nv_file_full_path):
            continue
        print(nv_file_full_path)
        file_mtime = os.path.getmtime(nv_file_full_path)
        print(time.ctime(file_mtime))
        no_version_filename =os.path.splitext(no_version_file)[0]
        #check the dic
        if not version_dic.get(no_version_filename):
            copy_verison(nv_file_full_path,tar_dir,1)
            update_record[no_version_filename]={"version":1,"mtime":file_mtime}
        else:
            #get modify time and compare with the version file
            record_mtime = version_dic.get(no_version_filename).get("mtime")
            if file_mtime>record_mtime:
                verison = version_dic.get(no_version_filename).get("version")+1
                copy_verison(nv_file_full_path, tar_dir, verison)
                update_record[no_version_filename] = {"version": verison, "mtime": file_mtime}
    return update_record

def copy_verison(org_filepath,tar_dir,version):
    org_file = os.path.basename(org_filepath)
    org_filename = os.path.splitext(org_file)[0]
    org_fileext = os.path.splitext(org_file)[1]
    target_file_path = os.path.join(tar_dir,"%s_v%02d%s"%(org_filename,version,org_fileext))
    print(org_filepath)
    print(target_file_path)
    shutil.copy(org_filepath,target_file_path)



file_dic = version_dic(version_root)
new_file_dic = check_NoVersionFiles(otl_root,file_dic,version_root)


if not os.path.exists(os.path.join(r"D:/",time.strftime("%Y%m%d"))):
    os.mkdir(os.path.join(r"D:/",time.strftime("%Y%m%d")))

beforeupdate_path = os.path.join(r"D:/",time.strftime("%Y%m%d"),"%s_%s.json"%("org_otl",time.strftime("%Y%m%d_%H%M")))
with open(beforeupdate_path,"w+") as outfile:
    json.dump(file_dic,outfile)
update_path = os.path.join(r"D:/",time.strftime("%Y%m%d"),"%s_%s.json"%("new_otl",time.strftime("%Y%m%d_%H%M")))
with open(update_path,"w+") as outfile:
    json.dump(new_file_dic,outfile)











