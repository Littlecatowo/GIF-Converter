from PIL import Image, ImageOps
import os

class GIFConverter():
    def __init__(self):
        self.IMG_EXTENSIONS: list[str] = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
        self.IMG_PATH: list[str] = []

    def checkFolder(self):
        if not os.path.exists("./GIF輸出"):
            os.makedirs("./GIF輸出")

        if not os.path.exists("./原圖片在這裡"):
            os.makedirs("./原圖片在這裡")

    def FINDIMAGE(self):
        for file in os.listdir("./"):
            if any(file.lower().endswith(ext) for ext in self.IMG_EXTENSIONS):
                self.IMG_PATH.append(os.path.join("./", file))
            
    def convertToGIF(self):
        if self.IMG_PATH.__len__() == 0:
            print("目前沒有圖片可轉換為GIF格式。")
            return

        for path in self.IMG_PATH:
            print(f"目前正在轉換 -> {os.path.basename(path)}")
            print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            img: Image.Image = Image.open(path)
            img = ImageOps.exif_transpose(img)
            gif_path = os.path.join("./GIF輸出", os.path.splitext(os.path.basename(path))[0] + ".gif")
            img.save(gif_path, 'GIF')
            print(f"轉換前 -> {path}\n轉換後 -> {gif_path}")

            done_path = os.path.join("./原圖片在這裡", os.path.basename(path))
            os.rename(path, done_path)
            print(f"移動原圖片到 -> {done_path}")
            print("───────────────────────────────")

    def RUN(self):
        self.FINDIMAGE()
        self.convertToGIF()
        input("按 Enter 鍵結束視窗...")


GIF = GIFConverter()
GIF.checkFolder()
GIF.RUN()