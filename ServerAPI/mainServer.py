from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import model

app = Flask(__name__)
api = Api(app)

class demiraiAPI(Resource):

    def __init__(self):

        self.skModel = model.Model()

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('marka', required=True)
        parser.add_argument('os', required=True)
        parser.add_argument('hafiza', required=True)
        parser.add_argument('ram', required=True)
        parser.add_argument('goruntu', required=True)
        parser.add_argument('cozunurluk', required=True)
        parser.add_argument('kamera', required=True)
        parser.add_argument('batarya', required=True)
        parser.add_argument('mobilhiz', required=True)
        parser.add_argument('ekranboyutu', required=True)
        parser.add_argument('parmakizi', required=True)
        parser.add_argument('yuztanima', required=True)
        parser.add_argument('dayaniklilik', required=True)
        parser.add_argument('hat', required=True)
        parser.add_argument('sdcard', required=True)
        parser.add_argument('ekranyenileme', required=True)
        args = parser.parse_args()


        data = {"Marka": [args['marka']], 
                "İşletim Sistemi": [args['os']],
                "Dahili Hafıza" : [args['hafiza']],
                "RAM Kapasitesi" : [args['ram']],
                "Görüntü Teknolojisi" : [args['goruntu']],
                "Ekran Çözünürlüğü" : [args['cozunurluk']],
                "Kamera Çözünürlüğü" : [args['kamera']],
                "Batarya Kapasitesi Aralığı" : [args['batarya']],
                "Mobil Bağlantı Hızı" : [args['mobilhiz']],
                "Ekran Boyutu" : [args['ekranboyutu']],
                "Parmak İzi Okuyucu" : [args['parmakizi']],
                "Yüz Tanıma" : [args['yuztanima']],
                "Suya/Toza Dayanıklılık" : [args['dayaniklilik']],
                "Çift Hat" : [args['hat']],
                "Arttırılabilir Hafıza (Hafıza Kartı Desteği)" : [args['sdcard']],
                "Ekran Yenileme Hızı" : [args['ekranyenileme']]}

        PData = pd.DataFrame.from_dict(data)
        
        pred = self.skModel.predict(PData)[0]

        return pred, 201

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('marka', required=True)
        parser.add_argument('os', required=True)
        parser.add_argument('hafiza', required=True)
        parser.add_argument('ram', required=True)
        parser.add_argument('goruntu', required=True)
        parser.add_argument('cozunurluk', required=True)
        parser.add_argument('kamera', required=True)
        parser.add_argument('batarya', required=True)
        parser.add_argument('mobilhiz', required=True)
        parser.add_argument('ekranboyutu', required=True)
        parser.add_argument('parmakizi', required=True)
        parser.add_argument('yuztanima', required=True)
        parser.add_argument('dayaniklilik', required=True)
        parser.add_argument('hat', required=True)
        parser.add_argument('sdcard', required=True)
        parser.add_argument('ekranyenileme', required=True)
        args = parser.parse_args()


        data = {"Marka": [args['marka']], 
                "İşletim Sistemi": [args['os']],
                "Dahili Hafıza" : [args['hafiza']],
                "RAM Kapasitesi" : [args['ram']],
                "Görüntü Teknolojisi" : [args['goruntu']],
                "Ekran Çözünürlüğü" : [args['cozunurluk']],
                "Kamera Çözünürlüğü" : [args['kamera']],
                "Batarya Kapasitesi Aralığı" : [args['batarya']],
                "Mobil Bağlantı Hızı" : [args['mobilhiz']],
                "Ekran Boyutu" : [args['ekranboyutu']],
                "Parmak İzi Okuyucu" : [args['parmakizi']],
                "Yüz Tanıma" : [args['yuztanima']],
                "Suya/Toza Dayanıklılık" : [args['dayaniklilik']],
                "Çift Hat" : [args['hat']],
                "Arttırılabilir Hafıza (Hafıza Kartı Desteği)" : [args['sdcard']],
                "Ekran Yenileme Hızı" : [args['ekranyenileme']]}

        pred = self.skModel.predict(PData)[0]

        return pred, 201

api.add_resource(demiraiAPI, '/demiraiapi')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)