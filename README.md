# LLM4Kube
Code for CSCE 670 project LLM4Kube (https://viveklol.github.io/LLM4Kube/)

## Setup of Kubernetes and Open Telemetry Application.
Follow the official Open Telemetry Demo to setup a mock application on your local machine: https://opentelemetry.io/docs/demo/architecture/

## Generating Logs
After setting up the application, you can start generating logs. This covers a vareity of services and the Open Telemetry website provides important information with regards to this.

## LLMs for Augmentation
We prompted GPT-3.5-Turbo with the logs generated for each application to generate more logs, we have collected around 400 logs covering multiple scenarios. 

We also create a simple test set for evaluation.

To the best of our knowledge we are the first to attempt this.

## LLMs for Analysis

For analysis we used ChatGPT API and Groq APIs, we directly access Gemini via UI.

1. To run these scripts, auth tokens need to be stored.
2. The scripts can be run from `chatgpt.py` and `groq-llama3.py`

## Experiments

We provide a reference to our experiments workbook in this repo.

## Sample Responses:
Demoing our best results which were seen on GPT-3.5 Turbo.

1. Zero Shot GPT-3.5-Turbo: https://chat.openai.com/share/7bf980df-4a47-4269-8715-4330b6a52037
2. Few Shot GPT-3.5-Turbo: https://chat.openai.com/share/5bacb47e-eadc-4513-a84b-04656e68690e
3. Few Shot COT GPT-3.5-Turbo: https://chat.openai.com/share/3944194c-8a03-445a-b14f-e2c8fdba9f85
