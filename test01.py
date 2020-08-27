import os
import csv

#pythonファイルを置いているパス
path = os.getcwd()
#ディレクトリ名
dir_name = os.path.basename(path)
#CSVファイル名
csv_file = dir_name + ".csv"
#CSVファイルの中身
file_list = []

for file in os.listdir("."):
    # ファイルかどうか
    is_file = os.path.isfile(file)
    # このpyファイル自身でないか
    not_py_file = os.path.basename(__file__) != file

    if is_file and not_py_file:
        file_list.append([file])

with open(csv_file, "w", encoding="Shift_jis", newline="") as f:
    csv_writer = csv.writer(f)
    for r in file_list:
        csv_writer.writerow(r)