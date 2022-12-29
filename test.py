import os
from pathlib import Path

if __name__ == "__main__":
    # with open(f"C:/Users/User/Desktop/test.txt".replace("\\", "/"), "w") as f:
    #     f.write("Test!!")
    with open(f"{str(Path.home())}\\Desktop\\test.txt".replace("\\", "/"), "w") as f:
        f.write("Test!!!!!!")
    # os.system("mkdir C:\\Users\\User\\Desktop\\Test123")

