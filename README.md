🌤️ Cincinnati Weather Forecast Model (GenAFOB)
A reproducible, modular ML pipeline for hourly weather forecasting in Cincinnati. Built for the AI Accelerate Hackathon, this project demonstrates how to design restart safe pipelines, train and evaluate models, and deploy them with a simple Gradio web app.
🚀 Demo
Try the live app here:
GenaFOB - a Hugging Face Space by avya04
✨ Features
•	End to end pipeline: data ingestion → preprocessing → training → evaluation → deployment
•	Restart safe: artifacts are versioned (models/) and a deployable model is always saved (model-app/model.pkl)
•	Metrics: MAE and R² reported for validation
•	Interactive UI: Gradio app for quick predictions
•	Future predictions: saves results to predictions/future_predictions.csv
📂 Project Structure
ai-pipeline/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── model-app/
│   ├── app.py          # Gradio app
│   └── model.pkl       # Deployed model
│
├── src/
│   └── train.py        # Training script
│
├── models/             # Versioned models
│   └── xgb_model_<timestamp>.joblib
│
└── predictions/
    └── future_predictions.csv

⚡ Quickstart
1. Clone the repo
git clone https://github.com/FlickM10/cincinnati-weather-forecast.git
cd cincinnati-weather-forecast
2. Install dependencies
pip install -r requirements.txt
3. Run the app locally
cd model-app
python app.py
# open http://127.0.0.1:7860
4. Retrain the model
python src/train.py
This will:
•	Train an XGBoost model
•	Save a versioned model in models/
•	Update model-app/model.pkl
•	Generate predictions/future_predictions.csv
🛠️ Tech Stack
•	Python
•	XGBoost
•	Scikit-learn
•	Pandas / NumPy
•	Gradio
•	Matplotlib
•	Open-Meteo API (data source)
📈 Results
•	Achieved strong validation metrics (low MAE, high R²)
•	Demonstrated reproducibility and modular design
•	Delivered a working demo app for real time predictions


---


