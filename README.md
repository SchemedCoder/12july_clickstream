# Clickstream Analytics Platform

## Overview

A production-style real-time clickstream analytics platform built using Apache Kafka, PySpark Structured Streaming, Delta Lake, Azure Data Lake Gen2, Azure Synapse Analytics, and Power BI.

The platform simulates website click events, ingests them into Kafka, processes streaming data through a Medallion Architecture (Bronze → Silver → Gold), and generates business-ready analytics for reporting.

---

## Features

- Real-time clickstream ingestion
- Kafka event streaming
- PySpark Structured Streaming
- Bronze, Silver and Gold layers
- Sessionization
- Data cleansing and enrichment
- Delta Lake storage
- Azure Data Lake Gen2 integration
- Azure Synapse Analytics
- Power BI reporting
- Docker support
- GitHub Actions CI/CD

---

## Architecture

Website Users

↓

Kafka Producer

↓

Kafka Topic

↓

PySpark Structured Streaming

↓

Bronze Layer

↓

Silver Layer

↓

Gold Layer

↓

Azure Synapse Analytics

↓

Power BI Dashboard

---

## Tech Stack

- Python
- Apache Kafka
- PySpark
- Delta Lake
- Azure Data Lake Gen2
- Azure Synapse Analytics
- Power BI
- Docker
- GitHub Actions

---

## Folder Structure

See the repository structure for complete implementation.

---

## Future Enhancements

- Azure Event Hubs
- Microsoft Fabric
- Databricks Workflows
- Real-time anomaly detection
- Machine Learning recommendations
