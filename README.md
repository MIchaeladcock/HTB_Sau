# Sau

## Introduction

After completing the Hack The Box challenge (HTB) 'Sau,' I found the web exploitation path to be somewhat cumbersome. The task involved leveraging a Server-Side Request Forgery (SSRF) vulnerability to facilitate remote code execution, which made the exploitation process finicky. Syntax errors were easily introduced due to the need for pseudo-proxying. To streamline this process, I developed an automated Python script coupled with a Bash reverse shell payload. This tool significantly simplifies the exploitation workflow, enhancing efficiency and reducing the likelihood of errors

# Instruction 

1. Start the Hack The Box (HTB) machine 'Sau' by visiting Hack The Box - Sau and note down the machine's IP address.
2. Download the files "sau_main.py" and "rev.sh" from the repository and place them in the same directory.
3. Ensure you are connected to the HTB VPN and record your local machine's tun0 IP address.
4. Edit the "rev.sh" file to replace the placeholder IP address with your tun0 IP address, then save the changes.
4. In the directory containing "sau_main.py" and "rev.sh," open a terminal and start a Python web server listening on port 80 with the command: ```python3 -m http.server 80```. Keep this terminal open.
5. Open a new terminal or terminal pane and initiate a Netcat listener on port 9009 using the command: ```nc -nvlp 9009```. Do not close this terminal.
6. In a separate terminal or a new pane, make "sau_main.py" executable by running ```chmod +x sau_main.py```, then execute the script by following the on-screen prompts. You will be asked to enter the HTB machine's IP address and your local tun0 IP.
7. Enjoy your shell :)



