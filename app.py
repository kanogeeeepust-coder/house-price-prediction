#Gradio Deployment
!pip install gradio

import gradio as gr

def predict_house(income, house_age, rooms, bedrooms, population):
    prediction = loaded_pipeline.predict([[income, house_age, rooms, bedrooms, population]])[0]
    return f"${prediction:,.0f}"

interface = gr.Interface(
    fn=predict_house,
    inputs=[
        gr.Slider(20000, 100000, value=60000, label="Avg. Area Income"),
        gr.Slider(1, 10, value=5, label="Avg. Area House Age"),
        gr.Slider(1, 10, value=6, label="Avg. Area Number of Rooms"),
        gr.Slider(1, 6, value=3, step=1, label="Avg. Area Number of Bedrooms"),
        gr.Slider(10000, 70000, value=30000, label="Area Population")
    ],
    outputs=gr.Textbox(label="Predicted Price"),
    title="🏠 House Price Predictor"
)

interface.launch(share=True)

