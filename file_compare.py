# coding:utf-8

import os

def get_dirs(dir):
	dirs = os.listdir(dir)
	dir_num = []
	for dir in dirs:
		dir_num.append(dir.split(".")[0])
	return dir_num

def compare(map_list, depth_list):
	del_dirs = []
	for depth_dir in depth_list:
		if not depth_dir in map_list:
			del_dirs.append(depth_dir)
	return del_dirs

def del_file(dir, del_dirs):
	for i in del_dirs:
		d_dir = os.path.join(dir, i+".png")
		if os.path.isfile(d_dir):
			os.remove(d_dir)
			print("del:", d_dir)


if __name__ == "__main__":
	map_dir = "../../map/"
	depth_dir = "../../depth/"
	map_list = get_dirs(map_dir)
	depth_list = get_dirs(depth_dir)
	del_dirs = compare(map_list, depth_list)
	del_file(depth_dir, del_dirs)
