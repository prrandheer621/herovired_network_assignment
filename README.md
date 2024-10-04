Question - 1

step - 1: Created a config file in /etc/nginx/sites-available with name awesomeweb with below content.
	server {
		listen 80;
		server_name awesomeweb;

		root /var/www/awesomeweb;
		index index.html;

		location / {
			try_files $uri $uri/ =404;
		}
	}
	
step - 2: Created awesomeweb directory inside  /var/www/, and created a index.html file with custom html contents.

step - 3: Linked /etc/nginx/sites-available/awesomeweb with /etc/nginx/sites-enabled with below command
	sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/

step - 4: Restarted nginx server with sudo systemctl restart nginx/sites-available

step - 5: Checked the server with curl awesomeweb





Question - 2

step - 1: Install tabulate library using pip install tabulate

step - 2: Write a function getStatus to get status of subdomains.
	def getStatus(url):
		try:
			response = requests.get(url, timeout=5)
			if response.status_code == 200:
				return "Up"
			else:
				return "Down"
		except requests.ConnectionError:
			return "Down"
		except requests.Timeout:
			return "Timeout"

step - 3: Write a infinite loop, which will pause for 60 seconds after every run, and check for status of each subdomain available.
	def monitor_subdomains():
		while True:
			results = []
			
			#Check for each subdomain, and store the result for printing in tabular form
			for subdomain in subdomains:
				status = getStatus(subdomain)
				results.append([subdomain, status])

			
			# Priting results in tabular format in pretty Format
			print(tabulate(results, headers=["Subdomain", "Status"], tablefmt="pretty"))

			# Infinite loop paused for 60 secs, before it will run again
			time.sleep(60)

step - 4: Run the function from main.
	if __name__ == "__main__":
		monitor_subdomains()





Question - 3

step - 1: Downloaded Virtual box, Ubuntu vdi, nmap, npcap application on Windows

step - 2: Installed nginx inside the vdi, and  created the site awesomeweb and deployed on the server on port 8080.

step - 3: Windows host was unable to ping vdi, so changed vdi network setting to bridged adapter, and restarted vdi.

step - 4: Again restarted the nginx server, and ping from windows to the ip address given by 'ip addr show'/'hostname -I'

step - 5: Ping was success, and was able to load the page in browser as well, but still 'nmap 192.168.1.7' was not working.

step - 6: Using chatGPT, tried several command of nmap, only 1 worked, 'nmap -sT -Pn 192.168.1.7', which gave below output, all others were giving 0 hosts up.

	Starting Nmap 7.95 ( https://nmap.org ) at 2024-10-04 21:06 India Standard Time
	Nmap scan report for 192.168.1.7
	Host is up (0.00055s latency).
	Not shown: 998 filtered tcp ports (no-response)
	PORT     STATE SERVICE
	80/tcp   open  http
	8080/tcp open  http-proxy

	Nmap done: 1 IP address (1 host up) scanned in 5.07 seconds
	