# this is a simple script that prints out the version of requests lib
# Gengyuan Huang
# CMPUT404 Lab1 winter2021

import requests as rqs 

def main():
    rqs_version = rqs.__version__
    rqs_google_response = rqs.get("https://www.google.com")
    rqs_google_statuscode = rqs_google_response.status_code
    rqs_google_text = rqs_google_response.text

    print("The requests library version is: \n" + rqs_version)
    print("The google home page status code is: \n" + str(rqs_google_statuscode))
    print("The google home page content is: \n" + rqs_google_text)


main()