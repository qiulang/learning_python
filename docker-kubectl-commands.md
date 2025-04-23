# Docker to Kubernetes Command Translation

This guide provides a comprehensive mapping between Docker commands and their Kubernetes (kubectl) equivalents.

## Container/Pod Management
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker ps` | `kubectl get pods` | List running pods |
| `docker ps -a` | `kubectl get pods --all-namespaces` | List all pods across all namespaces |
| `docker run <image>` | `kubectl run <name> --image=<image>` | Run a single pod |
| | `kubectl create deployment <name> --image=<image>` | Create a deployment (recommended) |
| `docker exec -it <container> <command>` | `kubectl exec -it <pod> -- <command>` | Execute command in pod |
| `docker logs <container>` | `kubectl logs <pod>` | View pod logs |
| `docker stop <container>` | No direct equivalent - pods are either running or deleted | See below |
| | `kubectl scale deployment/<name> --replicas=0` | Scale to zero (similar effect) |
| `docker rm <container>` | `kubectl delete pod <pod>` | Delete pod |
| `docker restart <container>` | `kubectl rollout restart deployment/<name>` | Restart all pods in deployment |
| | `kubectl delete pod <pod>` | For individual pods (if controlled by deployment) |

## Image Management
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker pull <image>` | No direct equivalent - Kubernetes pulls images automatically | Images are pulled when pods are created |
| `docker build -t <image> .` | No direct equivalent | Build locally, push to registry, then reference in YAML |
| `docker tag <image> <new-image>` | No direct equivalent | Perform in container registry before deployment |
| `docker push <image>` | No direct equivalent | Push to registry before referencing in Kubernetes |

## Updating & Deployments
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| Update container (multi-step process) | `kubectl set image deployment/<name> <container-name>=<new-image:tag>` | Update image in deployment |
| | `kubectl apply -f deployment.yaml` | Apply updated config file |
| `docker-compose up` | `kubectl apply -f <compose-converted-yaml>` | Apply from config files |

## Service/Networking
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker port <container>` | `kubectl get service <service>` | View service port mappings |
| `docker network create` | `kubectl create service` | Create service |
| | `kubectl apply -f service.yaml` | Apply service from file |
| `docker network ls` | `kubectl get services` | List services |
| | `kubectl get endpoints` | List service endpoints |
| `docker network connect` | No direct equivalent | Use services and label selectors |

## Storage
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker volume create` | `kubectl apply -f pv.yaml` | Create persistent volume |
| | `kubectl apply -f pvc.yaml` | Create persistent volume claim |
| `docker volume ls` | `kubectl get pv` | List persistent volumes |
| | `kubectl get pvc` | List persistent volume claims |
| `docker volume rm` | `kubectl delete pv <name>` | Delete persistent volume |
| | `kubectl delete pvc <name>` | Delete persistent volume claim |

## Inspection & Status
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker inspect` | `kubectl describe pod/<pod>` | Detailed info about pod |
| | `kubectl describe deployment/<deployment>` | Detailed info about deployment |
| | `kubectl describe service/<service>` | Detailed info about service |
| `docker stats` | `kubectl top pods` | Pod CPU/memory usage |
| | `kubectl top nodes` | Node CPU/memory usage |

## Resource Control
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker update --memory/--cpu-shares` | `kubectl set resources deployment <name> --limits=cpu=<value>,memory=<value>` | Update resource limits |
| | `kubectl edit deployment <name>` | Edit deployment definition |

## Context/Namespace Management
| Docker Command | Kubernetes Command | Notes |
|----------------|-------------------|-------|
| `docker context use` | `kubectl config use-context <context>` | Switch context |
| `docker context ls` | `kubectl config get-contexts` | List available contexts |
| N/A | `kubectl config current-context` | Show current context |
| N/A | `kubectl create namespace <name>` | Create namespace |
| N/A | `kubectl get namespaces` | List namespaces |
| N/A | `kubectl config set-context --current --namespace=<namespace>` | Set default namespace |

## Additional Kubernetes-specific Commands
| Command | Description |
|---------|-------------|
| `kubectl apply -f <yaml-file>` | Create/update resources from file |
| `kubectl get all` | List all resources in current namespace |
| `kubectl get nodes` | List cluster nodes |
| `kubectl rollout status deployment/<name>` | Check deployment rollout status |
| `kubectl rollout history deployment/<name>` | View rollout history |
| `kubectl rollout undo deployment/<name>` | Rollback deployment |
| `kubectl port-forward <pod> <local-port>:<pod-port>` | Forward ports to pod |
| `kubectl scale deployment <name> --replicas=<count>` | Scale deployment |
| `kubectl cluster-info` | Display cluster info |
| `kubectl api-resources` | Show all available resource types |
| `kubectl explain <resource>` | Documentation for resource |

## Notes on Kubernetes vs Docker Paradigms
- Kubernetes operates at a higher abstraction level than Docker
- Pods are ephemeral and managed by controllers; individual pod lifecycle is less important
- Deployments, not individual pods, are the primary management unit
- Services provide stable networking regardless of underlying pod changes
- Configuration is primarily declarative (YAML) rather than imperative commands
