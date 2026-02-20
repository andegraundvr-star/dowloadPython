from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path

class TailDetector:
    def __init__(self, model_path, confidence=0.20):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def predict(self, image):
        """Возвращает изображение с маской и контуром"""
        results = self.model(image, conf=self.confidence)

        if len(results[0].boxes) == 0:
            return image

        #получаем изображение с размеченными хвостами
        result_image = results[0].plot()
        return result_image

    def predict_with_mask(self, image):
        """Возвращает изображение с полупрозрачной маской (как в задании)"""
        results = self.model(image, conf=self.confidence)

        if len(results[0].boxes) == 0:
            return image

        #создаем копию изображения
        img_copy = image.copy()

        #для каждого найденного хвоста
        if results[0].masks is not None:
            for mask in results[0].masks.data:
                #конвертируем маску в numpy
                mask_np = mask.cpu().numpy()
                #ресайзим до размера изображения
                mask_resized = cv2.resize(mask_np, (image.shape[1], image.shape[0]))

                #создаем полупрозрачную маску (красную)
                colored_mask = np.zeros_like(image)
                colored_mask[:, :, 0] = 255 * mask_resized  # красный канал

                #накладываем с прозрачностью 40%
                img_copy = cv2.addWeighted(img_copy, 0.6, colored_mask, 0.4, 0)

        return img_copy