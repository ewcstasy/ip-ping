import os
import platform

def ping_host(host):
    # Check the system platform
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Ping the specified host
    response = os.system(f"ping {param} 4 {host}")
    
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is unreachable")

if __name__ == "__main__":
    host_to_ping = input("Enter the IP address or hostname to ping: ")
    ping_host(host_to_ping)
