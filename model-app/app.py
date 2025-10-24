import gradio as gr
import pickle
import pandas as pd

# --- Load trained model ---
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Define prediction function ---
def predict(temp, humidity, precipitation_mm, wind):
    input_df = pd.DataFrame([{
        "temp": temp,
        "humidity": humidity,
        "precipitation_mm": precipitation_mm,
        "wind": wind
    }])
    prediction = model.predict(input_df)[0]
    return float(prediction)

# --- Gradio interface with correct inputs ---
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Temperature"),
        gr.Number(label="Humidity"),
        gr.Number(label="Precipitation (mm)"),
        gr.Number(label="Wind Speed")
    ],
    outputs=gr.Number(label="Predicted Target"),
    title="🌤️ Cincinnati Weather Forecast Model",
    description="Enter weather conditions to get a prediction."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
