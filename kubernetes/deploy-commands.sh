# Cria o alias para o kubectl
alias k=kubectl

# Deploy do objetos no cluster
k create -f deployment.yaml
k create -f service.yaml


# Listar os pods
k get pods

# Listar deployments
k get deployment

# Listar servicos
k get svc


# Kube proxy
kubectl port-forward pod/POD_NOME 8080:80
