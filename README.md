# SimpleScapyTool

## Definition:

- In this project, we write a set of Scapy functions which are stored in a Phyton script.
- We design a Graphical User Interface(GUI) for the sake of user.GUI has 5 buttons and a label which displays results.

## Outcomes:

- Saving the results to a file.
- Finding a new result which is bounded to recorded results.
- Learning how to use Python programming language.
- Learning how to use Scapy

## Graphical User Interface(GUI):

- ICMP Button:This button calls icmp( ) function .Then prints the results from text file.
- Port Button:This button calls port( ) function.Then prints the results from text file.
- Router Button:This button calls routers( ) function.Then prints the results from text file
- Web Button:This button calls web( ) funtion.Then prints the results from text file.
- SNMP Button:This button calls snmp( ) function.Then prints the results from text file.
![sst](https://cloud.githubusercontent.com/assets/12773964/23141077/0fb58b54-f7c6-11e6-8ba8-41be966028a0.jpg)

### ICMP Ping:
- The Internet Control Message Protocol is one of the main protocols of the Internet Protocol Suite.It is used by network devices,like routers,to send error messages indicating.

- In this part our aim is to send ping to the IP addresses in specific ranges.We also collected these IP Adresses and we have detected that which of them are open.

#### Outcomes:
- Determine the IP Adresses
- Check if the IP Adress is open or not
- Printing these IP Adresses to a file.

#### Wireshark Output:
![2](https://cloud.githubusercontent.com/assets/12773964/23141120/41b92be2-f7c6-11e6-8bf9-f719d9bfe459.jpg)

#### Command Line Output:
![3](https://cloud.githubusercontent.com/assets/12773964/23141132/5513689c-f7c6-11e6-8c19-f0998e157399.jpg)

#### Comment:
- If the IP adress gives a response to our packet ,it means that the IP adress is online.If it does not give a response, it means that the IP adress is offline.

### Port Identification – Open Ports
- The program read source addresses from the file ,namely , icmp.txt.Then scan all addresses individually.After the scan ,we found the port numbers which are open and write these port numbers with their services names to a text file.

#### Outcomes:
- Reading recorded result from previous task .
- Scaning the ports one by one.
- Learning how to find a port which is open.
- Printing their addresses,ports and service names to a text file.

#### Wireshark Output:
![4](https://cloud.githubusercontent.com/assets/12773964/23141145/6a2c1b16-f7c6-11e6-8b40-065cffb6d7d0.jpg)

#### Command Line Output:
![5](https://cloud.githubusercontent.com/assets/12773964/23141147/6ad9b776-f7c6-11e6-9a02-ffd16bb8a0c7.jpg)

#### Comment:
![6](https://cloud.githubusercontent.com/assets/12773964/23141182/9fa864d4-f7c6-11e6-8c6c-90543b510865.jpg)

- IP addresses which seen at above are shows the ports which are currently open.

### Router & Firewall Detection
- We made a hostname scan.After the scan we list router and firewall addresses which are between the hostname we want and the computer.After that the IP addresses are pushed to a port scaning and the results are saved to a text file.

#### Outcomes:
- Learning how to make Router & Firewall scan.

#### Wireshark Output:
![7](https://cloud.githubusercontent.com/assets/12773964/23141318/45df9bf6-f7c7-11e6-9879-61528ffd4109.jpg)

#### Command Line Output:
![8](https://cloud.githubusercontent.com/assets/12773964/23141317/45ddff9e-f7c7-11e6-8acc-21c80fcceb56.jpg)

#### Comment:
- We have made a router and firewall detection scan and we found that the IP adresses which shown above are adresses of routers and firewalls that are between our machine and the destiniton host.

### Web Server Detection:
- Protocols and ports of 10 web server addresses are analyzed.The resulst are saved to a text file.

#### Outcomes:
- Learning how to scan protocols and ports of the Web Server addresses.

#### Wireshark Output:
![9](https://cloud.githubusercontent.com/assets/12773964/23141366/9318cc4e-f7c7-11e6-9018-9832138d0998.jpg)
![10](https://cloud.githubusercontent.com/assets/12773964/23141365/93140646-f7c7-11e6-909f-af8b58b3db22.jpg)

#### Command Line Output:
![11](https://cloud.githubusercontent.com/assets/12773964/23141368/931e0ccc-f7c7-11e6-9ad8-5281ebbbf401.jpg)

#### Comment:
![12](https://cloud.githubusercontent.com/assets/12773964/23141367/931b9d20-f7c7-11e6-866c-2404996e3b70.jpg)

- The results which shown above are the results of IP adresses of our hostnames and their port types.

### SNMP Detection:

- Snmp function sends request to snmp port using UDP and receives answers from UDP port 161.Because of that it detects which port is open at which IP adress.

#### Outcomes:
- Scanning and finding hosts adresses having SNMP and ports of each host.

#### Wireshark Output:
![13](https://cloud.githubusercontent.com/assets/12773964/23141523/464cccfc-f7c8-11e6-829c-84bb759f4b59.jpg)

#### Command Line Output:
![14](https://cloud.githubusercontent.com/assets/12773964/23141524/464e33da-f7c8-11e6-9b6c-d63d17ddf381.jpg)

#### Comment:
![15](https://cloud.githubusercontent.com/assets/12773964/23141525/464e3286-f7c8-11e6-8a73-0d3820df7c2c.jpg)
- As we can see ,in our Wireshark output, IP adresses which ends with 30,31,32 are closed.We can see it in our function output too.

