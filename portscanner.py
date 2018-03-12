import socket,sys,time,datetime,argparse,os
from sys import argv

os.system('clear')
 
xyz,host = argv
ip = socket.gethostbyname(host)
print(ip)

open_ports = []

common_ports = {
 
	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'389': 'LDAP',
	'443': 'HTTPS',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'2082': 'CPANEL',
	'2083': 'CPANEL',
	'3306': 'MYSQL',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}
 
starting_time = time.time()
print ("+" * 40)
print ("\tSimple Port Scanner..!!!")
print ("+" * 40)
 

print ("Scanning for most common ports on %s" % (host))
print ("Scanning started at %s" %(time.strftime("%I:%M:%S %p")))

def check_port(host, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((host, port))	
		if r == 0:
			result = r 
		sock.close()
	except (Exception, e):
		pass
 
	return result

def get_service(port):
	port = str(port)
	if port in common_ports:
		return common_ports[port]
	else:
		return 0
 
 
try:
	print ("Scan in progress..")
	print ("Connecting to Ports ")
 
	
	for p in common_ports:
		sys.stdout.flush()
		p = int(p)
		response = check_port(host, p)
		if response == 0:
			open_ports.append(p)
			sys.stdout.write('\b' * len(str(p)))
	
	print ("\nScanning completed at %s" %(time.strftime("%I:%M:%S %p")))
	ending_time = time.time()
	total_time = ending_time - starting_time
	print ("=" * 40)
	print ("\tScan Report: %s" %(host))
	print ("=" * 40)
	if total_time <= 60:
		total_time = str(round(total_time, 2))
		print ("Scan Took %s seconds" %(total_time))
	else:
		total_time = total_time / 60
		print ("Scan Took %s Minutes" %(total_time))
		
	if open_ports:
		print ("Open Ports: ")
		for i in sorted(open_ports):
			service = get_service(i)
			if not service:
				service = "Unknown service"
			print ("\t%s %s: Open" % (i, service))
	else:
		print ("Sorry, No open ports found.!!")
 
except KeyboardInterrupt:
	print ("You pressed Ctrl+C. Exiting ")
	sys.exit(1)
