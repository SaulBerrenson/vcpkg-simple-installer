import os
import platform
from consolemenu import *
from consolemenu.items import *
from os import walk

#VCPKG TRIPLETS DIRECTORY
VCPKG_TRIPLETS_DIR = "C:\\BuildTools\\vcpkg\\triplets"
#EXPORT PKG DIRECTORY
EXPORT_DIR = "C:\\BuildTools\\vcpkg\\export"

#find tripplets at specific folder
def find_triplets():
    tripplets = []
    configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(VCPKG_TRIPLETS_DIR)
    for f in files if f.endswith('.cmake')]
    for path_file in configfiles:
        tripplets.append(os.path.basename(path_file).replace(".cmake",""))
    return tripplets

#shell execute cmd.exe commands
def shell(command):
   os.system(command)

#find pkg
def find_pkg():
    pkg_name = input("Enter library name: ")
    shell("vcpkg search %s" % pkg_name)
    shell("pause")

#install pkg at vcpkg
def install_default_pkg():
    pkg_name = input("Enter library name: ")
    print("Select your tripplet")
    index = 1
    tripplets = find_triplets()
    for tripplet in tripplets:
        print("%s: %s" % (index,tripplet))
        index+=1
    index = int(input("Write index of tripplet -> "))
    full_pkg = "%s:%s" % (pkg_name,tripplets[index-1])
    shell("vcpkg install %s" % full_pkg)
    shell("pause")

#remove pkg at vcpkg
def remove_pkg():
    pkg_name = input("Enter library name: ")
    print("Select your tripplet")
    index = 1
    tripplets = find_triplets()
    for tripplet in tripplets:
        print("%s: %s" % (index,tripplet))
        index+=1
    index = int(input("Write index of tripplet -> "))
    full_pkg = "%s:%s" % (pkg_name,tripplets[index-1])
    shell("vcpkg remove %s" % full_pkg)
    shell("pause")

#install pkg -> export pkg -> remove pkg
def export_pkg():
    pkg_name = input("Enter library name: ")
    print("Select your tripplet")
    index = 1
    tripplets = find_triplets()
    for tripplet in tripplets:
        print("%s: %s" % (index,tripplet))
        index+=1
    index = int(input("Write index of tripplet -> "))
    full_pkg = "%s:%s" % (pkg_name,tripplets[index-1])
    shell("vcpkg install %s" % full_pkg)
    shell("vcpkg export %s --zip --output-dir=%s" % (full_pkg, EXPORT_DIR))
    shell("vcpkg remove %s" % full_pkg)
    shell("pause")

#create interactive menu
def create_menu():
    menu = ConsoleMenu("VCPkg Installer", "Custom installer for vcpkg")
    menu.append_item(FunctionItem("Search package by name", find_pkg))
    menu.append_item(FunctionItem("Install package at default directory", install_default_pkg))
    menu.append_item(FunctionItem("Remove package", export_pkg))
    menu.append_item(FunctionItem("Install package and export to directory", export_pkg))
    return menu

#entry point
def main():   
   create_menu().show()

if __name__=="__main__":
    main()