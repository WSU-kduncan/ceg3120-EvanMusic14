# Project 3

1. Mappings: 
    - AMI
        - Ubuntu Server 22.04 AMI ID: ami-08c40ec9ead489470

2. Resources 
    - /24 VPC Range: 10.0.0.0/24
    - /28 Subnet Range: 10.0.0.0/28
    - Key: Name
        - Value: NameHere

3. Security Group Settings:
    - SSH from WSU:
        - IpProtocol: tcp
            -  FromPort: '22'
            -  ToPort: '22'
            -  CidrIp: 130.108.0.0/16
    - Instannces within the VPC or subnet
        - IpProtocol: tcp
            -  FromPort: '22'
            -  ToPort: '22'
            -  CidrIp: 10.0.0.0/24
4. Instance settings:
    - Private IP in subnet range: 10.0.0.4
    - Change hostname
    - Install `git`, `python3`, `pip3`
        - apt-get install -y \\ \
              git \\ \
              python3 \\ \
              python3-pip && \\ \
            hostnamectl set-hostname MUSIC-UBUNTU
