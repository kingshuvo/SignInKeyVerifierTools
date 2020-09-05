import subprocess
import time
import os

# checking and deleting old test result files
os.remove("gp_output.txt") if os.path.exists("gp_output.txt") else None
os.remove("ga_output.txt") if os.path.exists("ga_output.txt") else None

print("Please Enter App Name:")
app_name = input()

print("Enter GA-APK location to proceed SignInKey Verificaiton")
apk_path_ga = input()

print()
print()

print("Enter GP-APK location to proceed SignInKey Verificaiton")
apk_path_gp = input()

print("Please wait....")
print()

with open('gp_output.txt', 'w') as f:
    subprocess.run("keytool -printcert -jarfile " + apk_path_gp, stdout=f, text=True)

with open('ga_output.txt', 'w') as f:
    subprocess.run("keytool -printcert -jarfile " + apk_path_ga, stdout=f, text=True)

print("=========================================================================================")
print("Test Name: App Store SignIn Key Verificaiton")
print()
print("App Name: ", app_name)
print()

file_gp = open("gp_output.txt", "r")
file_ga = open("ga_output.txt", "r")

file_list_gp = []

for line in file_gp:
    file_list_gp.append(line)
    if "SHA256" in line:
        skey_gp = line[10:]
        print("GP KEY= ", skey_gp)
        break

file_list_ga = []

for line in file_ga:
    file_list_ga.append(line)
    if "SHA256" in line:
        skey_ga = line[10:]
        print("GA KEY= ", skey_ga)
        break

file_gp.close()
file_ga.close()

if skey_ga == skey_gp:
    print("Result: 'Passed'# SignIn Key exactly matched.")
else:
    print("Result: 'Failed'# SignIn Key does not matched!")

print("=========================================================================================")
