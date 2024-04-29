import os
import argparse
from groq import Groq


# Need to obtain Key from Groq.
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

MESSAGE_TEMPLATES = {
    'zero_shot': """
Service | Reliant Services
Accounting Service | Kafka, Checkout Service, Frontend
Fraud Detection Service | Kafka, Checkout Service, Frontend
Redis | Cart Service, Checkout Service, Frontend
Kafka | Checkout Service, Frontend
Cart Service | Frontend, Checkout Service
Product Catalog Service | Recommendation Service, Frontend, Checkout Service
Currency Service | Frontend, Checkout Service
Email Service | Checkout Service, Frontend
Payment Service | Checkout Service, Frontend
Quote Service | Shipping Service, Frontend
Shipping Service | Checkout Service, Frontend
Checkout Service | Frontend
Ad Service | Frontend
Recommendation Service | Frontend

"Above Tabular data is service and the second column are services that rely on the service".

Given this log and the table of service dependencies above, you have to help analyze the scenario

{log}

Questions:
1. Is this log an error, information, or warning?
2. What services are directly affected if this is a failure or warning? The service and it's reliant services are directly affected, refer to the table above for reliant services.

""",
'COT': """
Service | Reliant Services
Accounting Service | Kafka, Checkout Service, Frontend
Fraud Detection Service | Kafka, Checkout Service, Frontend
Redis | Cart Service, Checkout Service, Frontend
Kafka | Checkout Service, Frontend
Cart Service | Frontend, Checkout Service
Product Catalog Service | Recommendation Service, Frontend, Checkout Service
Currency Service | Frontend, Checkout Service
Email Service | Checkout Service, Frontend
Payment Service | Checkout Service, Frontend
Quote Service | Shipping Service, Frontend
Shipping Service | Checkout Service, Frontend
Checkout Service | Frontend
Ad Service | Frontend
Recommendation Service | Frontend

"Above Tabular data is service and the second column are services that rely on the service".

Given this log and the table of service dependencies above, you have to help analyze the scenario

{log}

Questions:
1. Is this log an error, information, or warning?
2. What services are directly affected if this is a failure or warning? The service and it's reliant services are directly affected, refer to the table above for reliant services.


Here's an example:
[2024-04-16T17:53:35.678901] my-otel-demo-emailservice - ERROR --: Failed to send order confirmation email to: john@example.com. SMTP server error.

For this case, the answers are:
1. Failure because of error:
2. Services affected:
   a. emailservice - because this is the place error happened.
   b. looking at the table we know that emailservice is relied upon by Checkout and Frontend, so they are affected as well.

Now that you have an answer, analyze the questions for the first log.
"""
}

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Arguments for script.')
    parser.add_argument('--mode', type=str, choices=['zero_shot', 'COT'], default='zero_shot', help='Prompting Mode')
    parser.add_argument('--log_file', type=str, choices=['logs_test', 'all_logs'], default='logs_test', help='Logs to read.')
    args = parser.parse_args()
    message = MESSAGE_TEMPLATES[args.mode]

    with open(f'{args.log_file}.txt', 'r') as file:
        logs = [line.strip() for line in file.readlines()]
    responses = []
    for i, log in enumerate(logs):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message.format(log=log),
                }
            ],
            model="llama3-70b-8192",
        )
        responses.append(chat_completion.choices[0].message.content)
    
    with open('./responses.txt', 'w') as f:
        f.write("\n".join(responses))
