import os

print("Current working directory is:")
print(os.getcwd())  # cwd - current working directory

print("Changing current directory - going one folder up")
os.chdir("../")
print("Current working directory is:")
print(os.getcwd())

print("Creating new folders")
os.makedirs("./dir1/dir2/dir3")

print("Listing content of the current directory")
print(os.listdir("./"))
