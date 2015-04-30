import socket


class Server:
	def __init__(self):
		self._listen_port = 1234
		self._welcome_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._client_sock = None
		self._addr = None


	def get_port(self):
		return self._listen_port

	def get_sock(self):
		return self._welcome_sock

	def get_client_sock(self):
		return self._client_sock

	def set_client_sock(self, sock):
		self._client_sock = sock

	def get_addr(self):
		return self._addr

	def set_addr(self, addr):
		self._addr = addr

	listen_port = property(get_port)
	client_sock = property(get_client_sock, set_client_sock)
	addr = property(get_addr, set_addr)

	def hey_listen(self):
		self.welcome_sock.listen(1)

	def wait_for_connections(self):
		print("Waiting for connections...")
		self.client_sock, self.addr = self.welcome_sock.accept()
		print("Accepted connection from client: {}".format(addr))
		print("/n")

	def bind_port(self):
		client_sock.bind('', self.listen_port)

	def wait_for_command(self):
		while 1:
			self.wait_for_connections()
		#file_data = ""
		#recv_buff = ""
		#string_size = 0
		#string_size_buff = ""
		pass

def main():
	serv = Server()
	serv.bind_port()
	serv.hey_listen()
	serv.wait_for_command


if __name__ == '__main__':
	main()