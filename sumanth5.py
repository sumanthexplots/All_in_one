#!/usr/bin/env python3

"""
Sumanth Exploits Security Toolkit
Educational Cybersecurity Toolkit
"""

import socket
import threading
import requests
import os
from datetime import datetime

report_file = "security_report.txt"

# ---------------------
# Banner
# ---------------------

import os

def banner():
    os.system("cls" if os.name == "nt" else "clear")

    RED = "\033[91m"
    BLACK = "\033[40m"
    RESET = "\033[0m"

    print(f"""{BLACK}{RED}

 ███████╗██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗████████╗██╗  ██╗
 ██╔════╝██║   ██║████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██║  ██║
 ███████╗██║   ██║██╔████╔██║███████║██╔██╗ ██║   ██║   ███████║
 ╚════██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██╔══██║
 ███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ██║  ██║
 ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝

 ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗███████╗
 ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔════╝
 █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   ███████╗
 ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   ╚════██║
 ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   ███████║
 ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝

        EDUCATIONAL CYBERSECURITY TOOLKIT

{RESET}""")

# ---------------------
# Report Logger
# ---------------------

def log_report(text):

    with open(report_file, "a") as f:
        f.write(f"{datetime.now()} - {text}\n")


# ---------------------
# Multi-threaded Port Scanner
# ---------------------

def scan_port(target, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        log_report(f"Open port {port} on {target}")

    sock.close()


def port_scanner():

    target = input("Enter target IP: ")

    ports = range(1,1025)

    print(f"\nScanning {target}...\n")

    threads = []

    for port in ports:

        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\nScan finished")


# ---------------------
# IP Intelligence
# ---------------------

def ip_lookup():

    ip = input("Enter IP address: ")

    url = f"http://ip-api.com/json/{ip}"

    data = requests.get(url).json()

    print("\nIP Intelligence")
    print("------------------")

    for key in ["country","regionName","city","isp"]:
        print(f"{key}: {data.get(key)}")

    log_report(f"IP lookup performed on {ip}")


# ---------------------
# Email Intelligence
# ---------------------

def email_lookup():

    email = input("Enter email: ")

    domain = email.split("@")[-1]

    print("\nEmail Intelligence")
    print("------------------")
    print("Domain:", domain)

    try:
        ip = socket.gethostbyname(domain)
        print("Server IP:", ip)
    except:
        print("Could not resolve domain")

    log_report(f"Email intelligence lookup for {email}")


# ---------------------
# Basic Username OSINT
# ---------------------

def username_osint():

    username = input("Enter username: ")

    sites = [
        f"https://github.com/{username}",
        f"https://twitter.com/{username}",
        f"https://www.reddit.com/user/{username}"
    ]

    print("\nChecking username presence\n")

    for url in sites:

        try:
            r = requests.get(url, timeout=3)

            if r.status_code == 200:
                print("[FOUND]", url)
                log_report(f"Username found: {url}")

        except:
            pass


# ---------------------
# SSH Log Attack Detector
# ---------------------

def ssh_log_detector():

    logfile = "/var/log/auth.log"

    if not os.path.exists(logfile):
        print("Log file not found.")
        return

    print("\nScanning SSH logs...\n")

    with open(logfile) as f:

        for line in f:

            if "Failed password" in line:
                print("[FAILED LOGIN]", line.strip())
                log_report("SSH failed login detected")


# ---------------------
# Simple Packet Sniffer
# ---------------------

def packet_sniffer():

    print("\nStarting packet sniffer (CTRL+C to stop)\n")

    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:

        raw_data, addr = s.recvfrom(65535)

        print("Packet from:", addr)
        log_report("Packet captured")


# ---------------------
# Menu
# ---------------------

def menu():

    while True:

        banner()

        print("1. Multi-threaded Port Scanner")
        print("2. IP Intelligence Lookup")
        print("3. Email Intelligence")
        print("4. Username OSINT")
        print("5. SSH Attack Detector")
        print("6. Packet Sniffer")
        print("7. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            port_scanner()

        elif choice == "2":
            ip_lookup()

        elif choice == "3":
            email_lookup()

        elif choice == "4":
            username_osint()

        elif choice == "5":
            ssh_log_detector()

        elif choice == "6":
            packet_sniffer()

        elif choice == "7":
            break

        input("\nPress Enter to continue...")

# ---------------------

if __name__ == "__main__":
    menu()
