from bs4 import BeautifulSoup
import requests as req
import pandas as pd

sayfa = 1

dictt = {"Urun Başlığı":[],
		 "Link":[],
		 "Marka":[],
		 "İşletim Sistemi":[],
		 "Dahili Hafıza":[],
		 "RAM Kapasitesi":[],
		 "Ekran Cinsi":[],
		 "Ekran Çözünürlüğü":[],
		 "Kamera Çözünürlüğü":[],
		 "Batarya Kapasitesi Aralığı":[],
		 "Mobil Bağlantı Hızı":[],
		 "Ekran Boyutu":[],
		 "Görüntü Teknolojisi":[],
		 "Parmak İzi Okuyucu":[],
		 "Yüz Tanıma":[],
		 "Suya/Toza Dayanıklılık":[],
		 "Çift Hat":[],
		 "Arttırılabilir Hafıza (Hafıza Kartı Desteği)":[],
		 "Ekran Yenileme Hızı":[],
		 "Fiyat":[]}

dicttFlag = {"İşletim Sistemi":[0],
		     "Dahili Hafıza":[0],
		     "RAM Kapasitesi":[0],
		     "Ekran Cinsi":[0],
		     "Ekran Çözünürlüğü":[0],
		     "Kamera Çözünürlüğü":[0],
		     "Batarya Kapasitesi Aralığı":[0],
		     "Mobil Bağlantı Hızı":[0],
		     "Ekran Boyutu":[0],
		     "Görüntü Teknolojisi":[0],
		     "Parmak İzi Okuyucu":[0],
		     "Yüz Tanıma":[0],
		     "Suya/Toza Dayanıklılık":[0],
		     "Çift Hat":[0],
		     "Arttırılabilir Hafıza (Hafıza Kartı Desteği)":[0],
		     "Ekran Yenileme Hızı":[0]}
