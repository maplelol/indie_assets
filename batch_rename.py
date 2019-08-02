#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import getopt



def main(argv):
	path_name = './'
	new_name = 'file'

	try:
		opts,args = getopt.getopt(argv, "hp:n:", ["help=","path=","name"])# 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
	except getopt.GetoptError:
		print 'Error: batch_rename.py expect a relative path -p <relative_path>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-h":
			print 'batch_rename.py -p <relative_path>'
			sys.exit()
		elif opt in ("-p", "--path"):
			path_name = path_name + arg
		elif opt in ("-n", "--name"):
			new_name = arg

	print("relative_path="+path_name);

	path_name = os.path.abspath(path_name);

	print("abs_path="+path_name);

	i=1
	for item in os.listdir(path_name):
		# print("item="+item)
		item_abs_path = os.path.join(path_name,item)
		# print("item_abs_path="+item_abs_path)
		item_type = os.path.splitext(item)[-1]
		# print("item_type="+item_type)
		item_abs_path_new = os.path.join(path_name,(new_name+str(i)+item_type))
		# print("item_abs_path_new="+item_abs_path_new)
		os.rename(item_abs_path,item_abs_path_new)
		i += 1


if __name__ == "__main__":
	main(sys.argv[1:])
