from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
import tensorflow as tf

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def burn_wound(request):
    if request.method == 'POST':
        image_Pixel = 224
        print(request.POST)
        degrees = ['First', 'Second', 'Third']
        model = tf.keras.models.load_model('ml/model.h5')
        print("Name : ", request.POST.get("name"))
        print("Email : ", request.POST.get("email"))
        image_test = request.FILES['test_image']
        image_data = image_test.read()
        image_array = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
        print(image_array.shape)  # Debug statement
        image_array = cv2.resize(image_array, (image_Pixel, image_Pixel))
        img_test = np.expand_dims(image_array, axis=0)
        result = model.predict(img_test)
        prediction = degrees[np.argmax(result.tolist()[0])]
        return render(request, 'index.html', {'prediction': prediction, 'burn_wound': True})
    else:
        return HttpResponse('Not Found')

