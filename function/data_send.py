import json
import socket

# Constants
SERVER = 'localhost'
WAITING_PORT = 8765

def send_data(data_s_list, hostname_v=SERVER, waiting_port_v=WAITING_PORT):
    node_s = hostname_v
    port_s = waiting_port_v

    try:
        print("Sending data to server...")
        socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_r_s.connect((node_s, port_s))

        print('Connected to server at {}:{}'.format(node_s, port_s))

        data_s_json = json.dumps(data_s_list)
        data_s = data_s_json.encode('utf-8')
        socket_r_s.send(data_s)
        print("Data sent to server:", data_s_json)

        socket_r_s.recv(1024)

    except KeyboardInterrupt:
        print("Ctrl-C is hit! Ending client.")

    except Exception as e:
        print("Error while sending data:", e)

if __name__ == "__main__":
    # Example data to send
    data_s_list = [
        {"temperature": 25.0, "humidity": 60.0},
        {"temperature": 26.0, "humidity": 65.0}
    ]
    
    # Send the data
    send_data(data_s_list)