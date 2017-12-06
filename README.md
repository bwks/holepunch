# holepunch
Python library to generate ACL and firewall rules for network devices.  
This project is in the early stages so I cannot guarantee it will not have breaking changes.

## Project Goals
- Create service/object groups based on YAML input
- Create vendor specific ACL's based on YAML input
- Pre-defined services for common rules such as ms-ad 
- Initial support for Cisco/Arista/Juniper
- Potential future support for iptables/firewalld

## Example Input Data

```yaml
protocols:
  tcp:
    - port: 25 
      description: "SMTP"
    - port: 53 
      description: "DNS"
    - port: 88
      description: "Kerberos"
```

## Example Template Rendering

```python
import yaml

from utils.loaders import render_from_template

with open('services/microsoft-ad.yml', 'r') as f:                        
    data = yaml.load(f)

print(render_from_template('templates/juniper/srx/', 'service.j2', **data))

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
}

print(render_from_template('templates/cisco/asa/', 'service.j2', **data))

object service tcp-25
 service tcp destination eq 25
object service tcp-53
 service tcp destination eq 53
object service tcp-88
.
.
.
```

