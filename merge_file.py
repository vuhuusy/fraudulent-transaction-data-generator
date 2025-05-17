import os
import glob

input_dir = r"C:\Users\vuhuu\MyFolder\Desktop\fraudulent-transaction-data-generator\output\year=2024"
output_file = os.path.join(input_dir, "merged_transactions.csv")

csv_files = glob.glob(os.path.join(input_dir, "*.csv"))
csv_files.sort()  # sắp xếp để dễ kiểm soát thứ tự

total_lines = 0
header_written = False

with open(output_file, 'w', encoding='utf-8') as fout:
    for file in csv_files:
        with open(file, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
            if not lines:
                continue
            header = lines[0]
            data_lines = lines[1:]
            
            if not header_written:
                fout.write(header)
                header_written = True
            
            fout.writelines(data_lines)
            file_line_count = len(data_lines)
            total_lines += file_line_count
            print(f"Gộp: {os.path.basename(file)} ({file_line_count} dòng)")

print(f"\n✅ Đã gộp {len(csv_files)} file.")
print(f"📊 Tổng số dòng dữ liệu (không tính header): {total_lines:,}")
print(f"📄 File đầu ra: {output_file}")
