# Solar Power Generation Prediction
An Industrial Engineering approach to forecasting solar energy output using Machine Learning and Satellite-derived Meteorological data.

## 📌 Project Overview
This project predicts the daily energy generation (KWH) for a 1MW solar power plant located in **Kapilvastu, Nepal**. By integrating plant operational logs with **NASA POWER API** weather data, the system uses a **Random Forest Regressor** to provide accurate forecasts and a 365-day predictive horizon.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Data Science:** Pandas, NumPy, Scikit-Learn
- **Weather Data:** NASA POWER API (REST API)
- **Serialization:** Joblib (for model saving)
- **Visualization:** Matplotlib, Seaborn

## 📂 Project Structure
```text
solar_power_prediction/
├── data/
│   ├── raw/                # Original Excel logs from the plant
│   ├── processed/          # Cleaned data and Master Dataset (Solar + Weather)
│   └── weather/            # NASA API downloaded CSVs
├── outputs/
│   ├── models/             # Trained .pkl model files (v1 and v2)
│   └── plots/              # Generated forecast graphs and heatmaps
├── nasa_weather.py         # Script to fetch solar irradiance & temp from NASA
├── model_training.ipynb    # Training logic and Performance Evaluation
├── main.py                 # Real-time manual prediction script
└── forecast_year.py        # Generates the 365-day seasonal forecast

```
## 👤 Author
- **Researcher:** Rupesh Sigdel
- **Institution:** Tribhuvan University, IOE-Thapathali Campus
- **Department:** Industrial Engineering

## 🛠️ How to Run the System
Follow these steps in order to replicate the results:

1. **Pre-process Data:** Run `preprocessing.ipynb` to clean the raw logs, handle date formats, and calculate **Specific Yield**.
2. **Fetch Weather:** Run `nasa_weather.py` to pull historical **Solar Irradiance** and **Temperature** data for the Kapilvastu coordinates ($27.65^\circ N, 83.05^\circ E$).
3. **Train Model:** Run `model_training.ipynb`. This trains the Random Forest model and saves it as `solar_model_v2.pkl`.
4. **Generate Forecast:** Run `python forecast_year.py` to generate the 365-day CSV and the seasonal generation plot.

## 📊 Model Performance & Validation
The model was evaluated against a 20% test split with the following results:
- **Coefficient of Determination ($R^2$):** 0.99 (99% Accuracy in variance explanation)
- **Mean Absolute Error (MAE):** ~164.77 KWH
- **Root Mean Square Error (RMSE):** ~347.36 KWH

## 📈 Key Engineering Insights
- **Seasonal Analysis:** The model effectively predicts the "Monsoon Dip" (low irradiance) and "Summer Peaks" typical of the Terai region.
- **Variable Correlation:** Solar Irradiance and Peak Load are the primary drivers of the system's energy output.
- **Practical Utility:** This tool assists in grid stability analysis and maintenance scheduling for the Kapilvastu power plant.

### **How to use this file:**
1. Open **VS Code**.
2. Create a new file in your main folder (`solar_power_prediction`) and name it exactly **`README.md`**.
3. Paste the text above into it and save.
4. If you have the "Markdown Preview" extension in VS Code, press `Ctrl + Shift + V` to see it looking professional with bold text and tables.

### **Why this helps your Seminar:**
When you show your folder to your internal or external examiner, having a `README.md` shows that you follow **Professional Software Standards**. It makes your project look like a "Product" rather than just a few scattered scripts.

**Would you like me to add a "License" section (like MIT License) to the README to make it look even more official?**