from django.shortcuts import render
from joblib import load
import numpy as np


# Create your views here.
def index(req):
    X1 = 0.0
    X2 = 0.0
    X3 = 0.0
    X4 = 0.0
    X5 = 0.0
    X6 = 0.0
    X = 'สแดงผล'
    if req.method == 'POST':
        print('เขา POST มา')
        X1 = float(req.POST['X1'])
        X2 = float(req.POST['X2'])
        X3 = float(req.POST['X3'])
        X4 = float(req.POST['X4'])
        X5 = float(req.POST['X5'])
        X6 = float(req.POST['X6'])
        fm = np.array([[X1, X2, X3, X4, X5, X6]])
        md = load('./houseapp/static/houseapp.model')
        X = md.predict(fm)
    return render(req, 'houseapp/index.html' ,{ 
        'result': X,
        'X1': X1, 
        'X2': X2, 
        'X3': X3,
        'X4': X4,
        'X5': X5,
        'X6': X6,
    })