count = 0
while True:
	if(sayfa == 41):
		print("Sayfa Bitti")
		break
	#Siteye request atar.
	response = req.get("https://www.trendyol.com/akilli-cep-telefonu-x-c109460?pi={}".format(sayfa))
	#200 döner ise bağlantı başarılı.
	print(response)
	html = response.content
	#htmle ulaşır.
	Soup = BeautifulSoup(html,"html.parser")
	#classı belirlenen divleri alır.
	div = Soup.find_all("div",{"class":"p-card-chldrn-cntnr"})

	for i in div:
	
		#div içindeki a etiketli verileri alır.
		link = i.find("a")
		print("https://www.trendyol.com"+link["href"])
		#Ürünün linkine gider
		response = req.get("https://www.trendyol.com"+link["href"])
		print(response)
		html = response.content
		Soup = BeautifulSoup(html,"html.parser")
		#ürünün özelliklerini çeker
		li = Soup.find_all("li",{"class":"detail-attr-item"})
		pr = Soup.find("h1",{"class":"pr-new-br"})

		try:

			marka = pr.find("a").text

		except:

			marka = ''

		price = Soup.find("span",{"class":"prc-slg"})
		fiyat = price.text
		fiyat = fiyat.replace('.','')

		try:

			fiyat = fiyat.removesuffix(' TL')
		
			if float(fiyat) < float(1000):
				print(fiyat)
				continue

		except:

			a = fiyat
			a = a.split(',')
			a = a[0]

			print(a)
			fiyat = str(a)

			if float(a) < float(1000):
				print(fiyat)
				continue

		fiyat = str(fiyat) + ' TL'
		dictt['Fiyat'].append(fiyat)
		print("Fiyat = ",fiyat)
		dictt['Link'].append("https://www.trendyol.com"+link["href"])

        #Marka
		print(marka)
        #başlık
		print(pr.text)
		dictt['Urun Başlığı'].append(pr.text)
		dictt['Marka'].append(marka)

		dicttFlag['İşletim Sistemi'][0] = 0
		dicttFlag['Dahili Hafıza'][0] = 0
		dicttFlag['RAM Kapasitesi'][0] = 0
		dicttFlag['Ekran Cinsi'][0] = 0
		dicttFlag['Ekran Çözünürlüğü'][0] = 0
		dicttFlag['Kamera Çözünürlüğü'][0] = 0
		dicttFlag['Batarya Kapasitesi Aralığı'][0] = 0
		dicttFlag['Mobil Bağlantı Hızı'][0] = 0
		dicttFlag['Ekran Boyutu'][0] = 0
		dicttFlag['Görüntü Teknolojisi'][0] = 0
		dicttFlag['Parmak İzi Okuyucu'][0] = 0
		dicttFlag['Yüz Tanıma'][0] = 0
		dicttFlag['Suya/Toza Dayanıklılık'][0] = 0
		dicttFlag['Çift Hat'][0] = 0
		dicttFlag['Arttırılabilir Hafıza (Hafıza Kartı Desteği)'][0] = 0
		dicttFlag['Ekran Yenileme Hızı'][0] = 0

		for j in li:

			#İstenilen özellikleri sırasıyla yazdırır.
			if(j.find("span").text == "İşletim Sistemi"):
				print(j.find("b").text)
				dicttFlag['İşletim Sistemi'][0] = 1
				dictt['İşletim Sistemi'].append(j.find("b").text)

			if(j.find("span").text == "Dahili Hafıza"):
				print(j.find("b").text)
				dicttFlag['Dahili Hafıza'][0] = 1
				dictt['Dahili Hafıza'].append(j.find("b").text)

			if(j.find("span").text == "RAM Kapasitesi"):
				print(j.find("b").text)
				dicttFlag['RAM Kapasitesi'][0] = 1
				dictt['RAM Kapasitesi'].append(j.find("b").text)

			if(j.find("span").text == "Ekran Cinsi"):
				print(j.find("b").text)
				dicttFlag['Ekran Cinsi'][0] = 1
				dictt['Ekran Cinsi'].append(j.find("b").text)

			if(j.find("span").text == "Ekran Çözünürlüğü"):
				print(j.find("b").text)
				dicttFlag['Ekran Çözünürlüğü'][0] = 1
				dictt['Ekran Çözünürlüğü'].append(j.find("b").text)

			if(j.find("span").text == "Kamera Çözünürlüğü"):
				print(j.find("b").text)
				dicttFlag['Kamera Çözünürlüğü'][0] = 1
				dictt['Kamera Çözünürlüğü'].append(j.find("b").text)

			if(j.find("span").text == "Batarya Kapasitesi Aralığı"):
				print(j.find("b").text)
				dicttFlag['Batarya Kapasitesi Aralığı'][0] = 1
				dictt['Batarya Kapasitesi Aralığı'].append(j.find("b").text)

			if(j.find("span").text == "Mobil Bağlantı Hızı"):
				print(j.find("b").text)
				dicttFlag['Mobil Bağlantı Hızı'][0] = 1
				dictt['Mobil Bağlantı Hızı'].append(j.find("b").text)

			if(j.find("span").text == "Ekran Boyutu"):
				print(j.find("b").text)
				dicttFlag['Ekran Boyutu'][0] = 1
				dictt['Ekran Boyutu'].append(j.find("b").text)

			if(j.find("span").text == "Görüntü Teknolojisi"):
				print(j.find("b").text)
				dicttFlag['Görüntü Teknolojisi'][0] = 1
				dictt['Görüntü Teknolojisi'].append(j.find("b").text)

			if(j.find("span").text == "Parmak İzi Okuyucu"):
				print(j.find("b").text)
				dicttFlag['Parmak İzi Okuyucu'][0] = 1
				dictt['Parmak İzi Okuyucu'].append(j.find("b").text)

			if(j.find("span").text == "Yüz Tanıma"):
				print(j.find("b").text)
				dicttFlag['Yüz Tanıma'][0] = 1
				dictt['Yüz Tanıma'].append(j.find("b").text)

			if(j.find("span").text == "Suya/Toza Dayanıklılık"):
				print(j.find("b").text)
				dicttFlag['Suya/Toza Dayanıklılık'][0] = 1
				dictt['Suya/Toza Dayanıklılık'].append(j.find("b").text)

			if(j.find("span").text == "Çift Hat"):
				print(j.find("b").text)
				dicttFlag['Çift Hat'][0] = 1
				dictt['Çift Hat'].append(j.find("b").text)

			if(j.find("span").text == "Arttırılabilir Hafıza (Hafıza Kartı Desteği)"):
				print(j.find("b").text)
				dicttFlag['Arttırılabilir Hafıza (Hafıza Kartı Desteği)'][0] = 1
				dictt['Arttırılabilir Hafıza (Hafıza Kartı Desteği)'].append(j.find("b").text)

			if(j.find("span").text == "Ekran Yenileme Hızı"):
				print(j.find("b").text)
				dicttFlag['Ekran Yenileme Hızı'][0] = 1
				dictt['Ekran Yenileme Hızı'].append(j.find("b").text)

		try:		
			if dicttFlag['İşletim Sistemi'][0] == 0:
				dictt['İşletim Sistemi'][count] = ''
		except:
			dictt['İşletim Sistemi'].append('')

		try:
			if dicttFlag['Dahili Hafıza'][0] == 0:
				dictt['Dahili Hafıza'][count] = ''
		except:
			dictt['Dahili Hafıza'].append('')

		try:
			if dicttFlag['RAM Kapasitesi'][0] == 0:
				dictt['RAM Kapasitesi'][count] = ''
		except:
			dictt['RAM Kapasitesi'].append('')

		try:
			if dicttFlag['Ekran Cinsi'][0] == 0:
				dictt['Ekran Cinsi'][count] = ''
		except:
			dictt['Ekran Cinsi'].append('')

		try:
			if dicttFlag['Ekran Çözünürlüğü'][0] == 0:
				dictt['Ekran Çözünürlüğü'][count] = ''
		except:
			dictt['Ekran Çözünürlüğü'].append('')

		try:
			if dicttFlag['Kamera Çözünürlüğü'][0] == 0:
				dictt['Kamera Çözünürlüğü'][count] = ''
		except:
			dictt['Kamera Çözünürlüğü'].append('')

		try:
			if dicttFlag['Batarya Kapasitesi Aralığı'][0] == 0:
				dictt['Batarya Kapasitesi Aralığı'][count] = ''
		except:
			dictt['Batarya Kapasitesi Aralığı'].append('')

		try:
			if dicttFlag['Mobil Bağlantı Hızı'][0] == 0:
				dictt['Mobil Bağlantı Hızı'][count] = ''
		except:
			dictt['Mobil Bağlantı Hızı'].append('')

		try:
			if dicttFlag['Ekran Boyutu'][0] == 0:
				dictt['Ekran Boyutu'][count] = ''
		except:
			dictt['Ekran Boyutu'].append('')

		try:
			if dicttFlag['Görüntü Teknolojisi'][0] == 0:
				dictt['Görüntü Teknolojisi'][count] = ''
		except:
			dictt['Görüntü Teknolojisi'].append('')

		try:
			if dicttFlag['Parmak İzi Okuyucu'][0] == 0:
				dictt['Parmak İzi Okuyucu'][count] = ''
		except:
			dictt['Parmak İzi Okuyucu'].append('')

		try:
			if dicttFlag['Yüz Tanıma'][0] == 0:
				dictt['Yüz Tanıma'][count] = ''
		except:
			dictt['Yüz Tanıma'].append('')

		try:
			if dicttFlag['Suya/Toza Dayanıklılık'][0] == 0:
				dictt['Suya/Toza Dayanıklılık'][count] = ''
		except:
			dictt['Suya/Toza Dayanıklılık'].append('')

		try:
			if dicttFlag['Çift Hat'][0] == 0:
				dictt['Çift Hat'][count] = ''
		except:
			dictt['Çift Hat'].append('')

		try:
			if dicttFlag['Arttırılabilir Hafıza (Hafıza Kartı Desteği)'][0] == 0:
				dictt['Arttırılabilir Hafıza (Hafıza Kartı Desteği)'][count] = ''
		except:
			dictt['Arttırılabilir Hafıza (Hafıza Kartı Desteği)'].append('')

		try:
			if dicttFlag['Ekran Yenileme Hızı'][0] == 0:
				dictt['Ekran Yenileme Hızı'][count] = ''
		except:
			dictt['Ekran Yenileme Hızı'].append('')

		count+=1
		print("****************************")


	sayfa+=1

data = pd.DataFrame(dictt)
data.to_csv("out.csv",index=False)