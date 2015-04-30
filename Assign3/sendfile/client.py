import socket
import os
import sys

class Client:
	def __init__(self, addr, port):
		self._server_addr = addr
		self._server_port = port
		self._client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def get_server_addr(self):
		return self._server_addr

	def get_server_port(self):
		return self._server_port

	def get_conn_sock(self):
		return self._conn_sock

	server_addr = property(get_server_addr)
	server_port = property(get_server_port)
	client_sock = property(get_conn_sock)

	def connect_to_server(self):
		#client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_sock.connect(server_addr, server_port)

	def get_user_command(self):
		return input("ftp> ")

	def send_to_server(self, info):
		client_sock.send(info)

	def verify_command(self, cmd):
		if cmd[0:3] == 'lsl':
			#client performs an ls command on its list of files
			pass
		if cmd[0:3] == 'get':
			#client requests file from server
			pass
		if cmd[0:3] == 'put':
			#client places file to server
			pass
		if cmd[0:2] == 'ls':
			#request server to perform an ls command on its current directory
			pass


def main()
	client = Client('localhost', 1234)


if __name__ == '__main__':
	main()