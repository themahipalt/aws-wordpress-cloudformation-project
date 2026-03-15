# AWS WordPress Deployment using CloudFormation

## Project Description

This project demonstrates how to deploy and manage a WordPress environment on AWS using Infrastructure as Code (IaC) with AWS CloudFormation. The goal is to automate the provisioning of infrastructure resources and ensure a scalable, secure, and cost-effective environment for hosting a WordPress website.

The project creates a complete AWS infrastructure that includes networking components, compute resources, and monitoring services required to run a WordPress instance. The deployment is automated using CloudFormation templates, allowing the infrastructure to be easily replicated and managed.

The environment also includes automation to start and stop development instances during business hours (9 AM – 6 PM) using AWS Lambda and EventBridge scheduling, helping reduce operational costs.

This project follows cloud best practices by separating public and private resources within a Virtual Private Cloud (VPC), implementing security groups for controlled access, and enabling monitoring through AWS CloudWatch.

---

## Project Objectives

* Deploy a WordPress instance on AWS using AWS CloudFormation
* Create a production environment for hosting live blog content
* Create a development and testing environment separate from production
* Automate infrastructure deployment using Infrastructure as Code
* Monitor system performance and health using AWS monitoring services
* Implement cost optimization by scheduling development instances to run only during business hours

---

## Architecture Overview

The project deploys a two-tier architecture consisting of a web server layer and a database layer. The web server is deployed in a public subnet so it can be accessed from the internet, while the database is placed in a private subnet for enhanced security.

The architecture includes:

* Amazon VPC for network isolation
* Public and private subnets for secure resource placement
* Internet Gateway for public internet access
* NAT Gateway for private subnet outbound connectivity
* EC2 instance for the WordPress web server
* Database instance for WordPress data storage
* Security Groups for controlled network access
* AWS Lambda functions for automation
* EventBridge Scheduler for instance scheduling
* Amazon CloudWatch for monitoring and logging

---

## Technologies Used

* AWS CloudFormation – Infrastructure provisioning
* Amazon EC2 – WordPress web server hosting
* Amazon VPC – Network isolation and control
* AWS Lambda – Automation for instance management
* Amazon EventBridge – Scheduled start/stop of development instances
* Amazon CloudWatch – Monitoring and logging
* GitHub – Version control and project repository
* Python (Boto3) – AWS automation scripts

---

## Project Structure

```
aws-wordpress-cloudformation-project
│
├── cloudformation
│     └── wordpress-stack.yaml
│
├── lambda
│     ├── start_instance.py
│     └── stop_instance.py
│
├── docs
│     └── architecture.md
│
└── README.md
```

---

## Deployment Steps

1. Clone the GitHub repository to your local system
2. Navigate to the project directory
3. Upload the CloudFormation template to AWS CloudFormation
4. Launch the stack to create the infrastructure
5. Access the WordPress instance using the EC2 public IP address
6. Configure WordPress through the web setup page

---

## Monitoring

Amazon CloudWatch is used to monitor EC2 instance metrics including CPU utilization, network activity, and system performance. CloudWatch logs are also used to monitor Lambda automation functions.

---

## Automation

AWS Lambda functions are used to automatically start and stop development EC2 instances based on business hours.

Schedule:

* Start Instance – 9:00 AM
* Stop Instance – 6:00 PM

This automation helps optimize AWS usage costs.

---

## Expected Outcome

After deployment, the infrastructure will automatically provision a WordPress server environment on AWS. Users will be able to access the WordPress setup page through the EC2 public IP address and configure their blog platform.

The project demonstrates how Infrastructure as Code can be used to automate cloud infrastructure deployment and management in real-world scenarios.
