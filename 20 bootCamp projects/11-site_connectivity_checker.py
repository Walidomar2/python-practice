#########################################################################
# auther: Walid Omar
# brief: taking the url from user and check the connectivity to the url 
#       and give back the response code after opening that url
#########################################################################

import urllib.request as urllib

def checkConnectivity(url):
    print("checking connectivity... ")
    
    response = urllib.urlopen(url)
    
    print(f"Connected to {url} successfully ")
    print(f"the response code is: {response.getcode()}")


userUrl = input("Enter the url you want to check : ").strip()

checkConnectivity(userUrl)




