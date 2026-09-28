[简体中文](README.md) | [English](README.en.md)

# zabbix-models

A collection of Zabbix monitoring templates plus an Ansible 2.4 API wrapper, bundled with a Grafana dashboard and agent-side scripts, ready to use out of the box.

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Zabbix](https://img.shields.io/badge/Zabbix-Monitoring_Templates-D40000?style=flat&logo=zabbix&logoColor=white)](https://www.zabbix.com/)
[![Ansible](https://img.shields.io/badge/Ansible-2.4.2-EE0000?style=flat&logo=ansible&logoColor=white)](https://www.ansible.com/)

## ✨ Features

### Monitoring templates (XML, import into the Zabbix Web UI)

- **Template Linux System Base** — a base Linux monitoring template:
  - CPU: idle/interrupt/iowait/system/user time, context switches and interrupts per second, load
  - Memory & Swap: total, used amount and percentage, free swap size and percentage
  - Processes: total processes, currently running processes
  - Disk capacity (auto discovery): total size, used/free, usage percentage, free inode percentage
  - Disk I/O status: rrqm/s, wrqm/s, r/s, w/s, await, %util and other iostat metrics
  - Network interfaces: traffic in/out, packet rate, dropped/error packet statistics
  - Network: TCP connection states (established, time_wait, close_wait, listen, etc.) and socket counts
  - Others: system local time / uptime, hostname, max open files, /etc/passwd and /etc/hosts checks
- **Template Dell iDrac SNMPV2** — DELL server hardware monitoring (SNMP V2)
- **Zabbix_Template_Linux_Redis_Discovery** — Redis monitoring with low-level discovery
- **Zabbix_Template_Linux_Memcached** — Memcached monitoring
- **Percona MySQL template** (percona mysql server 2.0.9)

### Companion components

- **Grafana dashboard**: `Grafana_Template_Linux_System_Base.json`, import into Grafana to use with the base Linux template
- **Agent side**: `zabbix_agentd.d/` contains UserParameter configs plus discovery/status scripts for disk, memory, Redis and Memcached, with zabbix-agent installers for CentOS / Ubuntu
- **ansible_run**: an executor built on the Ansible 2.4.2.0 Python API
  - `AdHocRunner`: runs ad-hoc module tasks (e.g. cron, shell) from a task list
  - `CommandRunner`: runs shell/command/raw/script commands in batch
  - `PlayBookRunner`: runs a playbook and aggregates per-host results
  - `BaseInventory` / `BaseHost`: builds an inventory dynamically from dicts, with password, private key, become (sudo/su) and group support
- **golang-zabbix-robot-64**: bundled alert robot tool (Linux x64 binary)

## 🛠 Tech Stack

- Zabbix templates (XML)
- Python 3.6 + Ansible 2.4.2.0 (the `ansible_run` API wrapper)

## 🚀 Quick Start

### Import the monitoring templates

```bash
# 1. Import the XML template files in the Zabbix Web UI
# 2. Deploy configs and scripts on the agent side
cp -r zabbix_agentd.d/. /etc/zabbix/zabbix_agentd.d/
systemctl restart zabbix-agent
# 3. Import the Grafana_Template_Linux_System_Base.json dashboard into Grafana
```

### Use ansible_run

```python
from ansible_run.inventory import BaseInventory
from ansible_run.runner import AdHocRunner, CommandRunner

inventory = BaseInventory([{"hostname": "testserver", "ip": "192.168.10.100",
                            "port": 22, "username": "root", "password": "123456"}])

CommandRunner(inventory).execute('pwd', 'all')          # Run commands in batch
AdHocRunner(inventory).run(tasks, 'all')                # Run an ad-hoc task list
```

## 📁 Directory Structure

```
zabbix-models/
├── Template Linux System Base.xml            # Base Linux monitoring template
├── Template Dell iDrac SNMPV2.xml            # DELL hardware monitoring template
├── Zabbix_Template_Linux_Memcached.xml       # Memcached monitoring template
├── Zabbix_Template_Linux_Redis_Discovery.xml # Redis discovery template
├── Grafana_Template_Linux_System_Base.json   # Grafana dashboard
├── ansible_run/                              # Ansible API wrapper (with tests)
├── zabbix_agentd.d/                          # Agent-side configs, scripts and installers
└── golang-zabbix-robot-64/                   # Alert robot binary
```

## 🔗 Related Projects

- Author profile: [hequan2017](https://github.com/hequan2017)

## 📄 License

This repository does not include a LICENSE file yet; please contact the author before reuse.
