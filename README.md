## About The Project

The event-driven microservice project focuses on developing a scalable and efficient inventory management and product ordering system using a microservices architecture. The project incorporates modern development practices such as Continuous Integration and Continuous Deployment (CICD) and leverages Kubernetes and Google Kubernetes Engine (GKE) for deployment.


## Architecture Highlights

Microservice Architecture: The project is designed around a microservices architecture, where different components of the system are broken down into smaller, independently deployable services. This architecture promotes flexibility, scalability, and maintainability.

Event-Driven Communication: The microservices communicate with each other through an event-driven approach. Events are used to signal changes in the system, such as new products being added to the inventory or orders being placed. This enables loose coupling between services and allows for asynchronous processing.

CICD Pipeline with CloudBuild: The project employs a robust CICD pipeline using CloudBuild. The pipeline is triggered automatically whenever changes are pushed to the GitHub repository's main branch. CloudBuild builds Docker images for each microservice and push it to Artifact Registry

Dockerized Microservices: Each microservice is containerized using Docker, enabling consistent deployment across various environments and eliminating potential runtime discrepancies.

GKE Deployment: The Dockerized microservices are deployed to Google Kubernetes Engine (GKE), a managed Kubernetes service. GKE provides scalability, automatic load balancing, and ease of management for the microservices.

Load Balancer for Frontend: Frontend microservices are exposed to external connections via a LoadBalancer service in GKE. This ensures that users can access the application easily and efficiently.

FastAPI Microservices and Ingress: FastAPI microservices, responsible for specific backend functionalities, are exposed to the frontend through NodePort services. This access is orchestrated using an Ingress resource, allowing for controlled and secure routing of traffic.

## Architecture
![Image](https://i.imgur.com/ExRqURI.png)
![Image](https://i.imgur.com/cDkYPAl.png)

## Screenshots

![Image](https://i.imgur.com/mw9bXqQ.png)
![Image](https://i.imgur.com/a0fi4Vl.png)
![Image](https://i.imgur.com/hICau9I.png)
![Image](https://i.imgur.com/d1C4omZ.png)
![Image](https://i.imgur.com/ffNOFXD.png)
![Image](https://i.imgur.com/ok0Qzmu.png)
![Image](https://i.imgur.com/eTpn7nP.png)


## Product Backlog Items

Helm Chart Templating: The project roadmap includes the implementation of Helm charts for managing Kubernetes manifests. Helm simplifies deployment and configuration management by enabling templating and versioning of Kubernetes resources.

Monitoring: The monitoring aspect involves integrating monitoring solutions like Prometheus and Grafana to track the health and performance of microservices and the overall system. This ensures proactive identification and resolution of issues.

Database Migration to StatefulSets: Currently, the project uses deployments for managing databases. The backlog includes migrating the databases to StatefulSets, which offer more predictable and stable network identities for database pods.
