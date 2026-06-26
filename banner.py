import socket


def grab_banner(ip, port, timeout=2):
    """
    Attempt to grab the service banner from an open port.
    Returns the banner string or 'N/A' if unavailable.
    """

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        sock.connect((ip, port))

        # Send a newline to trigger some services
        try:
            sock.send(b"\r\n")
        except:
            pass

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner[:100]

        return "No Banner"

    except Exception:
        return "N/A"