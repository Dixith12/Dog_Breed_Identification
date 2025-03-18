from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the model
model_path = 'model/improved_dog_breed_model_version.keras'
model = load_model(model_path)

# Define Breed Labels
breed_labels = {
    0: 'Dalmatian',
    1: 'German Shepherd',
    2: 'Husky',
    3: 'Pug',
    4: 'Rottweiler',
    5: 'Shih Tzu'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file is uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        # Save the uploaded file to the static/uploads folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Preprocess the image
        img = load_img(file_path, target_size=(224, 224))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict the breed
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence_score = np.max(predictions) * 100
        predicted_breed = breed_labels.get(predicted_class, "Unknown")

        # Pass the results and file path to the template
        return render_template(
            'index.html',
            uploaded_file=file.filename,
            predicted_breed=predicted_breed,
            confidence_score=f"{confidence_score:.2f}%"
        )

    return render_template('index.html', uploaded_file=None)

if __name__ == '__main__':
    app.run(debug=True)
