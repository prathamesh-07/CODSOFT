import scapy.all as scapy
import os
import time
import logging

# Setting up logging
logging.basicConfig(filename='network_forensics.log', 
                    format='%(asctime)s %(message)s', 
                    level=logging.INFO)

# Function to log and print alerts
def log_alert(message):
    print(message)
    logging.info(message)

# Function to sniff packets and analyze them
def packet_sniffer(packet):
    if packet.haslayer(scapy.IP):
        ip_layer = packet.getlayer(scapy.IP)
        log_alert(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

    if packet.haslayer(scapy.TCP):
        tcp_layer = packet.getlayer(scapy.TCP)
        log_alert(f"TCP Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")
        
        if tcp_layer.flags == 'S':  # TCP SYN flag (possible scan)
            log_alert(f"SYN Packet: Possible scan detected from {ip_layer.src} to {ip_layer.dst}")

    if packet.haslayer(scapy.DNS) and packet.getlayer(scapy.DNS).qr == 0:
        dns_layer = packet.getlayer(scapy.DNS)
        log_alert(f"DNS Request: {ip_layer.src} -> {dns_layer.qname.decode()}")

# Function to investigate various logs
def investigate_logs(log_file):
    if not os.path.exists(log_file):
        print("Log file not found!")
        return
    
    with open(log_file, 'r') as file:
        for line in file:
            if "SYN Packet" in line:
                print(f"ALERT: {line.strip()} (Potential Port Scan Detected)")
            if "DNS Request" in line:
                print(f"DNS Query Logged: {line.strip()}")
                
# Start packet sniffing
def start_sniffing(interface):
    log_alert("Starting network traffic monitoring...")
    scapy.sniff(iface=interface, prn=packet_sniffer)

if __name__ == "__main__":
    # Start network monitoring on interface 'eth0'
    start_sniffing('eth0')
    
    # Investigate the logs after sniffing for a certain period
    time.sleep(60)  # Monitor for 60 seconds
    investigate_logs('network_forensics.log')
