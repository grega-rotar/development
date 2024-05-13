docker build . -t docker-registry.etiam.si/etiam-si
docker push docker-registry.etiam.si/etiam-si
kubectl rollout restart deployment etiam-si -n etiam-si