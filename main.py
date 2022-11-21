from gui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sql_main import *
import sqlite3 as sql
class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.kmt_btn.setText("Onayla")
        self.ui.kmt_btn.clicked.connect(self.sorgu)
        self.ad = self.ui.line_ad.text()
        self.soyad = self.ui.line_soyad.text()
        self.tc_no =self.ui.line_tc.text()
        self.telno=self.ui.line_telno.text()
        self.sag_goz=self.ui.line_r.text()
        self.sag_ax=self.ui.line_rax.text()
        self.sol_goz=self.ui.line_l.text()
        self.sol_ax=self.ui.line_lax.text()
        self.cambilgi=self.ui.cmb_marka.currentText()
        self.tarih=self.ui.line_tarih.text()
        
    def sorgu(self):
        if self.ui.radio_ekle.isChecked()==True:
            self.ekle()
        elif self.ui.radio_sil.isChecked()==True:
            self.sil()
        elif self.ui.radio_update.isChecked()==True:
            self.update()
        elif self.ui.radio_list.isChecked()==True:
            self.duruma_gore()
    def ekle(self):
        ad =self.ui.line_ad.text() 
        soyad = self.ui.line_soyad.text()
        tc_no=self.ui.line_tc.text()
        telno =self.ui.line_telno.text()
        sag_goz=self.ui.line_r.text()
        sag_ax=self.ui.line_rax.text()
        sol_goz=self.ui.line_l.text()
        sol_ax=self.ui.line_lax.text()
        cambilgi=self.ui.cmb_marka.currentText()
        tarih=self.ui.line_tarih.text()
        data = veriler()
        data.ekle(ad,soyad,tc_no,telno,sag_goz,sag_ax,sol_goz,sol_ax,cambilgi,tarih)
        self.temizle()
        self.listele()
        
    def sil(self):
        ad = self.ui.line_ad.text()
        soyad = self.ui.line_soyad.text()
        tc_no=self.ui.line_tc.text()
        data=veriler()
        data.sil(ad,soyad,tc_no)
        self.temizle()
        self.listele()
    def update(self):
        ad =self.ui.line_ad.text() 
        soyad = self.ui.line_soyad.text()
        tc_no=self.ui.line_tc.text()
        telno =self.ui.line_telno.text()
        sag_goz=self.ui.line_r.text()
        sag_ax=self.ui.line_rax.text()
        sol_goz=self.ui.line_l.text()
        sol_ax=self.ui.line_lax.text()
        cambilgi=self.ui.cmb_marka.currentText()
        tarih=self.ui.line_tarih.text()
        data = veriler()
        data.guncelle(ad,soyad,tc_no,telno,sag_goz,sag_ax,sol_goz,sol_ax,cambilgi,tarih)
        self.temizle()
        self.listele()
    def temizle(self):
        self.ui.line_ad.clear()
        self.ui.line_soyad.clear()
        self.ui.line_tc.clear()
        self.ui.line_telno.clear()
        self.ui.line_r.clear()
        self.ui.line_rax.clear()
        self.ui.line_l.clear()
        self.ui.line_lax.clear()
        self.ui.line_tarih.clear()  
    def listele(self):
        self.ui.table_data.clear()
        self.conn=sql.connect("veritabani.db")
        self.imlec=self.conn.cursor()
        self.imlec.execute("select * from 'datalar' ")
        for indexSatir,kayitNumarasi in enumerate(self.imlec):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
                self.ui.table_data.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
        self.conn.close()
    def duruma_gore(self):
        self.ui.table_data.clear()
        self.conn=sql.connect("veritabani.db")
        self.imlec=self.conn.cursor()
        kategori=self.ui.cmb_list.currentText()
        sorgu = "select * from 'datalar' where cam_bilgi ='{}' ".format(kategori)
        self.imlec.execute(sorgu)
        for indexSatir,kayitNumarasi in enumerate(self.imlec):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
                self.ui.table_data.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
        self.conn.close()
program = QApplication([])
arayuz = form()
arayuz.show()
program.exec()