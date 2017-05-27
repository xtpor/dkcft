
import sys
import random
import struct
import socket

LOGIN = 3
COMMAND = 2

request_id = random.randint(0, 65535)


def encode(request_id, packet_type, payload):
    pad = '\x00\x00'
    length = 4 + 4 + len(payload) + 2
    return struct.pack('<iii', length, request_id, packet_type) + payload + pad


def recv(sock):
    length, request_id, packet_type = struct.unpack('<iii', sock.recv(12))
    payload = sock.recv(length - 4 - 4 - 2)
    pad = sock.recv(2)
    assert pad == '\x00\x00'
    return request_id, payload


def send_auth_packet(sock, password):
    return sock.send(encode(request_id, LOGIN, password))


def send_command_packet(sock, command):
    return sock.send(encode(request_id, COMMAND, command))


def recv_auth_packet(sock):
    rid, _ = recv(sock)
    return rid == request_id


def recv_command_packet(sock):
    rid, payload = recv(sock)
    assert rid == request_id
    return payload

if __name__ == '__main__':
    addr = (sys.argv[1].split("@")[1], 25575)
    password = sys.argv[2]

    sock = socket.create_connection(addr)
    send_auth_packet(sock, password)

    if not recv_auth_packet(sock):
        sys.exit(-1)

    while True:
        line = sys.stdin.readline()
        if line == '':
            break

        send_command_packet(sock, line)
        print recv_command_packet(sock)

    sock.close()
