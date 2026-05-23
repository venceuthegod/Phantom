#!/data/data/com.termux/files/usr/bin/bash

clear

echo "
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
"

echo "[+] Installing PHANTOM..."

pkg update -y
pkg upgrade -y

echo "[+] Installing system packages..."

pkg install python -y
pkg install python-pip -y
pkg install git -y
pkg install clang -y
pkg install libxml2 -y
pkg install libxslt -y

echo "[+] Upgrading pip..."

python -m pip install --upgrade pip

echo "[+] Installing Python requirements..."

pip install -r requirements.txt

chmod +x *.sh

mkdir reports

echo ""
echo "[✓] Installation completed successfully."
echo ""
echo "Start PHANTOM with:"
echo "python phantom.py"
echo ""
