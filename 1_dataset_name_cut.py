# -*- coding: utf-8 -*-
"""
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
フォルダの画像データの名前を数字の連番のみにする

dataset_n/
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


"""
import os
import shutil

src_root = "dataset_j"
dst_root = "dataset_n"

# 出力フォルダ作成
for i in range(10):
    os.makedirs(os.path.join(dst_root, str(i)), exist_ok=True)

# 各フォルダを処理
for label in range(10):
    src_dir = os.path.join(src_root, str(label))
    dst_dir = os.path.join(dst_root, str(label))

    if not os.path.isdir(src_dir):
        continue

    files = sorted(os.listdir(src_dir))
    
    counter = 1

    for file in files:
        src_path = os.path.join(src_dir, file)

        # 画像以外は無視
        if not os.path.isfile(src_path):
            continue

        # 連番のファイル名（例：00001.jpg）
        new_name = f"{counter:05d}.jpg"
        dst_path = os.path.join(dst_dir, new_name)

        shutil.copy(src_path, dst_path)
        counter += 1

print("✔ 連番変更して dataset_n にコピー完了！")
