from flask import Flask,render_template, request
import cv2
import numpy as np
import os
from model import predict_class

UPLOAD_FOLDER='static/images'
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/predict", methods = ["POST"])
def prediction():
    upload_file = request.files['upload_file']
    image_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
    upload_file.save(image_path)
    
    model_path = 'model.h5'
    list=["椎茸（シイタケ）" ,"平茸（ヒラタケ）", "杏鮑菇（エリンギ）", "火炎茸（カエンタケ）", "柿占地（カキシメジ）", "臭裏紅茸（クサウラベニタケ）", "卵茸（タマゴタケ）", "毒鶴茸（ドクツルタケ）", "舞茸（マイタケ）"]
    

    pred = predict_class(image_path, model_path)

   
    return render_template("predict.html", pred=list[pred])

if __name__ == "__main__":
    app.run(debug=True)






# from flask import Flask,render_template, request
# import cv2
# import numpy as np
# from model import predict_class

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods = ["POST"])
# def prediction():
#     image_path = 'static/images/image.jpg'
#     model_path = 'model.h5'
#     list=["siitake" ,"hiratake", "eringi", "kaentake", "kakisimeji", "kusaurabenitaketake", "tamagotake", "dokutsurutake", "maitake"]
    

#     pred = predict_class(image_path, model_path)

   
#     return render_template("predict.html", pred=list[pred])

# if __name__ == "__main__":
#     app.run(debug=True)


# <!-- {% extends "layout.html" %}
# {% block content %}
# <main>
    
#     <div class="box">
        
#             <h2 class="result">セリフは{{pred}}</h2>
            
        
#     </div>
        
# </main>
# {% endblock %} -->