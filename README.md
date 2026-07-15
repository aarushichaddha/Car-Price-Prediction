# Car Price Prediction Web Application

This is a Machine Learning based web application built with Flask that predicts the selling price of a used car based on various features such as its age, present price, kilometers driven, fuel type, seller type, and transmission type.

## Project Structure

- `app.py`: The main Flask application script that handles routing and prediction logic.
- `model.py`: The machine learning script used to train the Random Forest Regressor model and save it.
- `dataset/`: Directory containing the dataset (`car data.csv`) used for training the model.
- `prediction_model.pkl`: The trained Random Forest model saved as a pickle file.
- `columns.pkl`: The list of feature columns required by the model (saved during training to ensure the input data structure matches).
- `templates/`: Directory containing the HTML templates (`index.html`).
- `static/`: Directory containing static files like CSS and images.

## Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas
- **Frontend**: HTML, CSS

## Prerequisites

Make sure you have Python installed on your system (Python 3.x is recommended). You will also need the following Python packages:
- Flask
- pandas
- scikit-learn

You can install the required packages using pip:
```bash
pip install Flask pandas scikit-learn
```

## How to Run Locally

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/Car Price Prediction
   ```
3. (Optional) If you want to retrain the machine learning model, run the `model.py` script:
   ```bash
   python model.py
   ```
   This will generate/update the `prediction_model.pkl` and `columns.pkl` files.
4. Start the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage

1. Open the web application in your browser.
2. Fill in the car details in the provided form:
   - **Car Age**: Age of the car in years.
   - **Present Price**: Current ex-showroom price of the car (in lakhs).
   - **Kilometers Driven**: Total distance the car has been driven.
   - **Owner**: Number of previous owners (e.g., 0 for first owner).
   - **Fuel Type**: Select Petrol, Diesel, or CNG.
   - **Seller Type**: Select Dealer or Individual.
   - **Transmission Type**: Select Manual or Automatic.
3. Click on the "Predict" button to get the estimated selling price of the car.

## Model Details

The underlying machine learning model is a `RandomForestRegressor` with 500 estimators. It is trained on the provided dataset after applying data preprocessing steps, such as:
- Calculating the car's age from its manufacturing year (relative to the current year).
- Applying one-hot encoding to categorical features (Fuel Type, Seller Type, Transmission) for model compatibility.
