# -*- coding: utf-8 -*-
"""
解凍した元データdataのファル形式をjpgに統一する

現在のデータセットは
ASL Digits/asl_dataset_digits/
├── 0
├── 1
├── 2
├── 3
├── 4
├── 5
├── 6
├── 7
├── 8
└── 9
と
ASL Digits/test/
├── 0
├── 1
├── 2
├── 3
├── 4
├── 5
├── 6
├── 7
├── 8
└── 9
です。

これをデータ形式をkpegにするとともに第3ディレクトリで同じものは統合して
dataset_j/
├── 0
├── 1
├── 2
├── 3
├── 4
├── 5
├── 6
├── 7
├── 8
└── 9
とする
"""
import os
import shutil
from PIL import Image
from pathlib import Path

# 元データ
src_dirs = [
    "ASL Digits/asl_dataset_digits",
    "ASL Digits/test"
]

# 出力先
dst_root = "dataset_j"

# JPEG に変換して保存
def convert_to_jpeg(src_path, dst_path):
    try:
        img = Image.open(src_path)
        rgb_img = img.convert("RGB")  # JPEG は RGB
        rgb_img.save(dst_path, "JPEG")
    except Exception as e:
        print(f"Error converting {src_path}: {e}")

# 出力フォルダ作成
for i in range(10):
    os.makedirs(os.path.join(dst_root, str(i)), exist_ok=True)

# 2つの dataset を統合して JPEG 化
for src_dir in src_dirs:
    for label in range(10):
        src_label_dir = os.path.join(src_dir, str(label))
        dst_label_dir = os.path.join(dst_root, str(label))

        if not os.path.isdir(src_label_dir):
            continue

        for file in os.listdir(src_label_dir):
            src_file = os.path.join(src_label_dir, file)

            # 拡張子を jpg に
            stem = Path(file).stem
            dst_file = os.path.join(dst_label_dir, f"{stem}.jpg")

            convert_to_jpeg(src_file, dst_file)

print("✔ 統合と JPEG 変換が完了しました！")

