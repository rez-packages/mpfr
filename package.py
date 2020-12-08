name = "mpfr"
version = "4.1.0"

variants=[["platform-linux", "arch-x86_64"]]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")


