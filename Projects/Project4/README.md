## Setup Load Balancing TODOs

1. Create a `.ssh/config` file on each system that correlates hostnames to private IPs of systems within the subnet (your instances).
    - Description of how file is configured
        ````
        Host serv1
            HostName 10.0.1.10
            User ubuntu
            IdentityFile ./nameOfPrivateKey.pem
        Host serv2
            HostName 10.0.1.11
            User ubuntu
            IdentityFile ./nameOfPrivateKey.pem
        ````
2. How to SSH in between the systems utilizing their private IPs.
    - Apache server instances that have private IP's can be ssh'd into by first sshing into the proxy server instance that has a public IP address
    - First, you need to put your private key on the instance with the public IP, because to access the instances with private IP's you still need to have your private key. To do this use the following command:
        - `scp -i privatekey.pem privatekey.pem ubuntu@elasticIPAddress:/home/ubuntu`
        - This will use the secure copy protocol to copy your private key to the instance
    - Next, you need to ssh into the instance you just copied the private key to
    - Lastly, to ssh into the instances with the private IP addresses all you have to do is use the ssh command as you normally would using the private key you just copied and the private IP of the instance you want to ssh into
3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
        - `/etc/haproxy/haproxy.cfg`
     - What configuration(s) were set (if any)
     - How to restart the service after a configuration change
        - `systemctl restart servicename`
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
     - What configuration(s) were set (if any)
     - Where site content files were located (and why)
     - How to restart the service after a configuration change
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
6. (Optional) - link to your proxy so I can click it.
