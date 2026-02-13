# Network Tools

Simple CLI tools for network traffic analysis.

## Tools

### pcap-analyze.py
Analyze PCAP files and search for flags.
```bash
python pcap-analyze.py capture.pcap
```

**Note**: Requires scapy library (optional dependency).

### http-extract.sh
Extract HTTP traffic from PCAP files.
```bash
./http-extract.sh capture.pcap
```

## Common Patterns
- Packet sniffing
- Protocol analysis
- Traffic reconstruction
- Password extraction
- DNS exfiltration
