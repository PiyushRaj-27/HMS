from django.shortcuts import render, HttpResponse
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
# Create your views here.
def predict(request):
    return render(request, "prediction.html")

def diabetes(request):
    context = {"checked": False}
    if request.method == "POST":
        preg = float(request.POST["pregnancies"])
        gluc = float(request.POST["glucose"])
        bp = float(request.POST["bp"])
        skin = float(request.POST["skin"])
        insulin = float(request.POST["insulin"])
        bmi = float(request.POST["bmi"])
        dpf = float(request.POST["dpf"])
        age = float(request.POST["age"])
        loaded_model = pickle.load(open("D:\College Files\Sem5\Assignment\HMLS\hms\diseases\diabetes.pkl",'rb'))
        diabetes_dataset = pd.read_csv('D:\College Files\Sem5\Assignment\HMLS\hms\diseases\diabetes.csv')
        X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
        scaler = StandardScaler()
        scaler.fit(X)
        input_data = (preg, gluc, bp, skin, insulin, bmi, dpf, age)
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        std_data = scaler.transform(input_data_reshaped)
        prediction = loaded_model.predict(std_data)
        context = {}
        if prediction[0] == 0:
            context["result"] = False
            context["checked"] = True
        else:
            context["result"] = True
            context["checked"] = True
        return render(request, "predictDiabetes.html", context)
    return render(request, "predictDiabetes.html")