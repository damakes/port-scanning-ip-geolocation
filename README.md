# Network Mapper project with geographic maps

After completing the [Nmap](https://nmap.org/) scanning course at Metropolia UAS, I became interested in automating the port scanning process. I decided to experiment with Python and Nmap to create a Port Scanner. I've created a [script](scan_now.py) that displays the status of the target, whether it is up or down. Then probes a range of network ports on a target system, determining which ports are open and which are closed. 
 
<img src="docs\image-6.png" alt="isolated" height="330"/>

 The open ports indicate services or applications that are actively listening on the target system. Shows the operating system details, if available. Shows the network route details, if available. Displays the results of the scan in color-coded output. - [PortScanner.md](docs/PortScanner.md)

Building on this, I thought it would be interesting to visualize the geographical location of the target on a map.
I found a data provider, that offers reliable and scalable IP data solutions. 

<img src="docs\image-5.png" alt="isolated" height="330"/>

I utilized the [ipinfo.io API](https://ipinfo.io/) to obtain the geographical coordinates of the target IP address. I then used the [Folium library](https://github.com/python-visualization/folium) to create interactive maps. The map is saved as an HTML file, which can be opened in a web browser to view the location. - [IP_Geolocation.md](docs/IP_Geolocation.md) / Github pages: [MyMaps](https://damakes.github.io/port-scanning-ip-geolocation/)


#### [REFERENCES](docs/References.md)"# port-scanning-ip-geolocation" 
