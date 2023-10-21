#!/usr/bin/env python3 
import subprocess
import os
import sys
import threading
# a quick scan to find the open ports with --min-rate 15000;
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    else:
        print(f"Directory '{directory}' already exists.")

def write_output_to_file(output, ip, file_suffix):
    new_dir = "nmap"
    create_directory(new_dir)
    
    file_path = f"{new_dir}/{ip}_{file_suffix}.nmap"
    print(f"writing the output to {file_path}")
    with open(file_path, 'w') as f:
        f.write(output)
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
            g = open(f"nmap/00{IP}_AllInOne.nmap","a")
            f.write(f"{stdout.decode('utf-8')}")
            g.write(f"{stdout.decode('utf-8')}")
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
        output = stdout.decode('latin1')
        print(stdout.decode('utf-8'))
        print(f"writing the output to nmap/{IP}_Fullscan.nmap")
        
        f = open(f"nmap/{IP}_FullScan.nmap",'w')
        g = open(f"nmap/00{IP}_AllInOne.nmap","a")

        decoded_output = stdout.decode('latin1')

        f.write(decoded_output)
        g.write(decoded_output)

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
        g = open(f"nmap/00{IP}_AllInOne.nmap","a")
        f.write(f"{stdout.decode('utf-8')}")
        g.write(f"{stdout.decode('utf-8')}")
        
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
        g = open(f"nmap/00{IP}_AllInOne.nmap","a")

        f.write(f"{stdout.decode('utf-8')}")
        g.write(f"{stdout.decode('utf-8')}")
        

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
        g = open(f"nmap/00{IP}_AllInOne.nmap","a")

        f.write(f"{stdout.decode('utf-8')}")   
        g.write(f"{stdout.decode('utf-8')}")
if __name__ == "__main__":
    if len(sys.argv) != 2 or os.getuid() != 0:
        print("further in the script I run a UDP scan which requires root privileges")
        print("Usage: sudo python3 nmap_automater.py <IP>")
        sys.exit(1)
    else:
        IP = sys.argv[1]
        open_ports = quickScan(IP)
        if not open_ports:
            print("""No ports were open. There can be a few problems:
                1. Machine is not pingable.
                2. I am using --min-rate 15000 and some older machines do not respond back. Try a basic scan.
                3. Check the IP address.""")
            exit()

        t4 = threading.Thread(target=FullScanOnOpenPorts, args=(IP, open_ports,))
        t4.start() 

        t1 = threading.Thread(target=AllPortScan, args=(IP,))
        t1.start()

        t2 = threading.Thread(target=UDPtop20Ports, args=(IP,))
        t2.start()

        t3 = threading.Thread(target=UDPtop200Ports, args=(IP,))
        t3.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
