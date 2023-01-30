import subprocess

def memory_dump():
    pid = input("Enter the PID of the process to dump: ")
    filename = input("Enter the name of the file to save the dump: ")
    subprocess.call(["gcore", "-o", filename, pid])
    print("Memory dump saved to", filename)

memory_dump()