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
```

## Example Template Rendering

### Cisco ASA Service
```
object service tcp-25
 service tcp destination eq 25
  
object service tcp-53
 service tcp destination eq 53
  
object service tcp-88
 service tcp destination eq 88
  
object service tcp-135
 service tcp destination eq 135
  
object service tcp-139
 service tcp destination eq 139
```

### Junpier SRX Application
```
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
    application tcp-135 {
        protocol tcp;
        destination-port 135;
    }
    application tcp-139 {
        protocol tcp;
        destination-port 139;
    }
}
```
