import requests
import urllib
import imghdr
import os
import ssl
import csv

filePathDict = 'dogsImageNet.csv'
_url = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid="

def loadDogDict():
    with open(filePathDict, mode='r') as infile:
        reader = csv.reader(infile, delimiter=';')
        dogBreedDict = {str(rows[0]).zfill(3) + '.' + str(rows[1]).replace(' ', '_'): rows[2] for rows in reader}
    return dogBreedDict

dogBreedDict = loadDogDict()
for folder_name, wnid in dogBreedDict.items():
    response = requests.get(_url + wnid)
    resp = response.content.decode("utf-8")
    count = 0
    errors = 0
    for url in resp.split('\r\n'):
        count+=1
        if (count % 10 == 0):
            print(str(count) + " links were processed")
        file_name = "images/" + folder_name+ "/" + str(count - errors) + ".jpg"
        try:
            urllib.request.urlretrieve(url, file_name)
            if (imghdr.what(file_name) != "jpeg"):
                os.remove(file_name)
        except (urllib.error.URLError, urllib.error.HTTPError, ConnectionResetError, ssl.CertificateError) as error:
            errors+=1
            print(error)

print(count)