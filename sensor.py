import function.data_dht11 as dht11
import function.data_send as data_send
import sys

SERVER = 'localhost'
WAITING_PORT = 8765

WAIT_INTERVAL = 2

if __name__ == "__main__":
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
        #print(option_key)
        if ("-h" == option_key):
            count = count + 1
            hostname_v = sys.argv[count]
            #print(option_key, hostname_v)
        if ("-p" == option_key):
            count = count + 1
            waiting_port_v = int(sys.argv[count])
            #print(option_key, port_v)
        if ("-m" == option_key):
            count = count + 1
            message_v = sys.argv[count]
            #print(option_key, message_v)

        count = count + 1

    #data_s_list = dht11.test_get_dht_data()
    # テスト用のデータを作成
    
    data_s_list = [
        {"temperature": 25.0, "humidity": 60.0},
        {"temperature": 24.0, "humidity": 65.0}
    ]

    print(hostname_v)
    print(waiting_port_v)
    print("data_s_list: ", data_s_list)

    data_send.send_data(data_s_list, hostname_v, waiting_port_v)