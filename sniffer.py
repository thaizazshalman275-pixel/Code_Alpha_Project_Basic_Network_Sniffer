from scapy.all import sniff, IP, TCP
from datetime import datetime
from collections import Counter

# -------------------------
# CONFIG
# -------------------------
LOG_FILE = "log.txt"
MAX_PACKETS = 50  # change or set None for unlimited (not recommended)

packet_count = 0
ip_counter = Counter()

# -------------------------
# LOG FUNCTION
# -------------------------
def write_log(data):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data + "\n")

# -------------------------
# PACKET PROCESSOR
# -------------------------
def process_packet(packet):
    global packet_count

    if not packet.haslayer(IP) or not packet.haslayer(TCP):
        return

    ip = packet[IP]
    tcp = packet[TCP]

    # HTTP / HTTPS filter only
    if tcp.dport not in [80, 443] and tcp.sport not in [80, 443]:
        return

    packet_count += 1

    src_ip = ip.src
    dst_ip = ip.dst
    src_port = tcp.sport
    dst_port = tcp.dport

    protocol = "HTTPS" if 443 in [src_port, dst_port] else "HTTP"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = (
        f"{timestamp} | Packet {packet_count} | "
        f"{src_ip}:{src_port} → {dst_ip}:{dst_port} | {protocol}"
    )

    print(log_line)
    write_log(log_line)

    # Track IP activity
    ip_counter[src_ip] += 1
    ip_counter[dst_ip] += 1

# -------------------------
# START SNIFFER
# -------------------------
print("🔥 Professional Network Sniffer Started")
print("📡 Capturing HTTP/HTTPS traffic only...")
print("📁 Logging to log.txt")
print("⛔ Stops automatically after limit OR Ctrl + C\n")

sniff(
    prn=process_packet,
    store=False,
    timeout=60,  # safety stop (60 seconds max run)
    stop_filter=lambda x: packet_count >= MAX_PACKETS
)

# -------------------------
# FINAL REPORT
# -------------------------
print("\n==============================")
print("📊 FINAL NETWORK REPORT")
print("==============================")
print("Total Packets:", packet_count)

print("\n🌐 TOP ACTIVE IPs:")
for ip, count in ip_counter.most_common(5):
    print(f"{ip} → {count} packets")

print("==============================")