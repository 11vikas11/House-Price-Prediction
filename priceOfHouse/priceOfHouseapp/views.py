from django.shortcuts import render
import joblib
import numpy as np
from .forms import HousePriceForm

# Load trained model
model = joblib.load('ml_model/model.pkl')

def predict_price(request):
    prediction = None
    if request.method == "POST":
        form = HousePriceForm(request.POST)
        if form.is_valid():
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            sqft = form.cleaned_data['sqft']
            location = form.cleaned_data['location']
            
            # Prepare input data
            features = np.array([[bedrooms, bathrooms, sqft, location]])
            
            # Make prediction
            prediction = model.predict(features)[0]

    else:
        form = HousePriceForm()

    return render(request, 'index.html', {'form': form, 'prediction': prediction})
