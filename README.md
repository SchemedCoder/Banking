
# Real-Time Banking Audit Pipeline 🏦

## Overview

Enterprise-style banking audit and fraud monitoring pipeline built using Kafka, PySpark Structured Streaming, ADLS Gen2, Docker, and Streamlit.

---

## Features

- Real-time banking transaction streaming
- Fraud detection rules
- Suspicious transaction monitoring
- Audit KPIs
- Watermarking support
- Dashboard visualization

---

## Architecture

Kafka → PySpark → ADLS Gen2 → Dashboard

---

## KPIs

- Total transactions
- Suspicious transactions
- High-value transfers
- City-wise banking analytics

---

## Run Project

### Start Kafka

```bash
docker-compose up
```

### Run Producer

```bash
python producer/transaction_producer.py
```

### Run Streaming Pipeline

```bash
spark-submit spark/audit_pipeline.py
```

### Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Resume Line

Built a real-time banking audit pipeline using Kafka, PySpark Structured Streaming, ADLS Gen2, Docker, and Streamlit to monitor transaction activity and detect suspicious banking patterns.
