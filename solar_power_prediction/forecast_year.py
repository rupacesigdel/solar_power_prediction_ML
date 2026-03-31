import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

BASE_DIR = r'C:\Users\a2z\OneDrive\Desktop\solar_power_prediction'
MODEL_PATH = os.path.join(BASE_DIR, 'outputs', 'models', 'solar_model_v2.pkl')
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'cleaned_solar_data.csv')

if not os.path.exists(DATA_PATH):
    print(f"ERROR: CSV file not found at {DATA_PATH}")
    exit()

history = pd.read_csv(DATA_PATH)

history.columns = [col.strip() for col in history.columns]
mapping = {'Peak load (KW)': 'Peak_load_KW', 'Generated Energy (KWH)': 'Generated_Energy_KWH'}
history = history.rename(columns=mapping)

# CALCULATE STATS & FALLBACKS
monthly_stats = history.groupby('Month')[['Peak_load_KW', 'Specific_Yield']].mean()

# calculates the global average to use for months you DON'T have data for
overall_avg_load = history['Peak_load_KW'].mean()
overall_avg_yield = history['Specific_Yield'].mean()

model = joblib.load(MODEL_PATH)

# GENERATE 365 DAYS FORECAST
start_date = datetime.now()
future_dates = [start_date + timedelta(days=i) for i in range(365)]

forecast_results = []

for date in future_dates:
    month = date.month
    day_of_year = date.timetuple().tm_yday
    
    # if month exists in history, otherwise use global average
    if month in monthly_stats.index:
        est_load = monthly_stats.loc[month, 'Peak_load_KW']
        est_yield = monthly_stats.loc[month, 'Specific_Yield']
    else:
        est_load = overall_avg_load
        est_yield = overall_avg_yield
    
    input_features = pd.DataFrame(
        [[month, day_of_year, est_load, est_yield]], 
        columns=['Month', 'Day_of_Year', 'Peak_load_KW', 'Specific_Yield']
    )
    
    pred_energy = model.predict(input_features)[0]
    forecast_results.append({
        'Date': date.strftime('%Y-%m-%d'), 
        'Month': month,
        'Predicted_Energy_KWH': round(pred_energy, 2)
    })

# CREATE DATAFRAME
forecast_df = pd.DataFrame(forecast_results)

# EXPORT DATA 
output_csv_path = os.path.join(BASE_DIR, 'data', 'processed', 'yearly_forecast_results.csv')
# Ensure the directory exists
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
forecast_df.to_csv(output_csv_path, index=False)

# VISUALIZATION
plt.figure(figsize=(12, 6))
plt.plot(pd.to_datetime(forecast_df['Date']), forecast_df['Predicted_Energy_KWH'], color='darkorange')
plt.title('1-Year Solar Generation Forecast')
plt.xlabel('Date')
plt.ylabel('Energy (KWH)')
plt.grid(True, alpha=0.3)

plot_path = os.path.join(BASE_DIR, 'outputs', 'plots', 'year_forecast.png')
plt.savefig(plot_path)
plt.show()

print(f"\n--- SUCCESS ---")
print(f"1. CSV Saved: {output_csv_path}")
print(f"2. Plot Saved: {plot_path}")