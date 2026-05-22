from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transactions = [

    {
        "transaction_id": 1001,
        "account_id": "ACC1001",
        "customer_name": "Rahul Sharma",
        "city": "Delhi",
        "transaction_type": "UPI",
        "amount": 4500,
        "transaction_status": "SUCCESS",
        "transaction_time": "2025-01-01 10:00:00"
    },

    {
        "transaction_id": 1002,
        "account_id": "ACC1002",
        "customer_name": "Priya Singh",
        "city": "Mumbai",
        "transaction_type": "NEFT",
        "amount": 85000,
        "transaction_status": "SUCCESS",
        "transaction_time": "2025-01-01 10:01:00"
    },

    {
        "transaction_id": 1003,
        "account_id": "ACC1003",
        "customer_name": "Aman Verma",
        "city": "Bangalore",
        "transaction_type": "IMPS",
        "amount": 1200000,
        "transaction_status": "SUCCESS",
        "transaction_time": "2025-01-01 10:02:00"
    }

]

for transaction in transactions:

    producer.send(
        "bank_transactions",
        value=transaction
    )

    print("✅ Transaction Sent:", transaction)

    time.sleep(2)

print("🚀 Banking transaction streaming completed")
