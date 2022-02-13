![](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) ![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

![phone01(1)](https://user-images.githubusercontent.com/54184905/153725790-b827f7c0-4034-47dd-a10e-6e9b377eed6b.jpg)


#  Trendyol Smartphone Price Prediction 

This web application makes a price estimate based on the features of your dream phone, thus allowing you to determine the features of your dream phone according to your budget. Web application takes predictions from the model created using smartphone data pulled from Trendyol e-commerce site, the phone features entered are given to the linear regression model and a price estimate is obtained.

[**The deployed version of the website**](http://52.45.118.34/)

[**Dataset Kaggle link**](https://www.kaggle.com/ahmetfurkandemr/trendyol-smartphones)

[**Our work on the dataset (GPU)**](https://www.kaggle.com/ahmetfurkandemr/trendyol-phone-price-prediction-with-rapids)

[**Our work on the dataset (CPU)**](https://www.kaggle.com/ahmetfurkandemr/trendyol-phone-price-prediction-with-sklearn-cpu)

![Adsız](https://user-images.githubusercontent.com/54184905/153725585-9559cfb8-3941-4789-90b9-1bcde469beb0.png)


```
Trendyol Smartphone Price Prediction 
│
├── FlaskWeb
│   ├── mainWeb.py
│   └── templates
│       ├── about.html
│       ├── formhelpers.html
│       ├── form_template.html
│       ├── HomePage.html
│       ├── includes
│       │   ├── footer.html
│       │   ├── navbar.html
│       │   └── Trendyol_item.jpg
│       ├── Trendyol_item.jpeg
│       ├── Trendyol_item.jpg
│       ├── Trendyol_item.svg
│       └── website-background-3.jpg
├── GetData
│   └── GetData.py
├── Readme.md
├── requirements.txt
└── ServerAPI
    ├── finalized_model.sav
    ├── mainServer.py
    ├── model.py
    └── __pycache__
        └── model.cpython-39.pyc
```

To use the web application on your own computer, install the python packages with the command below.

```bash
sudo pip3 install -r requirements.txt
```

* **Running the Server API**

    This API passes incoming parameters to the model and receives a price estimate, then passes that estimate back to the website. You can deploy the API with the following command.

    ```bash
    sudo python3 mainServer.py
    ```

    **Warning :** After running this script, change the ip address returned to you with the ip on line 147 of the website, so that the connection is established and there is no error in data transfer.
    
* **Deploying the Flask website**

    This website transmits the data entered by the user to the model via API and receives an estimate and presents this estimate to the user. After changing your ip address with the ip address on line 147, you can run the website with the command below.

    ```bash
    sudo python3 mainWeb.py
    ```

### Developers of the project

[**Ahmet Furkan DEMIR**](https://www.linkedin.com/in/1dfurkan/)

[**Batuhan Türk**](https://www.linkedin.com/in/batuhan-t%C3%BCrk-6621b118b/)
