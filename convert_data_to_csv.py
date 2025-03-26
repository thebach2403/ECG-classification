
import os #làm vc với thư mục tệp
import wfdb
import csv
import glob

# create csv folder
csv_folder_name = "ECG__csv_folder"  #make name
os.makedirs(csv_folder_name, exist_ok= True)

#func to convert 
raw_data_path = "E:/pv/WORKING/ECG Project/mit-bih-arrhythmia-database-1.0.0"

def convert_to_csv(patient_number):
    
    record = wfdb.rdrecord(f"{raw_data_path}/{patient_number}")
    leads = record.sig_name    #lấy tên kênh lead
    ecg_data = record.p_signal # lấy dữ liệu digi ra
    fs = record.fs  # tần số lấy mẫu
    
    #tính thời gian mỗi mẫu
    time_ms = [(i*1000) / fs for i in range(len(ecg_data))]
        
    #tạo đường dẫn lưu file csv mới
    csv_path = os.path.join(csv_folder_name, f"{patient_number}.csv")

    #open file csv đẻ làm vc, with open tự động đóng file khi xong
    with open(csv_path, "w", newline='') as outfile:
        writer = csv.writer(outfile)
        #viết header 
        writer.writerow(["index","time_ms"] + leads)      
        for i in range(len(ecg_data)):
            writer.writerow([i, time_ms[i]] + list (ecg_data[i]))


#quét để tìm các tệp hea
hea_files = glob.glob(os.path.join(raw_data_path,"*.hea"))

#Lấy patient_id từ tên file
patient_ids = [os.path.splitext(os.path.basename(f))[0] for f in hea_files]

print(f"Tìm thấy {len(patient_ids)} bệnh nhân.")

# Chuyển tất cả sang CSV
for pid in patient_ids:
    convert_to_csv(pid)
print("done")



























