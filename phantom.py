#!/usr/bin/env python3

import os
import re
import json
import socket
import requests
import concurrent.futures

from bs4 import BeautifulSoup
from colorama import Fore, init
from rich.console import Console
from rich.table import Table
from urllib.parse import urljoin

# =========================
# INIT
# =========================

init(autoreset=True)

console = Console()

CYAN = Fore.CYAN
WHITE = Fore.WHITE
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123 Safari/537.36"
}

# =========================
# CORE
# =========================

def clear():
    os.system("clear")


def banner():

    clear()

    print(f"""{CYAN}

██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝

{WHITE}               STEALTH INTELLIGENCE FRAMEWORK

{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")


def pause():
    input(f"\n{CYAN}Press ENTER to continue...")


def request(url):

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10,
            allow_redirects=True
        )

        return response

    except:
        return None

# =========================
# 01 USERNAME SCANNER
# =========================

def username_scanner():

    banner()

    username = input(f"{GREEN}Username: {WHITE}")

    sites = {
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "Kick": f"https://kick.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "TryHackMe": f"https://tryhackme.com/p/{username}",
        "Replit": f"https://replit.com/@{username}",
        "Behance": f"https://behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Chess": f"https://chess.com/member/{username}"
    }

    found = 0

    print()

    for site, url in sites.items():

        try:

            response = request(url)

            if response and response.status_code in [200, 301, 302]:

                print(f"{GREEN}[FOUND]{WHITE} {site:<15} -> {url}")

                found += 1

        except:
            pass

    print(f"\n{CYAN}Profiles Found:{WHITE} {found}")

    pause()

# =========================
# 02 DNS LOOKUP
# =========================

def dns_lookup():

    banner()

    domain = input(f"{GREEN}Domain: {WHITE}")

    print()

    try:

        ip = socket.gethostbyname(domain)

        print(f"{CYAN}Resolved IP:{WHITE} {ip}")

    except:

        print(f"{RED}Failed to resolve domain.")

    pause()

# =========================
# 03 GEOIP LOOKUP
# =========================

def geoip_lookup():

    banner()

    target = input(f"{GREEN}IP or Domain: {WHITE}")

    print()

    try:

        response = request(f"https://ipinfo.io/{target}/json")

        if response:

            data = response.json()

            table = Table(title="GeoIP Intelligence")

            table.add_column("Field", style="cyan")
            table.add_column("Value", style="white")

            for k, v in data.items():
                table.add_row(str(k), str(v))

            console.print(table)

    except:

        print(f"{RED}Lookup failed.")

    pause()

# =========================
# 04 TECHNOLOGY DETECTOR
# =========================

def tech_detector():

    banner()

    url = input(f"{GREEN}Target URL: {WHITE}")

    response = request(url)

    if not response:

        print(f"{RED}Connection failed.")

        pause()

        return

    body = response.text.lower()

    headers = response.headers

    print()

    if "wordpress" in body:
        print(f"{GREEN}[+] WordPress Detected")

    if "react" in body:
        print(f"{GREEN}[+] React Detected")

    if "vue" in body:
        print(f"{GREEN}[+] Vue Detected")

    if "cloudflare" in body:
        print(f"{GREEN}[+] Cloudflare Detected")

    print(f"\n{CYAN}Server:{WHITE} {headers.get('Server', 'Unknown')}")

    pause()

# =========================
# 05 HTTP HEADER ANALYZER
# =========================

def header_analyzer():

    banner()

    url = input(f"{GREEN}Target URL: {WHITE}")

    response = request(url)

    if not response:

        print(f"{RED}Connection failed.")

        pause()

        return

    table = Table(title="HTTP Headers")

    table.add_column("Header", style="cyan")
    table.add_column("Value", style="white")

    for key, value in response.headers.items():

        table.add_row(key, value)

    console.print(table)

    pause()

# =========================
# 06 ROBOTS PARSER
# =========================

def robots_parser():

    banner()

    url = input(f"{GREEN}Target URL: {WHITE}")

    target = urljoin(url, "/robots.txt")

    response = request(target)

    print()

    if response and response.status_code == 200:

        print(response.text)

    else:

        print(f"{RED}robots.txt not found.")

    pause()

# =========================
#   07 SITEMAP EXTRACTOR
# =========================

def sitemap_extractor():

    banner()

    url = input(f"{GREEN}Target URL: {WHITE}")

    target = urljoin(url, "/sitemap.xml")

    response = request(target)

    print()

    if not response:

        print(f"{RED}Failed to fetch sitemap.")

        pause()

        return

    soup = BeautifulSoup(response.text, "xml")

    urls = soup.find_all("loc")

    if not urls:

        print(f"{YELLOW}No URLs found.")

    else:

        for loc in urls:

            print(f"{GREEN}{loc.text}")

    pause()

# =========================
# 08 EMAIL HARVESTER
# =========================

def email_harvester():

    banner()

    url = input(f"{GREEN}Target URL: {WHITE}")

    response = request(url)

    print()

    if not response:

        print(f"{RED}Failed to fetch page.")

        pause()

        return

    emails = set(
        re.findall(
            r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            response.text
        )
    )

    if emails:

        for email in emails:

            print(f"{GREEN}{email}")

    else:

        print(f"{YELLOW}No emails found.")

    pause()

# =========================
# 09 SUBDOMAIN ENUMERATOR
# =========================

def subdomain_enum():

    banner()

    domain = input(f"{GREEN}Domain: {WHITE}")

    subs = [
        "www",
        "mail",
        "api",
        "admin",
        "cdn",
        "vpn",
        "dev",
        "blog"
    ]

    print()

    for sub in subs:

        host = f"{sub}.{domain}"

        try:

            ip = socket.gethostbyname(host)

            print(f"{GREEN}[FOUND]{WHITE} {host:<25} -> {ip}")

        except:
            pass

    pause()

# =========================
# 10 PORT CHECKER
# =========================

def port_checker():

    banner()

    target = input(f"{GREEN}Target IP: {WHITE}")

    ports = [
        21,
        22,
        25,
        53,
        80,
        110,
        139,
        443,
        445,
        3306,
        8080
    ]

    print()

    def check(port):

        s = socket.socket()

        s.settimeout(1)

        try:

            s.connect((target, port))

            print(f"{GREEN}[OPEN]{WHITE} Port {port}")

        except:
            pass

        s.close()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:

        executor.map(check, ports)

    pause()

# =========================
# 11 URL CRAWLER
# =========================

def url_crawler():

    banner()

    url = input(f"{GREEN}Target URL: {WHITE}")

    response = request(url)

    print()

    if not response:

        print(f"{RED}Failed to crawl target.")

        pause()

        return

    soup = BeautifulSoup(response.text, "html.parser")

    links = set()

    for tag in soup.find_all("a", href=True):

        href = urljoin(url, tag["href"])

        if href not in links:

            links.add(href)

            print(f"{GREEN}{href}")

    pause()

# =========================
# 12 SAVE REPORT
# =========================

def save_report():

    banner()

    name = input(f"{GREEN}Report Name: {WHITE}")

    os.makedirs("reports", exist_ok=True)

    path = f"reports/{name}.json"

    data = {
        "framework": "PHANTOM",
        "status": "generated"
    }

    with open(path, "w") as f:

        json.dump(data, f, indent=4)

    print(f"\n{GREEN}Report saved:{WHITE} {path}")

    pause()

# =========================
# MENU
# =========================

def menu():

    while True:

        banner()

        print(f"{CYAN}[01]{WHITE} Username Scanner          {CYAN}[07]{WHITE} Sitemap Extractor")
        print(f"{CYAN}[02]{WHITE} DNS Lookup                 {CYAN}[08]{WHITE} Email Harvester")
        print(f"{CYAN}[03]{WHITE} GeoIP Lookup               {CYAN}[09]{WHITE} Subdomain Enumerator")
        print(f"{CYAN}[04]{WHITE} Technology Detector        {CYAN}[10]{WHITE} Port Checker")
        print(f"{CYAN}[05]{WHITE} HTTP Header Analyzer       {CYAN}[11]{WHITE} URL Crawler")
        print(f"{CYAN}[06]{WHITE} Robots.txt Parser          {CYAN}[12]{WHITE} Save Report")

        print(f"\n{CYAN}[00]{WHITE} Exit")

        choice = input(f"\n{CYAN}[phantom@user]▶ {WHITE}")

        if choice in ["1", "01"]:
            username_scanner()

        elif choice in ["2", "02"]:
            dns_lookup()

        elif choice in ["3", "03"]:
            geoip_lookup()

        elif choice in ["4", "04"]:
            tech_detector()

        elif choice in ["5", "05"]:
            header_analyzer()

        elif choice in ["6", "06"]:
            robots_parser()

        elif choice in ["7", "07"]:
            sitemap_extractor()

        elif choice in ["8", "08"]:
            email_harvester()

        elif choice in ["9", "09"]:
            subdomain_enum()

        elif choice == "10":
            port_checker()

        elif choice == "11":
            url_crawler()

        elif choice == "12":
            save_report()

        elif choice in ["0", "00"]:

            clear()

            exit()

        else:

            print(f"{RED}Invalid option.")

menu()
