# Dog Breed Identification

## About
This project is a deep learning-based **dog breed identification** system using the **ResNet** architecture. The model classifies images of dogs into one of **six breeds**:

- Dalmatian
- German Shepherd
- Husky
- Pug
- Rottweiler
- Shih Tzu

Since the trained model is **over 200MB**, it is not included in this repository. Users must **train the model themselves** and place it in the appropriate directory.

## Features
- Upload an image of a dog to predict its breed.
- Uses a **pre-trained ResNet model** for high accuracy.
- Web interface built with **Flask**.
- Allows users to train the model with their dataset.

## Setup Guide
### 1. Clone the Repository
```sh
git clone https://github.com/dixith12/Dog_Breed_Identification.git
cd Dog_Breed_Identification
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install -r requirements.txt
```

### 3. Train the Model
Since the model is not included, you need to train it yourself:
1. **Collect a dataset** with images of the six dog breeds.
2. **Upload the dataset to Google Drive**.
3. Open and run the **Google Colab notebook** provided in `train_model.ipynb`.
4. Download the trained model and place it inside a folder named `model/` in the project directory.

### 4. Run the Application
Start the Flask app:
```sh
python app.py
```
Then, open your browser and visit:
```
http://127.0.0.1:5000/
```

## Screenshots
<p align="center">
  <img src="https://github.com/user-attachments/assets/0b561833-ceb1-4689-8f08-a63d0d773113" width="48%" height="600">
  <img src="https://github.com/user-attachments/assets/8c8ef2e5-db09-4a74-993b-6c94742154da" width="48%" height="600">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/587dab34-bcb3-47df-aae0-eb4a11ca1eda" width="48%" height="600">
  <img src="https://github.com/user-attachments/assets/19c7ad46-71cf-43f9-88de-34405d185c2e" width="48%" height="600">
</p>

## Notes
- Users must **create a `model/` folder** and place their trained model inside it.
- Dataset collection and preprocessing must be done manually.
- If you encounter issues, ensure all dependencies are installed correctly.

Happy coding! 🚀
