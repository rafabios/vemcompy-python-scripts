# Instalando o k3s

### Master: 192.168.1.40

### Worker: 192.168.1.30


## Master

### Instalando no master
```
export K3S_KUBECONFIG_MODE="644"
export INSTALL_K3S_EXEC=" --no-deploy servicelb --no-deploy traefik"
```
#### Rodando o k3s
```
curl -sfL https://get.k3s.io | sh -
```
#### Status
```
sudo systemctl status k3s
```

### Baixando o Kubectl
```
https://kubernetes.io/docs/tasks/tools/install-kubectl/
```
#### Ver o node:
```
kubectl get nodes -o wide
```
#### Ver servicos deployados:
```
kubectl get pods -A -o wide
```
#### pegar o token no master:
```
cat /var/lib/rancher/k3s/server/node-token
```



# Worker



#### Instalar o k3s no worker (slave)

#### Setando as variaveis

```
export K3S_KUBECONFIG_MODE="644"
export K3S_URL="https://192.168.1.30:6443"  # Alterar para seu IP do master #
export K3S_TOKEN="K106edce2ad174510a840ff7e49680fc556f8830173773a1ec1a5dc779a83d4e35b::server:5a9b70a1f5bc02a7cf775f97fa912345"
```

#### instalando o agente:
```
curl -sfL https://get.k3s.io | sh -
```

#### Verificar o status
```
systemctl status k3s-agent
```




# Opcional #
#### Copiando o kube config para sua maquina:

```
scp vemcompy@192.168.1.30:/etc/rancher/k3s/k3s.yaml ~/.kube/config

sed -i '' 's/127\.0\.0\.1/192\.168\.1\.30/g' ~/.kube/config
```



# Validando o cluster (master)
```
kubectl get nodes -o wide
```



# Instalando o Helm (Master)
#### Para versoes mais novas: https://github.com/helm/helm/releases
```
wget https://get.helm.sh/helm-v3.3.4-linux-amd64.tar.gz
```
#### Descompactando e movendo
```
tar -zxvf helm-v3.3.4-linux-amd64.tar.gz
mv linux-amd64/helm /usr/local/bin/helm
```

### Checando o helm:
```
helm version
```
### Adicionando repositorios:
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com
```



# CREDITOS E REFERENCIAS:


https://kauri.io/38-install-and-configure-a-kubernetes-cluster-with/418b3bc1e0544fbc955a4bbba6fff8a9/a





