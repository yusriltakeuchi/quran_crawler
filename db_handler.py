import sqlite3
from crawler import Crawler

class DBHandler:

    def __init__(self):
        self.conn = sqlite3.connect("quran.db")
        self.crawler = Crawler()

    def createTable(self):
        print(" Creating table surat")
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS surat
        (   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nama TEXT NOT NULL,
            nomor INTEGER NOT NULL,
            arti TEXT NOT NULL,
            asma TEXT NOT NULL,
            keterangan TEXT NOT NULL,
            ayat INTEGER NOT NULL,
            audio TEXT NOT NULL,
            rukuk INTEGER NOT NULL,
            type TEXT NOT NULL,
            urut INTEGER NOT NULL
        )
        ''')

        print(" Creating table ayat")
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS ayat
        (   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nomor INTEGER NOT NULL,
            arab TEXT NOT NULL,
            indonesia TEXT NOT NULL,
            ejaan TEXT NOT NULL,
            surat_id INTEGER NOT NULL
        )
        ''')

    def insertSurat(self, data):
        count = 0

        cur = self.conn.cursor()
        for _data in data:
            count += 1
            print(" [{0}/{1}] Insert Surat {2}".format(str(count), str(len(data)), _data['nama']))
            cur.execute('''
                INSERT INTO surat
                (nama, nomor, arti, asma, keterangan, ayat, audio, rukuk, type, urut)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (_data['nama'], _data['nomor'], _data['arti'], _data['asma'], _data['keterangan'], _data['ayat'], _data['audio'], _data['rukuk'], _data['type'], _data['urut']))
            self.conn.commit()

            # insert ayat
            ayatData = self.crawler.getDataAyat(cur.lastrowid)
            self.insertAyat(ayatData, cur.lastrowid)

        print(" Surat successfully inserted")

    def insertAyat(self, data, surat_id):

        cur = self.conn.cursor()
        print("    [*] Getting ayat data")
        for _data in data:
            cur.execute('''
                INSERT INTO ayat
                (nomor, arab, indonesia, ejaan, surat_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (_data['nomor'], _data['ar'], _data['id'], _data['tr'], surat_id))
            self.conn.commit()
      
        print("    [*] Successfully got ayat")