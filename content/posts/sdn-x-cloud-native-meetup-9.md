Title: SDN x Cloud Native Meetup #9
Slug: sdn-x-cloud-native-meetup-9
Date: 2018-10-09 21:43:14
Authors: fkz
Category: Note
Tags: Meetup
Summary: Note for SDN x Cloud Native Meetup #9

link: <https://cntug.kktix.cc/events/sdn-cntug-9>

---

# Kubernetes Container Runtime Interface

Speaker: <https://github.com/chechiachang>

CRI, OCI, CRI-O


## Trend Kubernetes

- 1.3: rktnetes
- 1.5: CRI
- 1.7 removed pre-CRI Docker/rkt integration
- Currently works Kubelet to use CRI
- CRI-O: released 1.0.x to match Kubernetes 1.7


## Nomination

- CRI-O
    - OCI-based implementation of Kubernetes Container Runtime Interface
    - > 可以用它來跑 Container
- CRI
    - Kubernetes Container Runtime Interface
- OCI
    - Open Container Intiative
    - > 開源容器促進協議
    - Container 的工業化標準


## Projects with Container Runtime

docker, rkt, LXC/LXD, runC, containerd, OpenVZ, ssytemd-nspawn, machinectl, ...


## Container Runtime Interface (CRI)

- Enable Kubernetes to support more runtimes
- Free kubernetes to focus on orchestration from runtime integration
- Consists
    - a protocol buffers and gRPC API
    - libraries, additional specifications and tools
- Architect
    - dockershim
    - cri-containerd


## Protobuf

- <https://github.com/protocolbuffers/protobuf>


## CRI runtimes

- Docker CRI shim (cri-containerd)
- CoreOS rktlet
- fraktal
- Intel Clear Containers


## Open Container Initiative (OCI)

- open governmance strucgture
- container industry standards
- runtime spec
    - <https://github.com/opencontainers/runtime-spec>
    - defines configuration, execution environment, and lifecycle of a container
_ image spec
    - <https://github.com/opencontainers/image-spec>
    - spec on architecture and OS, filesystem layers and configuration


## OCI from aspect of user

- Use all OCI-conplimant container runtime
- Use all OCI-complimant images registries
- Similar UX
- <https://www.opencontainers.org/blog/2018/06/20/cri-o-how-standards-power-a-container-runtime>


## CRI-O

- <https://cri-o.io>
- OCI-based implementation of Kubernetes Container Runtime Interface
- Kubernetes incubator projet also part of the CNCF
- Dedicated for Kuberntes
- Enable CRI-O plugin to other runtimes
- Available on RHEL, Fedora, Centos, Ubuntu, ...
- 用途
    - 可以讓其他 runtime 以 plugin 的方式被使用
- ![cri-o architecutre](/files/sdn-x-cloud-native-meetup-9/cri-o.png)


## CRI-O vs Docker (containerd)

Docker: kubelet -> cri-containerd (shim) -> containerd -> runC -> container
CRI-O: kubelet -> cri-o -> runC -> container

- Lightweight
- Stability
    - built for Kubernetes
    - No cli, image utilities, ...
    - No swarm, mesosphere integration, ...


## Let's use CRI-O

- <https://github.com/kubernetes-sigs/cri-o>
- <https://github.com/kubernetes-sigs/cri-o/blob/master/tutorial.md>
- Install CRI-O
- Install Podman
    - Podman to cri-o as Docker-cli to Docker daemon
    - `sudo podman run --name my-golang golang:alpine bash`
    - > Docker 使用者無痛轉移


## References

- <https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/>

---

# Automatically Renew Your Certificate In Kubernetes

Speaker: <https://github.com/hwchiu>

<https://www.hwchiu.com/cert-manager.html>
<https://github.com/jetstack/cert-manager>
<https://cert-manager.readthedocs.io/en/latest/>


## Why we need cert-manager

- 簡化申請 Let's Encrypt 的步驟
- 憑證到期自動 renew


## What is cert-manager

- A Native Kubernetes certificate management controller.
- It can help with issuing certificates from a variety of sources, such as Let's Encrypt, HashiCorp Vault.
- It will ensure certificates are valid and up to date, and attempt to renew certificates.

### Components of cert-manager

- Issuers
- cert-manager
- Certificates
- Kuberntes Secrets

cert-manager 透過 [Kubernetes 的 CustomResourceDefinitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions) 新增了 `clusterissuers`, `issuers`, `certificate`


#### Issuers

<http://docs.cert-manager.io/en/latest/reference/issuers.html>

- ACME
    - [HTTP01](http://docs.cert-manager.io/en/latest/reference/issuers/acme/http01.html)
    - [DNS01](http://docs.cert-manager.io/en/latest/reference/issuers/acme/dns01.html)
        - Provision a TXT resource record containing a designated vaule for a specific validation domain name.
        - Requirement an approach to control the DNS provider
        - For example: If I want to verify `test.hwchiu.com`
            - I need to create a TXT record in `test.hwchiu.com` with specific content.
            - Let's Encrypt will query the TXT record of `test.hwchiu.com` to check it's content.
- CA
- Vault
- Self-signed


## How to use cert-manager

- Install the cert-manager
    - Deployment
    - Service Account
    - RBAC (if you enable it in your cluster)
- Create a Issuer/ClusterIssuer


### Install

- Use `helm` to install cert-manager

### ClusterIssuers

- In order to simpilify the configuration.
- Support
    - Google Cloud DNS
    - Amazon Route53
    - Cloudflare
    - Akamai FastDNS
    - RFC2136
    - ACME-DNS
- For the Cloudflare
    - you can get your API key from the control panel
    - We need to create a kubernetes secret resource with that API key.

---

# Lightning Talk

## Container Platform Information

Speaker: <https://github.com/pichuang>

- Podman
    - <https://www.projectatomic.io/blog/2018/02/reintroduction-podman/>
    - <https://github.com/containers/libpod>
- cri-o
    - <https://cri-o>
- buildah
    - <https://github.com/containers/buildah>
- Skopeo
    - <https://github.com/containers/skopeo>
- Istio
    - <https://istio.io/>
    - <https://github.com/istio/istio>
- CoreOS (Acquired by Red Hat)
    - Container OS
        - CoreOS
    - Container Platform
        - OpenShift
        - <https://www.okd.io/>
        - OpenShift is Kubernetes for the enterprise
    - Operation & Management
        - TECTONIC
