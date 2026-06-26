import socket
from datetime import datetime
from colorama import Fore, Style


def get_timestamp():
    """
    Returns the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_target(target):
    """
    Checks whether a hostname or IP address can be resolved.
    """
    try:
        socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False


def print_banner():
    """
    Prints the application banner.
    """

    print(Fore.CYAN + "=" * 70)
    print(Fore.CYAN + "          ADVANCED PYTHON PORT SCANNER")
    print(Fore.CYAN + "=" * 70)
    print(Fore.WHITE + "Author : Harshal Kapse")
    print(Fore.WHITE + "Version: 1.0")
    print(Fore.WHITE + "Protocol: TCP")
    print(Fore.CYAN + "=" * 70)


def print_scan_summary(target, elapsed_time, open_ports):
    """
    Prints the scan summary.
    """

    print("\n" + Fore.CYAN + "=" * 70)

    print(Fore.GREEN + "Scan Summary")

    print(Fore.CYAN + "=" * 70)

    print(f"Target        : {target}")
    print(f"Scan Finished : {get_timestamp()}")
    print(f"Time Taken    : {elapsed_time:.2f} seconds")
    print(f"Open Ports    : {len(open_ports)}")

    print(Fore.CYAN + "=" * 70)


def resolve_hostname(hostname):
    """
    Resolves hostname to IP.
    """
    try:
        return socket.gethostbyname(hostname)
    except:
        return None


def format_service(service):
    """
    Returns formatted service name.
    """
    if service:
        return service.upper()

    return "UNKNOWN"


def separator():
    """
    Prints a separator line.
    """
    print("-" * 70)


def success(message):
    print(Fore.GREEN + "[SUCCESS] " + Style.RESET_ALL + message)


def info(message):
    print(Fore.CYAN + "[INFO] " + Style.RESET_ALL + message)


def warning(message):
    print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + message)


def error(message):
    print(Fore.RED + "[ERROR] " + Style.RESET_ALL + message)