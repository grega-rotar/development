docker build . -t registry.etiam.si/public/grega-dev
docker push registry.etiam.si/public/grega-dev
kubectl apply -f deployment.yaml
kubectl rollout restart deployment grega-dev -n grega-dev