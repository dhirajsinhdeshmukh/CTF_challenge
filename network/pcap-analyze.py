#!/usr/bin/env python3
"""Simple packet analyzer for PCAP files"""

import sys

def analyze_pcap(pcap_path):
    """Basic PCAP analysis"""
    try:
        from scapy.all import rdpcap, IP, TCP, UDP, Raw
    except ImportError:
        print("Error: scapy required. Install with: pip install scapy", file=sys.stderr)
        sys.exit(1)
    
    try:
        packets = rdpcap(pcap_path)
        print(f"\nPCAP Analysis: {pcap_path}")
        print("-" * 50)
        print(f"Total packets: {len(packets)}")
        
        # Count protocols
        tcp_count = sum(1 for p in packets if TCP in p)
        udp_count = sum(1 for p in packets if UDP in p)
        
        print(f"TCP packets: {tcp_count}")
        print(f"UDP packets: {udp_count}")
        
        # Extract IPs
        ips = set()
        for pkt in packets:
            if IP in pkt:
                ips.add(pkt[IP].src)
                ips.add(pkt[IP].dst)
        
        print(f"\nUnique IPs: {len(ips)}")
        for ip in sorted(ips):
            print(f"  {ip}")
        
        # Search for flags in payload
        print("\nSearching for flags in payload...")
        for i, pkt in enumerate(packets):
            if Raw in pkt:
                payload = pkt[Raw].load.decode('latin-1', errors='ignore')
                if 'flag' in payload.lower():
                    print(f"Packet {i}: Possible flag found")
                    print(f"  {payload[:100]}")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pcap-analyze.py <pcap-file>")
        sys.exit(1)
    analyze_pcap(sys.argv[1])
