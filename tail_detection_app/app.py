import gradio as gr
import cv2
import numpy as np
from src.predict import TailDetector
from pathlib import Path

#инициализация детектора
model_path = Path("models/tail_model_20260220_1348.pt")
detector = TailDetector(model_path, confidence=0.20)

def process_image(image, confidence):
    """Обрабатывает загруженное изображение"""
    detector.confidence = confidence
    result = detector.predict_with_mask(image)
    return result

#создаем интерфейс
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(label="Загрузите фото кота"),
        gr.Slider(minimum=0.05, maximum=0.5, value=0.20, step=0.05,
                  label="Порог уверенности")
    ],
    outputs=gr.Image(label="Результат с маской хвоста"),
    title="Детектор хвостов",
    description="Загрузите фото кота, и модель покажет, где находится хвост",
    examples=[
        ["examples/cat1.jpg", 0.20],
        ["examples/cat2.jpg", 0.20],
    ]
)

if __name__ == "__main__":
    iface.launch(share=True)