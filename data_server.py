import function.data_receive as data_receive
import sys

SERVER = 'localhost'
WAITING_PORT = 8765

LOOP_INTERVAL = 5

if __name__ == '__main__':
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
#            print(option_key)
            if ("-h" == option_key):
                count = count + 1
                hostname_v = sys.argv[count]
#                print(option_key, hostname_v)

            if ("-p" == option_key):
                count = count + 1
                waiting_port_v = int(sys.argv[count])
#               print(option_key, waiting_port_v)

            count = count + 1

    print(hostname_v)
    print(waiting_port_v)
    
    data_receive.server_test(hostname_v, waiting_port_v)

