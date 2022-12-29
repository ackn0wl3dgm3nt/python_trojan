
def copy_binary(src, dst):
    binary_code = None
    with open(src, "rb") as f:
        binary_code = f.read()
    print(binary_code)
    with open(dst, "wb") as f:
        f.write(binary_code)

def get_binary_code(src):
    binary_code = None
    with open(src, "rb") as f:
        binary_code = f.read()
    return binary_code

a = get_binary_code("malware.exe")

# print(a)
#
# with open("malware_2.exe", "wb") as f:
#     f.write(a)

# copy_binary("malware.exe", "malware_2.exe")

# get_binary_code("malware.exe", "malware_2.txt")
