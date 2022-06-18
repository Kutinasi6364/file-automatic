import os
import sys

from tkinter import filedialog
from pdfminer.high_level import extract_text

file_type = [("pdfファイル","*.pdf")] 
file_dir = r"C:\Users\Kutinasi\Desktop\Program\python\file-automatic"

# ファイル選択ダイアログ表示
pdf_file = filedialog.askopenfilename(filetypes = file_type, initialdir = file_dir) 
# ファイルを選択しなかったら終了
if pdf_file == "":
  sys.exit()

# 拡張子をのぞいたファイル名取得
pdf_name = os.path.splitext(os.path.basename(pdf_file))[0]
pdf_text = extract_text(pdf_file)
print(pdf_text)

# テキストファイルに保存
with open(pdf_name + ".txt", "w", newline="", encoding="utf-8_sig") as cf:
    cf.write(pdf_text)