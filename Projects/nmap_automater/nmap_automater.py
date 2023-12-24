#!/usr/bin/env python3 
import subprocess
import os
import sys
import threading
# a quick scan to find the open ports with --min-rate 15000;
def quickScan(IP):
    command = f"nmap -p- --min-rate 15000 {IP}" 
    print(f"command to be executed {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode == 0:
        print(stdout.decode('utf-8'))
        
        command2 = "grep 'open' | awk -F/ '{print $1}'"
        process2 = subprocess.Popen(command2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout2, stderr2 = process2.communicate(input=stdout)
        
        if process2.returncode == 0:
            openPorts = stdout2.decode('utf-8').split()
            new_dir = "nmap"

            # Check if the directory already exists
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
                print(f"Directory '{new_dir}' created successfully.")
            else:
                print(f"Directory '{new_dir}' already exists.")
            
            print(f"writing The output to nmap/{IP}_allPorts.nmap")
            f = open(f"nmap/{IP}_allPorts.nmap","w")
            f.write(f"{stdout.decode('utf-8')}")
            print(f"performing a Full Scan on these open ports -> {openPorts}")
            # print(stdout2.decode('utf-8'))
            return(openPorts)
        else:
            print(f"Error executing command2: {stderr2.decode('utf-8')}")
    else:
        print(f"Error executing command: {stderr.decode('utf-8')}")

# running full scan  
def FullScanOnOpenPorts(ip, openPorts):
    result = ','.join(openPorts)
    command = f"nmap -sC -sV -p{result} {ip}" 
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        output = stdout.decode('utf-8')
        print(stdout.decode('utf-8'))
        print(f"writing the output to nmap/{IP}_Fullscan.nmap")
        f = open(f"nmap/{IP}_FullScan.nmap",'w')
        f.write(f"{stdout.decode('utf-8')}")
        
    else:
        print(f"Error executing command: {stderr.decode('utf-8')}")

# a udp scan for top 20 ports
def UDPtop20Ports(ip):
    command = f"sudo nmap -sU -sC --top-ports 20 {ip}" 
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        output = stdout.decode('utf-8')
        print(stdout.decode('utf-8'))
        print(f"writing the output to nmap/{ip}_Top20UdpPorts.nmap")
        f = open(f"nmap/{ip}_Top20UdpPorts.nmap",'w')
        f.write(f"{stdout.decode('utf-8')}")
        
    else:
        print(f"Error executing command: {stderr.decode('utf-8')}")

# a udp scan for top 200 ports
def UDPtop200Ports(ip):
    command = f"sudo nmap -sU -sC --top-ports 200 {ip}" 
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        output = stdout.decode('utf-8')
        print(stdout.decode('utf-8'))
        print(f"writing the output to nmap/{ip}_Top200UdpPorts.nmap")
        f = open(f"nmap/{ip}_Top200UdpPorts.nmap",'w')
        f.write(f"{stdout.decode('utf-8')}")
        

    else:
        print(f"Error executing command: {stderr.decode('utf-8')}")

# running a all ports nmap scan without min-rate, as sometimes using min-rate 15000 misses some ports.

def AllPortScan(ip):
    command = f"nmap -sC -sV -p- {ip}" 
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        output = stdout.decode('utf-8')
        print(stdout.decode('utf-8'))
        print(f"writing the output to nmap/{ip}_AllPortsFullScan.nmap")
        f = open(f"nmap/{ip}_AllPortsFullScan.nmap",'w')
        f.write(f"{stdout.decode('utf-8')}")   


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("further in the script i run a udp scan which requires root privilleges")
        print("Usage: sudo python3 nmap_automater.py <IP>")
    else:
        IP = sys.argv[1]
        openPorts = quickScan(IP)
        if(not openPorts):
            print("""Not ports were open There can be few problems
                1. machine is not pingable
                2. I am using --min-rate 15000 some older machines, do not respond back try a basic scan
                3. Check the IP address""")
            exit()
        t4 = threading.Thread(target=FullScanOnOpenPorts, args=(IP,openPorts,))
        t4.start() 

        t1 = threading.Thread(target=AllPortScan, args=(IP,))
        t1.start()

        t2 = threading.Thread(target=UDPtop20Ports, args=(IP,))
        t2.start()

        t3 = threading.Thread(target=UDPtop200Ports, args=(IP,))
        t3.start()


