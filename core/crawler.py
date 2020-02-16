import requests
import requests_cache
import json

class Crawler:

    baseURL = "https://al-quran-8d642.firebaseio.com"
    endPointSurat = "{0}/data.json?print=pretty".format(baseURL)
    endPointAyat = "{0}/surat/$nomor.json?print=pretty".format(baseURL)

    def __init__(self):
        requests_cache.install_cache("quran_cache")

    def getDataSurat(self):
        response = requests.get(self.endPointSurat)
        data = json.loads(response.text)
        return data

    def getDataAyat(self, nomor):
        response = requests.get(self.endPointAyat.replace("$nomor", str(nomor)))
        data = json.loads(response.text)
        return data