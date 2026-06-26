import os
import csv
import json
from datetime import datetime


def save_reports(target, open_ports):
    """
    Save scan results in TXT, CSV, and JSON formats.
    """

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_file = f"reports/scan_{timestamp}.txt"
    csv_file = f"reports/scan_{timestamp}.csv"
    json_file = f"reports/scan_{timestamp}.json"

    # ---------------- TXT ---------------- #

    with open(txt_file, "w", encoding="utf-8") as f:

        f.write("=" * 60 + "\n")
        f.write("ADVANCED PORT SCANNER REPORT\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Target: {target}\n")
        f.write(f"Scan Time: {datetime.now()}\n")
        f.write(f"Open Ports: {len(open_ports)}\n\n")

        for item in sorted(open_ports, key=lambda x: x["port"]):
            f.write(
                f"Port: {item['port']}\n"
                f"Service: {item['service']}\n"
                f"Banner: {item['banner']}\n"
                + "-" * 50 + "\n"
            )

    # ---------------- CSV ---------------- #

    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Port",
            "Service",
            "Banner"
        ])

        for item in sorted(open_ports, key=lambda x: x["port"]):

            writer.writerow([
                item["port"],
                item["service"],
                item["banner"]
            ])

    # ---------------- JSON ---------------- #

    with open(json_file, "w", encoding="utf-8") as jf:

        json.dump(
            {
                "target": target,
                "scan_time": str(datetime.now()),
                "total_open_ports": len(open_ports),
                "results": sorted(open_ports, key=lambda x: x["port"])
            },
            jf,
            indent=4
        )

    print("\n" + "=" * 60)
    print("Reports Saved Successfully")
    print("=" * 60)
    print(f"TXT  : {txt_file}")
    print(f"CSV  : {csv_file}")
    print(f"JSON : {json_file}")
    print("=" * 60)