import shutil
import os
import sys
try:
	files =  os.listdir("c:/Users/Sachin/.jenkins/workspace/my_jenkins_pytest/allure-report/history")
	#print(files)
	for f in files:
		#print(f)
		shutil.copy("c:/Users/Sachin/.jenkins/workspace/my_jenkins_pytest/allure-report/history/"+f,"c:/Users/Sachin/.jenkins/workspace/my_jenkins_pytest/allure-results/history",follow_symlinks=True)
except Exception as e:
	print("Error message : " + format(e))	