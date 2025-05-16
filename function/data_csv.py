import csv

DATA_DIR = 'work/data'
CSV_FILENAME = 'csv_sample.csv'
filename = DATA_DIR + '/' + CSV_FILENAME

def csv_write_iterator(data_r_list):
    with open(filename, mode='a', newline='') as f:
        write_iter = csv.writer(f)
        for row in data_r_list:
            tempe = row.get("temperature", row.get("temp_dht_1", "N/A"))
            humid = row.get("humidity", row.get("humid_dht_1", "N/A"))
            write_iter.writerow([tempe, humid])

def csv_read_one_file():
    with open(filename) as f:
        all_data = f.read()
        print(all_data)

def csv_read_iterator():
    with open(filename) as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            print(row)

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    csv_read_iterator()
    data_r_list = [
        {"temperature": 25.0, "humidity": 60.0},
        {"temperature": 26.5, "humidity": 65.0},
        {"temperature": 27.0, "humidity": 70.0}
    ]
    csv_write_iterator(data_r_list)