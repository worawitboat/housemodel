from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from .models import Species, Feature

# Create your views here.
def index(req):
    result = Species.objects.get(pk=1)
    sepal_length = 0.0
    sepal_width = 0.0
    petal_length = 0.0
    petal_width = 0.0
    if req.method == 'POST':
        print('เขา POST มา')
        #print(req.POST)
        sepal_length = float(req.POST['sepal_length'])
        sepal_width = float(req.POST['sepal_width'])
        petal_length = float(req.POST['petal_length'])
        petal_width = float(req.POST['petal_width'])
        print(sepal_length)
        print(sepal_width)
        print(petal_length)
        print(petal_width)
        # from sklearn.svm import LinearSVC 
        # model = LinearSVC() 
        # features = Feature.objects.all()
        # a, t = [], []
        # for f in features:
        #     a.append([ f.sepal_length, f.sepal_width, f.petal_length, f.petal_width ])
        #     t.append(f.species.sid-1)
        import numpy as np
        fm = np.array([[sepal_length, sepal_length, petal_length, petal_width]])
        from joblib import load
        model = load('irisapp/static/iris.model')
        x = model.predict(fm)
        print( type(x) )
        print( type(x[0]) )
        result = Species.objects.get(pk=x[0]+1)
    else:
        print('เขากด enter มา')
    return render(req, 'irisapp/index.html', { 
        'result': result,
        'sepal_length': sepal_length, 
        'sepal_width': sepal_width, 
        'petal_length': petal_length,
        'petal_width': petal_width,
    })

def api_species(req):
    # 1. JsonResponse() // ภากร
    # 2. serializer // 
    # 3. json.dumps() // Nim, 
    import json
    species = Species.objects.all();
    data = serializers.serialize('json', species, fields=('sid', 'name'))
    data = json.loads(data)
    return JsonResponse(data, safe=False)
