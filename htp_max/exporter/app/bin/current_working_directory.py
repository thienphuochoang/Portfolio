# -*- coding: utf-8 -*-
# @Author: tungle
# @Date:   2019-08-08 18:18:31
# @Last Modified by:   tungle
# @Last Modified time: 2019-08-08 21:20:01
import os


def get_cwd(count=5):
	crurrent_path = os.path.dirname(os.path.abspath(__file__))
	path_project = ""
	name_protject = ""
	while count != 0:
		# print count
		path_project = crurrent_path
		crurrent_path = os.path.dirname(crurrent_path)
		count = count-1
	# print path_project
	path = os.path.dirname(path_project)
	name = os.path.basename(path_project)
	return path, name 
    # mark_point = ""
    # while mark_point != "Projects":
    #     project_path = crurrent_path
    #     crurrent_path = os.path.dirname(crurrent_path)
    #     mark_point = crurrent_path.split('\\')[-1]
    # return project_path

def ahihi():
	currentPath = os.path.dirname(os.path.realpath(__file__))
	return currentPath