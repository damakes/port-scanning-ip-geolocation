import nmap
import pyfiglet
from modules.text_colors import TextColors

def scan(target):
  nm = nmap.PortScanner()
  try:
    nm.scan(target, arguments='-O -sV -sC --traceroute')
    return nm
  except Exception as e:
    print(f"An error occurred during scanning: {e}")
    return None

def status(nm, host):
  state = nm[host].state()
  up = "up" if state == "up" else ""
  down = "down" if state == "down" else ""

  print(f"Target is {TextColors.green}{up}{TextColors.end}{TextColors.red}{down}{TextColors.end}")

  print(f"{TextColors.cyan}-{TextColors.end}"*50)
  print(f"{TextColors.Background_Bright_Magenta}Scanning Target: {host} {nm[host].hostname()}{TextColors.end}")
  print(f"{TextColors.cyan}-{TextColors.end}"*50)

def protocol(nm, host):
  for proto in nm[host].all_protocols():
    print(f"\n{TextColors.magenta}Protocol{TextColors.end} ({TextColors.cyan}{proto}{TextColors.end})")
    port_info = nm[host][proto]
    sorted_ports = sorted(port_info.keys())
    for port in sorted_ports:
        print(f"[{TextColors.cyan}*{TextColors.end}] Port {port} {TextColors.cyan}|{TextColors.end} {port_info[port]['state']} {TextColors.cyan}|{TextColors.end} Service: {port_info[port]['name']} {TextColors.cyan}|{TextColors.end}")

def os(nm, host):
  if 'osmatch' in nm[host]:
        print(f"\n{TextColors.magenta}OS Matches:{TextColors.end}")
        for osmatch in nm[host]['osmatch']:
            print(f"[{TextColors.cyan}*{TextColors.end}] Name: {osmatch['name']} {TextColors.cyan}|{TextColors.end} Accuracy: {osmatch['accuracy']}% {TextColors.cyan}|{TextColors.end}")
            if 'osclass' in osmatch:
                for osclass in osmatch['osclass']:
                    print(f"   {TextColors.cyan}•{TextColors.end} Type: {osclass['type']} {TextColors.cyan}|{TextColors.end} Vendor: {osclass['vendor']} {TextColors.cyan}|{TextColors.end} OS Family: {osclass['osfamily']} {TextColors.cyan}|{TextColors.end} OS Generation: {osclass['osgen']} {TextColors.cyan}|{TextColors.end}")

def host_scripts(nm, host):
  if 'hostscript' in nm[host]:
      print(f"\n{TextColors.magenta}Host Script Results:{TextColors.end}")
      for script in nm[host]['hostscript']:
          print(f"[{TextColors.cyan}*{TextColors.end}] Script ID: {script['id']} \n{TextColors.cyan}Output{TextColors.end}: {script['output']}")

def traceroute(nm, host):
  if 'traceroute' in nm[host]:
    print(f"\n{TextColors.magenta}Traceroute:{TextColors.end}")
    for hop in nm[host]['traceroute']['hop']:
        print(f"[{TextColors.cyan}*{TextColors.end}] Hop: {hop['ttl']} {TextColors.cyan}|{TextColors.end} Address: {hop['ipaddr']}")

def info():
  ascii_banner = pyfiglet.figlet_format('ScAn NoW')
  print(f'{TextColors.cyan}{ascii_banner}{TextColors.end}')
  print(f"{TextColors.Background_Bright_Yellow}Command: -O -sV -sC --traceroute {TextColors.end}")
  print(f"{TextColors.yellow}• OS Detection (-O): Attempts to identify the operating system of the target host(s).{TextColors.end}")
  print(f"{TextColors.yellow}• Version Detection (-sV): Determines the versions of the services running on open ports.{TextColors.end}")
  print(f"{TextColors.yellow}• Default Scripts (-sC): Runs Nmap’s default set of scripts against the target. Equivalent to --script=default SCRIPT SCAN.{TextColors.end}")
  print(f"{TextColors.yellow}• Trace path to host (--traceroute): Traces the network route to the target{TextColors.end}")
  print(f"{TextColors.Background_Bright_Yellow}Enter IPv4 <X.X.X.X> address or Domain name <scanme.nmap.org>.{TextColors.end}\n")

def main():
  info()
  target = input(f'{TextColors.magenta}ScAn NoW: {TextColors.end}').strip()

  nm = scan(target)
  for host in nm.all_hosts():
    status(nm, host)
    protocol(nm, host)
    os(nm, host)
    host_scripts(nm, host)
    traceroute(nm, host)


if __name__ == "__main__":
  main()
