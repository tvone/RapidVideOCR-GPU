from rapid_videocr import RapidVideOCR
import glob
import os

model_v3 = "models/japan_PP-OCRv3_rec_infer.onnx"
model_v4 = "models/japan_PP-OCRv4_rec_infer.onnx"
extractor = RapidVideOCR(rec_model_path=model_v4, det_use_cuda=True, cls_use_cuda=True, rec_use_cuda=True)

rgb_dir = "images"
save_dir = "outputs"
# save_name = "sub_ocr_new"

for folder in glob.glob(os.path.join(rgb_dir, "*/")):
    if os.path.isdir(folder):
        folder_name = os.path.basename(os.path.normpath(folder))
        print(f"\nProcessing directory: {folder}\n")
        # outputs/a.srt  outputs/a.txt
        extractor(folder, save_dir, save_name=folder_name)



