# this is a simple script that prints out the version of requests lib
# Gengyuan Huang
# CMPUT404 Lab1 winter2021

import requests as rqs 

def main():
    rqs_version = rqs.__version__
    rqs_scriptfile_response = rqs.get("https://github.com/gengyuanhuang/cmput404_lab1/raw/main/cmput404_lab1_pyscript.py")
    rqs_scriptfile_statuscode = rqs_scriptfile_response.status_code
    rqs_scriptfile_text = rqs_scriptfile_response.text

    print("The requests library version is: \n" + rqs_version + "\n")
    print("The script file raw link status code is: \n" + str(rqs_scriptfile_statuscode) + "\n")
    print("The script file content is: \n" + rqs_scriptfile_text + "\n")


main()