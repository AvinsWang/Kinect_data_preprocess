# coding:utf-8
import os
import sys

def rename(sdir, tmp):
    if tmp:
        prefix = "xxx"
    else:
        prefix = ""
    for dirs in os.listdir(sdir):
        if dirs == "depth" or dirs == "map":
            count = 1
            for fname in os.listdir(os.path.join(sdir, dirs)):
                sname = os.path.splitext(fname)
                pre_dir = os.path.join(sdir, dirs, fname)
                aft_dir = os.path.join(sdir, dirs, prefix + str(count) +sname[1])
                os.rename(pre_dir, aft_dir)
                count += 1
                if tmp:
                    print(".")
                    print("...")
                else:
                    print(pre_dir, " -> ", aft_dir)

if __name__ == "__main__":
    sdir = "../../"
    rename(sdir,True)
    # rename(sdir,False)
