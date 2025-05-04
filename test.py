import AI_module
import Ocr_module
# test_ai=AI_module.Ai()
# print(test_ai.get_concise_answer("你好")) # 调用简单回答的AI
test_ocr = Ocr_module.OCR()
print(test_ocr.image_to_text("1.png"))  # 通过图片路径调用文字识别
