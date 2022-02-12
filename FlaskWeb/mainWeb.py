from crypt import methods
from flask import Flask,render_template,request
from wtforms import Form,validators,SelectField,RadioField
import requests
import time

class TeknikOzellikForm(Form):
    marka = SelectField('Marka',choices=[
            (0, 'Samsung'),
             (1, 'Apple'),
             (2, 'Xiaomi'),
             (3, 'General Mobile'),
             (4, 'Reeder'),
             (5, 'Oppo'),
             (6, 'Huawei'),
             (7, 'realme'),
             (8, 'Tecno'),
             (9, 'Infinix'),
             (10, 'POCO'),
             (11, 'Casper'),
             (12, 'Hiking'),
             (13, 'TCL'),
             (14, 'LG'),
             (15, 'Vivo'),
             (16, 'Alcatel'),
             (17, 'Elephone'),
             (18, 'VESTEL'),
             (19, 'Omix'),
             (20, 'Ulefone'),
             (21, 'Honor'),
             (22, 'Oneplus')
             ])
    
    dahili_hafiza = SelectField('Dahili Hafıza',choices=[
        (6,"1 TB"),
        (5,"512 GB"),
        (3,"256 GB"),
        (0,"128 GB"),
        (1,"64 GB"),
        (2,"32 GB"),
        (4,"16 GB"),
        (7,"8 GB")
    ])
    ram_kapasitesi = SelectField('RAM Kapasitesi',choices=[
        (7,"32 GB"),
        (6,"12 GB"),
        (2,"8 GB"),
        (1,"6 GB"),
        (0,"4 GB"),
        (3,"3 GB"),
        (4,"2 GB"),
        (5,"1 GB")
    ])
    goruntu_teknolojisi = SelectField('Görüntü Teknolojisi',choices=[
        (3,"LED"),
        (2,"OLED"),
        (1,"AMOLED"),
        (0,"LCD")
    ])
    ekran_cozunurluk = SelectField('Ekran Çözünürlüğü',choices=[
        (5,"UHD+"),
        (2,"QHD+"),
        (4,"QHD"),
        (0,"FHD+"),
        (1,"HD+"),
        (3,"HD")
    ])
    kamera_cozunurluk = SelectField('Kamera Çözünürlüğü',choices=[
        (0,"20 MP ve üstü"),
        (1,"10 - 15 MP"),
        (2,"15 - 20 MP"),
        (3,"5 - 10 MP"),
        (4,"5 MP ve altı")
    ])
    batarya_kapasite_araligi = SelectField('Batarya Kapasitesi Aralığı',choices=[
        (8,"6000-7000 mAh"),
        (1,"5000-6000 mAh"),
        (0,"4500-5000 mAh"),
        (2,"4000-4500 mAh"),
        (3,"3500-4000 mAh"),
        (4,"3000-3500 mAh"),
        (5,"2000-3000 mAh"),
        (6,"1000-2000 mAh"),
        (7,"800-1000 mAh")
    ])
    mobil_baglanti_hizi = SelectField('Mobil Bağlantı Hızı',choices=[
        (1,"5G"),
        (0,"4.5G"),
        (2,"4G"),
        (3,"3G"),
        (4,"2G")
    ])
    ekran_yenileme_hizi = SelectField('Ekran Yenileme Hızı',choices=[
        (5,"144 Hz üstü"),
        (4,"144 Hz"),
        (1,"120 Hz"),
        (2,"90 Hz"),
        (0,"60 Hz"),
        (3,"60 Hz altı")
    ])
    ekran_boyut = SelectField('Ekran Boyutu',choices=[
        (3,"10,5 inch"),
        (5,"6 - 8 inch"),
        (4,'6,8 inch'),
        (0,"6 inch ve üstü"),
        (2,"5,5 - 6 inç"),
        (1,"5 - 5,5 inch"),
        (6,"4 - 4,5 inch"),
        (7,"4,5 - 5 inch")
        ])
    parmak_izi_okuyucusu = RadioField("Parmak İzi Okuyucu",choices=[
        (0,"Var"),
        (1,"Yok")
    ],default = 0)
    yuz_tanima = RadioField("Yüz Tanıma",choices=[
        (0,"Var"),
        (1,"Yok")
    ],default = 0)
    suya_toza_dayaniklilik = RadioField("Suya/Toza Dayanıklılık",choices=[
        (1,"Var"),
        (0,"Yok")
    ],default = 1,)
    cift_hat = RadioField("Çift Hat",choices=[
        (0,"Var"),
        (1,"Yok")
    ],default = 0)
    arttirilabilir_hafiza = RadioField("Arttırılabilir Hafıza (Hafıza Kartı Desteği)",choices=[
        (0,"Var"),
        (1,"Yok")
    ],default = 0)
    isletim_sistemi = RadioField('İşletim Sistemi', choices = [
        (0,'Android'),
        (1,'İOS')
    ],default = 0)
    

app = Flask(__name__) 
@app.route("/",methods = ["GET","POST"])
def index():

    form = TeknikOzellikForm(request.form)
    pred=-99

    if request.method == "POST":


        url = "http://172.31.77.170:80/demiraiapi?marka="+str(form.marka.data)+"&os="+str(form.isletim_sistemi.data)
        url+="&hafiza="+str(form.dahili_hafiza.data)+"&ram="+str(form.ram_kapasitesi.data)
        url+="&goruntu="+str(form.goruntu_teknolojisi.data)+"&cozunurluk="+str(form.ekran_cozunurluk.data)
        url+="&kamera="+str(form.kamera_cozunurluk.data)+"&batarya="+str(form.batarya_kapasite_araligi.data)
        url+="&mobilhiz="+str(form.mobil_baglanti_hizi.data)+"&ekranboyutu="+str(form.ekran_boyut.data)
        url+="&parmakizi="+str(form.parmak_izi_okuyucusu.data)+"&yuztanima="+str(form.yuz_tanima.data)
        url+="&dayaniklilik="+str(form.suya_toza_dayaniklilik.data)+"&hat="+str(form.cift_hat.data)
        url+="&sdcard="+str(form.arttirilabilir_hafiza.data)+"&ekranyenileme="+str(form.ekran_yenileme_hizi.data)
        print(form.goruntu_teknolojisi.data)
        response = requests.get(url)
        pred = str(int(response.json())) + " TL"


    return render_template("form_template.html",form = form,pred_top = pred)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result")
def result():
    return render_template("result.html",pred_top = 0)


if __name__ == "__main__": 
	app.run(host='0.0.0.0', port=80)