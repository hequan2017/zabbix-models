[简体中文](README.md) | [English](README.en.md)

# zabbix-models

Zabbix 监控模板合集 + Ansible 2.4 API 调用封装，附带 Grafana 面板与 Agent 端脚本，开箱即用。

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Zabbix](https://img.shields.io/badge/Zabbix-监控模板-D40000?style=flat&logo=zabbix&logoColor=white)](https://www.zabbix.com/)
[![Ansible](https://img.shields.io/badge/Ansible-2.4.2-EE0000?style=flat&logo=ansible&logoColor=white)](https://www.ansible.com/)

## ✨ 功能特性

### 监控模板（XML，导入 Zabbix Web 即可使用）

- **Template Linux System Base** —— Linux 基础监控模板：
  - CPU：空闲/中断/iowait/系统/用户时间、每秒上下文切换与中断次数、负载
  - 内存 & Swap：总量、已用量与百分比、Swap 空闲大小与百分比
  - 进程：进程总数、正在运行的进程数
  - 磁盘容量（自动发现）：总大小、已用/未用、使用百分比、空闲 Inode 百分比
  - 磁盘 IO 状态：rrqm/s、wrqm/s、r/s、w/s、await、%util 等 iostat 指标
  - 网卡：进出流量、包速率、丢包与错误统计
  - 网络：TCP 连接状态（established、time_wait、close_wait、listen 等）与 Socket 数量
  - 其他：系统本地时间/启动时间、主机名、最大打开文件数、/etc/passwd 与 /etc/hosts 检测
- **Template Dell iDrac SNMPV2** —— DELL 服务器硬件监控（SNMP V2）
- **Zabbix_Template_Linux_Redis_Discovery** —— Redis 自动发现监控
- **Zabbix_Template_Linux_Memcached** —— Memcached 监控
- **Percona MySQL 模板**（percona mysql server 2.0.9）

### 配套组件

- **Grafana 面板**：`Grafana_Template_Linux_System_Base.json`，配合 Linux 基础模板直接导入 Grafana 使用
- **Agent 端**：`zabbix_agentd.d/` 内含 UserParameter 配置与磁盘/内存/Redis/Memcached 的发现、取值脚本，并附 CentOS / Ubuntu 的 zabbix-agent 安装包
- **ansible_run**：基于 Ansible 2.4.2.0 Python API 封装的执行器
  - `AdHocRunner`：以任务列表方式执行 ad-hoc 模块（如 cron、shell）
  - `CommandRunner`：批量执行 shell/command/raw/script 命令
  - `PlayBookRunner`：执行 Playbook 并汇总各主机执行结果
  - `BaseInventory` / `BaseHost`：用字典动态构建 Inventory，支持密码、私钥、become（sudo/su）与分组
- **golang-zabbix-robot-64**：内置的告警机器人工具（Linux x64 二进制）

## 🛠 技术栈

- Zabbix 模板（XML）
- Python 3.6 + Ansible 2.4.2.0（`ansible_run` API 封装）

## 🚀 快速开始

### 导入监控模板

```bash
# 1. 在 Zabbix Web 界面导入 XML 模板文件
# 2. Agent 端部署配置与脚本
cp -r zabbix_agentd.d/. /etc/zabbix/zabbix_agentd.d/
systemctl restart zabbix-agent
# 3. 在 Grafana 中导入 Grafana_Template_Linux_System_Base.json 面板
```

### 使用 ansible_run

```python
from ansible_run.inventory import BaseInventory
from ansible_run.runner import AdHocRunner, CommandRunner

inventory = BaseInventory([{"hostname": "testserver", "ip": "192.168.10.100",
                            "port": 22, "username": "root", "password": "123456"}])

CommandRunner(inventory).execute('pwd', 'all')          # 批量执行命令
AdHocRunner(inventory).run(tasks, 'all')                # 执行 ad-hoc 任务列表
```

## 📁 目录结构

```
zabbix-models/
├── Template Linux System Base.xml            # Linux 基础监控模板
├── Template Dell iDrac SNMPV2.xml            # DELL 硬件监控模板
├── Zabbix_Template_Linux_Memcached.xml       # Memcached 监控模板
├── Zabbix_Template_Linux_Redis_Discovery.xml # Redis 自动发现模板
├── Grafana_Template_Linux_System_Base.json   # Grafana 面板
├── ansible_run/                              # Ansible API 封装（含测试脚本）
├── zabbix_agentd.d/                          # Agent 端配置、脚本与安装包
└── golang-zabbix-robot-64/                   # 告警机器人二进制
```

## 🔗 相关项目

- 作者主页：[hequan2017](https://github.com/hequan2017)

## 📄 License

仓库暂未包含 LICENSE 文件，如需使用请联系作者。
