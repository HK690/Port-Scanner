import socket
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from tqdm import tqdm

from common_ports import COMMON_PORTS
from banner import grab_banner
from report import save_reports

# Initialize colorama
init(autoreset=True)

open_ports = []


def resolve_target(target):
    """Resolve hostname to IP address."""
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(Fore.RED + f"[ERROR] Unable to resolve hostname: {target}")
        exit()


def get_service(port):
    """Return known service name."""
    return COMMON_PORTS.get(port, "Unknown")


def scan_port(ip, port, timeout=1):
    """Scan a single TCP port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((ip, port))

        if result == 0:
            service = get_service(port)
            banner = grab_banner(ip, port)

            data = {
                "port": port,
                "service": service,
                "banner": banner
            }

            open_ports.append(data)

            print(
                Fore.GREEN +
                f"[OPEN] Port {port:<5} | {service:<15} | {banner}"
            )

        sock.close()

    except Exception:
        pass


def scan(ip, start_port, end_port, threads):
    """Perform multithreaded port scan."""

    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + f"Target : {ip}")
    print(Fore.CYAN + f"Ports  : {start_port}-{end_port}")
    print(Fore.CYAN + "=" * 60)

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:

        futures = []

        for port in range(start_port, end_port + 1):
            futures.append(
                executor.submit(scan_port, ip, port)
            )

        for _ in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="Scanning",
            colour="green"
        ):
            pass

    end_time = time.time()

    elapsed = round(end_time - start_time, 2)

    print("\n" + "=" * 60)

    print(Fore.YELLOW + f"Scan Completed")
    print(Fore.YELLOW + f"Open Ports : {len(open_ports)}")
    print(Fore.YELLOW + f"Time Taken : {elapsed} seconds")

    print("=" * 60)

    save_reports(ip, open_ports)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Advanced Python Port Scanner"
    )

    parser.add_argument(
        "target",
        help="Target IP or Hostname"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting Port"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=1024,
        help="Ending Port"
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=100,
        help="Number of Threads"
    )

    parser.add_argument(
        "--common",
        action="store_true",
        help="Scan Common Ports Only"
    )

    return parser.parse_args()


def scan_common_ports(ip, threads):
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "Scanning Common Ports")
    print(Fore.CYAN + "=" * 60)

    start = time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:

        futures = []

        for port in COMMON_PORTS.keys():
            futures.append(
                executor.submit(scan_port, ip, port)
            )

        for _ in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="Scanning",
            colour="green"
        ):
            pass

    end = time.time()

    print("\nScan Finished")

    print(Fore.YELLOW + f"Open Ports : {len(open_ports)}")
    print(Fore.YELLOW + f"Time Taken : {round(end-start,2)} sec")

    save_reports(ip, open_ports)


def main():

    args = parse_arguments()

    ip = resolve_target(args.target)

    print(Fore.BLUE + f"Resolved Target: {ip}\n")

    if args.common:
        scan_common_ports(ip, args.threads)

    else:
        scan(
            ip,
            args.start,
            args.end,
            args.threads
        )


if __name__ == "__main__":
    main()
