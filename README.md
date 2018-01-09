# holepunch
Python library to generate ACL and firewall rules for network devices.  
This project is in the early stages so I cannot guarantee it will not have breaking changes.

Note: This project is tested with python3.6+ other versions of python are not supported, but may work.

## Project Goals
- Create service/object groups based on YAML input
- Create vendor specific ACL's based on YAML input
- Pre-defined services for common rules such as ms-ad 
- Initial support for Cisco/Arista/Juniper
- Potential future support for iptables/firewalld

## Example Input Data

```yaml
description: "microsoft-ad"
protocols:
  tcp:
    - port: 25 
      description: "SMTP"
    - port: 53 
      description: "DNS"
    - port: 88
      description: "Kerberos"
    - port: 135
      description: "RPC, EPM"
    - port: 139
      description: "DFSN, NetBIOS Session Service, NetLogon"
    - port: 389
      description: "LDAP"
    - port: 445
      description: "SMB,CIFS,SMB2, DFSN, LSARPC, NbtSS, NetLogonR, SamR, SrvSvc"
    - port: 464
      description: "Kerberos change/set password"
    - port: 636
      description: "LDAPS"
    - port: 3268
      description: "LDAP GC"
    - port: 3269
      description: "LDAP GC SSL"
    - port: 5722
      description: "RPC, DFSR (SYSVOL)"
    - port: 9389
      description: "SOAP"
    - port_range: 
        start: 1024
        end: 5000
      description: "Windows Server 2003 dynamic port range"
    - port_range: 
        start: 49152
        end: 65535
      description: "Windows Server 2008 (and Windows Vista) dynamic port range"
  
  udp:
    - port: 53 
      description: "DNS"
    - port: 67 
      description: "DHCP"
    - port: 88 
      description: "Kerberos"
    - port: 123 
      description: "NTP"
    - port: 137 
      description: "NetLogon, NetBIOS Name Resolution"
    - port: 138 
      description: "DFSN, NetLogon, NetBIOS Datagram Service"
    - port: 389 
      description: "LDAP"
    - port: 445 
      description: "SMB,CIFS,SMB2, DFSN, LSARPC, NbtSS, NetLogonR, SamR, SrvSvc"
    - port: 464 
      description: "Kerberos change/set password"
    - port: 2535 
      description: "MADCAP"
    - port_range:
        start: 1024
        end: 5000
      description: "Windows Server 2003 dynamic port range"
    - port_range:
        start: 49152
        end: 65535
      description: "Windows Server 2008 (and Windows Vista) dynamic port range"
```

## Example Template Rendering

```python
import yaml

from utils.loaders import render_from_template

with open('services/microsoft-ad.yml', 'r') as f:                        
    data = yaml.load(f)

# Juniper SRX
print(render_from_template('templates/juniper/srx/', 'application.j2', **data))

applications {
    application tcp-25 {
        protocol tcp;
        destination-port 25;
    }
    application tcp-53 {
        protocol tcp;
        destination-port 53;
    }
    application tcp-88 {
        protocol tcp;
        destination-port 88;
    }
.
.
.
    application udp-49152-65535 {
        protocol udp;
        destination-port 49152-65535;
    }
}

# Cisco ASA
print(render_from_template('templates/cisco/asa/', 'service.j2', **data))

object service tcp-25
 service tcp destination eq 25
object service tcp-53
 service tcp destination eq 53
object service tcp-88
 service udp destination eq 88
.
.
.
object service udp-49152-65535
 service udp destination range 49152 65535
```

