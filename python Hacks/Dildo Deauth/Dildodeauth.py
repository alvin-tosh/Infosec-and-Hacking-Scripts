import nmap
import socket

# Define the target network 
target_network = "192.168.1.0/24"

# Initialize the nmap
nm_scan = nmap.PortScanner()

# scan the target network
nm_scan.scan(target_network, arguments='-sP')

# Iterate through the list of hosts found 
for host in nm_scan.all_hosts():
    # Check if the host is up
    if nm_scan[host].state() == "up":
        # Get the banner of the host
        try:
            banner = socket.getfqdn(host)
        except:
            banner = "No banner"

        # Check if any of the brand names match the banner or hostname
        if any(brand in banner for brand in ["Lovense", "We-Vibe", "Vibease", "Kiiroo", "Sybian", "Rubsy", "Svakom", "Huang"]):
            # Print the IP address and banner of the device
            print(f"Device found: {host} ({banner})")
