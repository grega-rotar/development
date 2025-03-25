---
title: "VM network information"
summary: ""
date: "May 25 2024"
draft: false
tags:
- documentation
# repoUrl: "https://gitlab.etiam.si/grega.rotar/roleta"
authors:
- Grega Rotar
---
## List of VMs and theirs IPV4 addresses
# Virtual Machines Documentation

# Virtual Machines Documentation

## Ubuntu
| Hostname                 | IP Address     | OS Version     |
|--------------------------|----------------|----------------|
| dns1.local.etiam.si     | 192.168.1.190  | Ubuntu 20.04.3 LTS |
| proxy.local.etiam.si    | 192.168.1.180  | Ubuntu 20.04.3 LTS |
| master_dev.local.etiam.si | 192.168.1.170 | Ubuntu 20.04.3 LTS |
| db.local.etiam.si       | 192.168.1.250  | Ubuntu 20.04.3 LTS |
| gitlab.local.etiam.si   | 192.168.1.230  | Ubuntu 20.04.3 LTS |
| broker.local.etiam.si   | 192.168.1.211  | Ubuntu 20.04.3 LTS |
| monitor.local.etiam.si  | 192.168.1.212  | Ubuntu 20.04.3 LTS |
| cdn                      | -              | -              |

**Purpose:**
- dns1: DNS server
- proxy: Proxy server
- master_dev: Development server
- db: Database server
- gitlab: GitLab server
- broker: Broker server
- monitor: Monitoring server
- cdn: Content Delivery Network

## Fedora
| Hostname                     | IP Address     | OS Version     |
|------------------------------|----------------|----------------|
| master.k8s.local.etiam.si   | 192.168.1.240  | Fedora 39      |
| master2.k8s.local.etiam.si  | 192.168.1.239  | Fedora 39      |
| master3.k8s.local.etiam.si  | 192.168.1.238  | Fedora 39      |
| w1.k8s.local.etiam.si       | 192.168.1.241  | Fedora 39      |
| w2.k8s.local.etiam.si       | 192.168.1.242  | Fedora 39      |
| nfs.local.etiam.si          | 192.168.1.215  | Fedora 39      |

**Purpose:**
- master.k8s, master2.k8s, master3.k8s: Kubernetes master nodes
- w1.k8s, w2.k8s: Kubernetes worker nodes
- nfs: NFS server

## Fedora Workstation
| IP Address     | OS Version     |
|----------------|----------------|
| 192.168.1.80   | Fedora Workstation (version not specified) |

**Purpose:**
- Workstation for general use

## Debian
| Hostname                  | IP Address     | OS Version     |
|---------------------------|----------------|----------------|
| haproxy.local.etiam.si   | 192.168.1.200  | Debian (version not specified) |

**Purpose:**
- HAProxy server

