import sqlite3 as sql

class veriler:
    def __init__(self):
        self.sql_name = sql.connect("veritabani.db")
        self.cursor = self.sql_name.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 'datalar' (ID integer primary key autoincrement,ad text,soyad text,tc_no integer,tel_no integer,sag_goz float,sag_ax float,
        sol_goz float,sol_ax float,cam_bilgi text,tarih text)                    
                            """)
        self.sql_name.commit()
        
    def ekle(self,ad,soyad,tc_no,tel_no,sag_goz,sag_ax,sol_goz,sol_ax,cam_bilgi,tarih):
        
        self.cursor.execute("""
        INSERT INTO 'datalar' (ad,soyad,tc_no,tel_no,sag_goz,sag_ax,sol_goz,sol_ax,cam_bilgi,tarih) VALUES (?,?,?,?,?,?,?,?,?,?)                    
                            """,(ad,soyad,tc_no,tel_no,sag_goz,sag_ax,sol_goz,sol_ax,cam_bilgi,tarih))
        self.sql_name.commit()
        self.sql_name.close()
    def listele(self):
        self.imlec = self.sql_name.cursor()
        self.imlec.execute("""
        SELECT * FROM 'datalar'               
                      """)
        self.imlec.fetchall()
        print(self.imlec)
    def sil(self,ad,soyad,tc):
        self.cursor.execute("""
        DELETE FROM 'datalar' WHERE ad = '{}' AND soyad ='{}' AND tc_no= '{}'                  
                            """.format(ad,soyad,tc))
        self.sql_name.commit()
        self.sql_name.close()
    def guncelle(self,ad,soyad,tc_no,tel_no,sag_goz,sag_ax,sol_goz,sol_ax,cam_bilgi,tarih):
        self.cursor.execute("UPDATE datalar SET tel_no='{}',sag_goz='{}',sag_ax='{}',sol_goz='{}',sol_ax='{}',cam_bilgi='{}',tarih='{}' WHERE ad='{}' AND soyad='{}' AND tc_no='{}' ".format(tel_no,sag_goz,sag_ax,sol_goz,sol_ax,cam_bilgi,tarih,ad,soyad,tc_no))
        self.sql_name.commit()
        self.sql_name.close()
