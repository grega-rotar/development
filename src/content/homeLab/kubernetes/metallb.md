---
title: "MetalLB in kubernetes cluster"
summary: "How to setup a MetalLB in kubernetes cluster to allow EXTERNAL-IP to work"
date: "May 13 2024"
draft: false
tags:
- k8s
- kubernetes
- MetalLB
- setup
demoUrl: "https://metallb.io/configuration/_advanced_ipaddresspool_configuration/"
authors:
- Grega Rotar
---
## Preparation
If you’re using kube-proxy in IPVS mode, since Kubernetes v1.14.2 you have to enable strict ARP mode.

*Note, you don’t need this if you’re using kube-router as service-proxy because it is enabling strict ARP by default.*

You can achieve this by editing kube-proxy config in current cluster:
```sh
kubectl edit configmap -n kube-system kube-proxy
```
You can also add this configuration snippet to your kubeadm-config, just append it with --- after the main configuration.

If you are trying to automate this change, these shell snippets may help you:
```sh
# see what changes would be made, returns nonzero returncode if different
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl diff -f - -n kube-system

# actually apply the changes, returns nonzero returncode on errors only
kubectl get configmap kube-proxy -n kube-system -o yaml | \
sed -e "s/strictARP: false/strictARP: true/" | \
kubectl apply -f - -n kube-system
```

## Instalation By Manifest
To install MetalLB, apply the manifest:
```sh
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.5/config/manifests/metallb-native.yaml
```
Go to https://metallb.universe.tf/installation/ to find **latest verison**.

There are other installation options available, which are also found on upper link.
## IPAddressPool
With applying this **.yml** file you create pool for external ip addresses.

```yml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
    #  - 192.168.1.203-192.168.1.208
    - 10.30.0.0/16

---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: example
  namespace: metallb-system
```

Find out more at: https://metallb.io/configuration/_advanced_ipaddresspool_configuration/


Best regards,   
Grega Rotar
