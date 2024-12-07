# US Visa Approval Prediction

This project predicts the approval status of US visa applications using machine learning and deep learning models, integrated with an MLOps pipeline for streamlined deployment.

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Solution Approach](#solution-approach)
- [Deployment](#deployment)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
Visa applications are often complex and influenced by multiple factors. This project focuses on building a robust model that predicts visa approval based on features like education, job experience, and company-specific information. The project also demonstrates how MLOps practices can be used to deploy and monitor such predictive models effectively.

---

## Problem Statement
Given a set of features such as:
- Continent
- Education level
- Job experience
- Training requirements
- Employment type
- Company-specific details (e.g., employee count, prevailing wage, contract tenure)

The task is to predict whether a visa application will be **approved** or **rejected**.

---

## Features
Key features in the dataset include:
- **Continent:** Asia, Africa, North America, Europe, South America, Oceania
- **Education Level:** High School, Bachelor's, Master's, Doctorate
- **Job Experience:** Yes/No
- **Required Training:** Yes/No
- **Employee Count:** 15,000 to 40,000
- **Region of Employment:** West, Northeast, South, Midwest, Island
- **Prevailing Wage:** 700 to 70,000
- **Contract Tenure:** Hour, Year, Week, Month
- **Full-time Employment:** Yes/No
- **Company Age:** 15 to 180 years

---

## Solution Approach
The solution consists of:
1. **Machine Learning:**  
   - Classification algorithms for predicting visa approval.
2. **Deep Learning:**  
   - A custom Artificial Neural Network (ANN) with a sigmoid activation function for binary classification.

---

## Deployment
The deployment process involves:
- **Docker:** Containerized application for scalability and reproducibility.
- **Cloud Services:** Hosting the solution on cloud platforms.
- **Self-Hosted Runner:** Automating CI/CD workflows.
- **Workflows:** Automated pipelines for training, validation, and deployment.

---

## Getting Started
### Prerequisites
- Docker
- Python 3.8+
- Cloud account (AWS/GCP/Azure)
- GitHub Actions

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/us-visa-approval-prediction.git
   cd us-visa-approval-prediction
