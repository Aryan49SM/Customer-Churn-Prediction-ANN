## Introduction
This project aims to predict customer churn and salary using Artificial Neural Networks (ANN). The models are built using TensorFlow and Keras libraries with Python.

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aryan49SM/Customer-Churn-Prediction-ANN.git
   cd Customer-Churn-Prediction-ANN
2. **Create a virtual environment:**
   ```bash
   python -m venv env
3. **Activate the virtual environment:**
   1. On Windows:
      ```bash
      .\env\Scripts\activate
    2. On macOS/Linux:
       ```bash
       source env/bin/activate
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

## Usage
Once you have installed the required dependencies, you can run the Jupyter notebooks provided to train and evaluate the models.

**Run streamlit**
```bash
python -m streamlit run app.py
```

## Model Architecture
* Input Layer
* Multiple Hidden Layers with ReLU activation
* Output Layer with appropriate activation function
* Optimization using Adam optimizer
* Binary Cross-entropy/Mean Absolute Error loss functions
