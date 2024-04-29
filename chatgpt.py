from openai import OpenAI
import os
import argparse

client = OpenAI()
MESSAGE_TEMPLATES = {
    'zero_shot': """
    Failed Service	Affected Service (Hard)
Accounting Service	Kafka, Checkout Service, Frontend
Fraud Detection Service	Kafka, Checkout Service, Frontend
Redis	Cart Service, Frontend
Kafka	Checkout Service, Accounting Service, Fraud Detection Service, Frontend
Cart Service	Frontend, Checkout Service
Product Catalog Service	Recommendation Service, Frontend, Checkout Service
Currency Service	Frontend, Checkout Service
Email Service	Checkout Service
Payment Service	Checkout Service
Quote Service	Shipping Service
Shipping Service	Checkout Service, Frontend
Checkout Service	Frontend
Ad Service	Frontend
Recommendation Service	Frontend

"Above Tabular data is Failed Data service and the services that are affected because of the failed service". Now based on below given log answer following questions:
1. Is this log error or information or warning?
2. Also tell me which services are affected?

Given log: {log}
""",
    'few_shot': """
Failed Service	Affected Service
Accounting Service	Kafka, Checkout Service, Frontend
Fraud Detection Service	Kafka, Checkout Service, Frontend
Redis	Cart Service, Checkout Service, Frontend
Kafka	Checkout Service, Frontend
Cart Service	Frontend, Checkout Service
Product Catalog Service	Recommendation Service, Frontend, Checkout Service
Currency Service	Frontend, Checkout Service
Email Service	Checkout Service, Frontend
Payment Service	Checkout Service, Frontend
Quote Service	Shipping Service, Frontend
Shipping Service	Checkout Service, Frontend
Checkout Service	Frontend
Ad Service	Frontend
Recommendation Service	Frontend

"Above Tabular data is Failed Data service and the services that are affected because of the failed service". Now based on below given log answer following questions:
1. Is this log error or information or warning?
2. Also tell me which services are affected?

Given log: [2024-04-16T17:53:10.123456] kubernetes - ERROR --: Pod my-otel-demo-cartservice restarted due to out-of-memory error.

Answer for Question 1 is: It is error log.
Answer for Question 2 is: Cart Service is affected which in turn affects Frontend and Checkout Service as per tabular data given above.

Given log: [2024-04-16T17:53:15.234567] my-otel-demo-adservice - ERROR --: Error processing request for ad ID: 12345. Database connection timed out.

Answer for Question 1 is: It is error log.
Answer for Question 2 is: Add Service is affected which in turn affects Frontend Service as per tabular data given above.

Given log: [2024-04-16T17:54:30.789012] my-otel-demo-paymentservice - WARNING --: Payment processing delayed. Bank server maintenance in progress.

Answer for Question 1 is: It is warning log.
Answer for Question 2 is: Payment Service is affected which in turn affects Frontend Service and Checkout Service as per tabular data given above.

Now similarly answer for below log:
{log}
""",
    'COT': """
Failed Service	Affected Service
Accounting Service	Kafka, Checkout Service, Frontend
Fraud Detection Service	Kafka, Checkout Service, Frontend
Redis	Cart Service, Checkout Service, Frontend
Kafka	Checkout Service, Frontend
Cart Service	Frontend, Checkout Service
Product Catalog Service	Recommendation Service, Frontend, Checkout Service
Currency Service	Frontend, Checkout Service
Email Service	Checkout Service, Frontend
Payment Service	Checkout Service, Frontend
Quote Service	Shipping Service, Frontend
Shipping Service	Checkout Service, Frontend
Checkout Service	Frontend
Ad Service	Frontend
Recommendation Service	Frontend

"Above Tabular data is Failed Data service and the services that are affected because of the failed service". Now based on below given log tell me which services are affected:

Given log:  [2024-04-16T17:53:10.123456] kubernetes - ERROR --: Pod my-otel-demo-cartservice restarted due to out-of-memory error.

"Let's break it down step by step:

1. Identify the Failed Service: The log indicates that the Cart Service failed. So, the failed service is Cart Service.
2. Determine Affected Services: According to the table, the affected services when the Cart Service fails are:
Checkout Service
Frontend
Conclusion: The Checkout Service and Frontend services are affected by the failure of the Email Service."

Given log: [2024-04-16T17:53:15.234567] my-otel-demo-adservice - ERROR --: Error processing request for ad ID: 12345. Database connection timed out.

"Let's break it down step by step:

1. Identify the Failed Service: The log indicates that the Ad Service failed. So, the failed service is Ad Service.
2. Determine Affected Services: According to the table, the affected services when the Ad Service fails are:
Frontend
Conclusion: The Frontend service is affected by the failure of the Ad Service."

Given log: [2024-04-16T17:54:30.789012] my-otel-demo-paymentservice - WARNING --: Payment processing delayed. Bank server maintenance in progress.

"Let's break it down step by step:

1. Identify the Failed Service: The log indicates that the Payment Service failed. So, the failed service is Payment Service.
2. Determine Affected Services: According to the table, the affected services when the Payment Service fails are:
Checkout
Frontend
Conclusion: The Frontend service and Checkout Services are affected by the failure of the Payment Service."

Now similarly answer for below other logs:
{log}
"""
}

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Arguments for script.')
    parser.add_argument('--mode', type=str, choices=['zero_shot', 'COT', 'few_shot'], default='zero_shot', help='Prompting Mode')
    parser.add_argument('--log_file', type=str, choices=['logs_test', 'all_logs'], default='logs_test', help='Logs to read.')

    args = parser.parse_args()
    message = MESSAGE_TEMPLATES[args.mode]

    with open(f'{args.log_file}.txt', 'r') as file:
        logs = [line.strip() for line in file.readlines()]
    responses = []
    for i, log in enumerate(logs):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a DevOPs expert, and are skilled in Kubernetes. Your task is to analyze some application logs."},
                {"role": "user", "content": message.format(log=log)}
            ]
        )
        responses.append(completion.choices[0].message)
    
    with open('./gpt_responses.txt', 'w') as f:
        f.write("\n".join(responses))


    