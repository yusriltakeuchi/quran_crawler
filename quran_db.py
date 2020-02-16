import requests
from core.db_handler import DBHandler
from core.crawler import Crawler

def headers():
    print("    /-------------------------/")
    print("   /      QURAN CRAWLER      /")
    print("  /      -------------      /")
    print(" /   by Yusril Rapsanjani  /")
    print("/-------------------------/")
    print("")

def main():
    headers()
    db = DBHandler()
    db.createTable();
    
    # Fetching data from api
    crawler = Crawler()
    print(" Crawling surat data")
    data = crawler.getDataSurat()

    print(" Starting insert surat")
    print("--------------------------")
    db.insertSurat(data)

if __name__ == "__main__":
    main()