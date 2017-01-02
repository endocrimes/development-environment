# Development Environment

## Preqrequsites

- Terraform
- Python
- Fabric
- Packet credentials

## Usage

```bash
$ cd terraform
$ terraform apply # make a note of the server ip address
$ cd ../fabric
$ fab -H <server-ip-from-terraform>
```

