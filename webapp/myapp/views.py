from django.shortcuts import render
import numpy as np
def convert_to_ndarray(x):
    #y = np.random.random((6,5))
    x = x.replace('[', '')
    x = x.replace(']', '')
    y = []
    for line in x.split('\n'):
        y.append( list(map(float, line.split())) )
    return np.array(y)
def matmul(req):
    a = convert_to_ndarray('1 2 3\n6 7 7\n8 9 6')
    b = convert_to_ndarray('1 2 3 4 5\n6 7 8 9 1\n9 8 7 6 4')
    if req.method == 'POST':
        a = convert_to_ndarray(req.POST['A'])
        b = convert_to_ndarray(req.POST['B'])
    else:
        pass
    return render(req, 'myapp/matmul.html', {
        'A': a,
        'B': b,
        'C' : np.dot(a,b)
    })