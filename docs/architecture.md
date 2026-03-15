~~~
VPC
│
├── Internet Gateway
│
├── Public Subnet
│   │
│   ├── Web Server (EC2)
│   │
│   └── NAT Gateway
│
├── Private Subnet
│   │
│   └── Database Server (EC2)
│
├── Route Tables
│   │
│   ├── Public Route Table
│   │   └── Route → Internet Gateway
│   │
│   └── Private Route Table
│       └── Route → NAT Gateway
│
└── Security Groups
    │
    ├── Web Server Security Group
    │   ├── HTTP (80)  → Allow Internet
    │   └── SSH (22)   → Allow Admin Access
    │
    └── Database Security Group
        └── MySQL (3306) → Allow only from Web Server


~~~