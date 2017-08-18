from icrawler.builtin import GoogleImageCrawler
import os
import csv

filePathDict = 'dogBreedsListGoogle.csv'

def loadDogDict():
    with open(filePathDict,'rU') as infile:
        reader = csv.reader(infile, dialect=csv.excel_tab, delimiter=';')
        dogBreedDict = {str(rows[0]).zfill(3) + '.' + str(rows[1]).replace(' ', '_'): str(rows[1]) for rows in reader}
    return dogBreedDict

def crawl(breedDir, breedName):
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': '~/dog-images/googleDogImages/' + breedDir})
    google_crawler.crawl(keyword=breedName, max_num=1000,
                         date_min=None, date_max=None,
                         min_size=(300, 300), max_size=None)

if __name__ == "__main__":
    dogBreedDict = loadDogDict()
    for breedDir, breedName in dogBreedDict.items():
        crawl(breedDir, breedName)