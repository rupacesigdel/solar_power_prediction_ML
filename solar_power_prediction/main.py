import joblib
import pandas as pd
import os

BASE_DIR = r'C:\Users\a2z\OneDrive\Desktop\solar_power_prediction'
MODEL_PATH = os.path.join(BASE_DIR, 'outputs', 'models', 'solar_model.pkl')

def predict_generation(peak_load, yield_val):
    """
    Loads the trained Random Forest model and predicts Solar Energy.
    """
    if not os.path.exists(MODEL_PATH):
        print(f"ERROR: Model file not found at {MODEL_PATH}")
        print("Please run 'model_training.ipynb' first to generate the model.")
        return None

    try:
        model = joblib.load(MODEL_PATH)
        
        input_data = pd.DataFrame(
            [[peak_load, yield_val]], 
            columns=['Peak_load_KW', 'Specific_Yield']
        )
        
        prediction = model.predict(input_data)
        return prediction[0]
    
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        return None

if __name__ == "__main__":
    print("\n" + "="*40)
    print("   SOLAR POWER PREDICTION SYSTEM (2081)")
    print("="*40)
    
    try:
        p_load = float(input("Enter expected Peak Load (KW): "))
        s_yield = float(input("Enter historical Specific Yield (kWh/kWp): "))
        
        result = predict_generation(p_load, s_yield)
        
        if result is not None:
            print("\n" + "-"*40)
            print(f"SUCCESS: Predicted Solar Generation")
            print(f"Result: {result:.2f} KWH")
            print("-"*40)
            
    except ValueError:
        print("INVALID INPUT: Please enter numeric values only.")
    
    input("\nPress Enter to exit...")
