import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    'data/',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    'data/',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

# Train model
model.fit(train_generator, validation_data=val_generator, epochs=15)

# Save model
model.save('model/cnn_model.h5')
print("Model saved!")
import cv2
import numpy as np
from tensorflow.keras.models import load_model

def load_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128,128))
    img = img/255.0
    return np.expand_dims(img, axis=0)

def predict(image_path, model_path='model/cnn_model.h5'):
    model = load_model(model_path)
    img = load_image(image_path)
    pred = model.predict(img)[0][0]
    return "Fake" if pred>0.5 else "Real"
import streamlit as st
from utils import predict

st.set_page_config(page_title="Deepfake Detection Tool", page_icon="🤖")

st.title("Deepfake Detection Tool 🤖")
st.write("Upload an image to check if it is Real or AI-generated (Deepfake).")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    with open("temp.jpg","wb") as f:
        f.write(uploaded_file.getbuffer())
    result = predict("temp.jpg")
    st.image("temp.jpg", caption='Uploaded Image', use_column_width=True)
    st.success(f"Prediction: {result}")