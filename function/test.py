import sys
import time
import socket
import threading
import json

#SERVER = 'localhost'
SERVER = '127.0.0.1'
WAITING_PORT = 8765
KEY_ID = 'takemoto'

LOOP_INTERVAL = 5
data

def server_test(server_v1=SERVER, waiting_port_v1=WAITING_PORT):

    stop_event = threading.Event()

    def recv_data1024(socket1, client_address1):
        try:
            data_r = socket1.recv(1024)
            data_r_str = data_r.decode('utf-8')

            # JSON文字列としてパース
            try:
                data_r_list = json.loads(data_r_str)
                print('I (the server) have just received the data __')
                for entry in data_r_list:
                    print(f"Temperature: {entry['temperature']}  Humidity: {entry['humidity']}")
                print('__ from the client. ' + str(client_address1))
            except json.JSONDecodeError:
                print('Failed to decode JSON:', data_r_str)

            time.sleep(LOOP_INTERVAL)

            print("Now, closing the data socket.")
            socket1.close()
        except Exception as e:
            print("Exception in recv_data1024:", e)

    # socoket for waiting of the requests.
    # AF_INET     : IPv4
    # SOCK_STREAM : TCP
    socket_w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_w.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    node_s = server_v1
    port_s = waiting_port_v1
    socket_w.bind((node_s, port_s)) 

    BACKLOG = 5
    socket_w.listen(BACKLOG)

    print('Waiting for the connection from the client(s). '
        + 'node: ' + node_s + '  '
        + 'port: ' + str(port_s))

    def accept_connections():
        while not stop_event.is_set():
            try:
                socket_w.settimeout(1)
                socket_s_r, client_address = socket_w.accept()
                print('Connection from ' 
                    + str(client_address) 
                    + " has been established.")

                thread = threading.Thread(target=recv_data1024, 
                    args=(socket_s_r, client_address),
                    daemon=True)
                thread.start()
            except socket.timeout:
                continue

    accept_thread = threading.Thread(target=accept_connections)
    accept_thread.start()

    try:
        while not stop_event.is_set():
            time.sleep(1)

    except KeyboardInterrupt:
        print("Ctrl-C is hit!")
        stop_event.set()
        accept_thread.join()
        print("Now, closing the waiting socket.")
        socket_w.close()

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT
    key_id_v = KEY_ID

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]

        if ("-h" == option_key):
            count = count + 1
            hostname_v = sys.argv[count]

        if ("-p" == option_key):
            count = count + 1
            waiting_port_v = int(sys.argv[count])

        if ("-k" == option_key):
            count = count + 1
            key_id_v = sys.argv[count]

        count = count + 1

    print(hostname_v)
    print(waiting_port_v)
    
    server_test(hostname_v, waiting_port_v)