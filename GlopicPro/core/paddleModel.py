

from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os



class PaddleModel:
    
    def __init__(self, path):
        
        print("heloooooooooooooooooooooooooooooo         ;jlknfvdnbkgvrekjgvdfbvk.jdsfbnvkjdfsbngk")
        self.ocr_model = PaddleOCR(lang='en')
        
        self.path = path
    
    
    def saveRes(self):
        
        
        result = self.ocr_model.ocr(self.path)
        
        # for i in result[0]:
        #     print(i[1][0])
        
        print("##################################################################################################################################")
        print(result[0])
        
        boxes = [res[0] for res in result[0]] # 
        texts = [res[1][0] for res in result[0]]
        scores = [res[1][1] for res in result[0]]
        
        font_path = os.path.join('GlopicPro/paddleModules/PaddleOCR', 'doc', 'fonts', 'latin.ttf')
        
        img = cv2.imread(self.path) 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        
        plt.figure(figsize=(15,15))

        annotated = draw_ocr(img, boxes, texts, scores, font_path=font_path) 
        
        cv2.imshow("image", annotated)
        
        # annotated.save("GlopicPro/media/result.png")
        
        # save the annotated as jpg image
        
                
        
        
        