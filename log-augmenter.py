from openai import OpenAI
import os
import argparse

client = OpenAI()

initial_log_prompt = '''
    (venv) E:\Tamu_courses\ISR\proj>kubectl logs my-otel-demo-emailservice-754f574fcc-mtnhf --all-containers=true
I, [2024-04-16T16:28:32.764920 #1]  INFO -- : Instrumentation: OpenTelemetry::Instrumentation::Sinatra was successfully installed with the following options {}
Puma starting in single mode...
* Puma version: 6.4.0 (ruby 3.2.2-p53) ("The Eagle of Durango")
*  Min threads: 0
*  Max threads: 5
*  Environment: production
*          PID: 1
== Sinatra (v3.1.0) has taken the stage on 8080 for production with backup from Puma
* Listening on http://0.0.0.0:8080
Use Ctrl-C to stop
Order confirmation email sent to: moore@example.com
10.244.0.52 - - [16/Apr/2024:16:30:37 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.5992
E, [2024-04-16T16:30:38.454061 #1] ERROR -- : OpenTelemetry error: OTLP exporter received rpc.Status{message=data refused due to high memory usage, details=[]}     
E, [2024-04-16T16:30:38.454137 #1] ERROR -- : OpenTelemetry error: Unable to export 4 spans
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:30:53 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0023
Order confirmation email sent to: mark@example.com
10.244.0.52 - - [16/Apr/2024:16:31:06 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:31:06 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0015
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:31:26 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0015
Order confirmation email sent to: steve@example.com
10.244.0.52 - - [16/Apr/2024:16:31:44 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: jeff@example.com
10.244.0.52 - - [16/Apr/2024:16:32:11 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: mark@example.com
10.244.0.52 - - [16/Apr/2024:16:32:57 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0016
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:32:59 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0015
Order confirmation email sent to: steve@example.com
10.244.0.52 - - [16/Apr/2024:16:34:07 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0016
E, [2024-04-16T16:34:08.561609 #1] ERROR -- : OpenTelemetry error: OTLP exporter received rpc.Status{message=data refused due to high memory usage, details=[]}     
E, [2024-04-16T16:34:08.561694 #1] ERROR -- : OpenTelemetry error: Unable to export 4 spans
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:34:23 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0025
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:34:56 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0033
10.244.0.52 - - [16/Apr/2024:16:34:58 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0021
Order confirmation email sent to: bill@example.com
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:35:16 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:35:34 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: mark@example.com
10.244.0.52 - - [16/Apr/2024:16:36:49 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: mark@example.com
10.244.0.52 - - [16/Apr/2024:16:36:56 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0025
Order confirmation email sent to: tobias@example.com
10.244.0.52 - - [16/Apr/2024:16:38:11 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:39:11 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0028
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:39:39 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: tobias@example.com
10.244.0.52 - - [16/Apr/2024:16:39:41 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:40:34 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0036
Order confirmation email sent to: tobias@example.com
10.244.0.52 - - [16/Apr/2024:16:40:48 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0021
Order confirmation email sent to: mark@example.com
10.244.0.52 - - [16/Apr/2024:16:41:45 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: jeff@example.com
10.244.0.52 - - [16/Apr/2024:16:45:50 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0021
Order confirmation email sent to: tobias@example.com
10.244.0.52 - - [16/Apr/2024:16:46:48 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:47:16 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: jack@example.com
10.244.0.52 - - [16/Apr/2024:16:48:03 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0026
Order confirmation email sent to: jack@example.com
10.244.0.52 - - [16/Apr/2024:16:48:08 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0015
Order confirmation email sent to: jeff@example.com
10.244.0.52 - - [16/Apr/2024:16:48:15 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0019
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:48:17 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:48:26 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0026
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:48:34 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0020
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:48:48 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: moore@example.com
10.244.0.52 - - [16/Apr/2024:16:48:48 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0014
Order confirmation email sent to: tobias@example.com
10.244.0.52 - - [16/Apr/2024:16:48:52 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0015
E, [2024-04-16T16:48:54.152148 #1] ERROR -- : OpenTelemetry error: OTLP exporter received rpc.Status{message=data refused due to high memory usage, details=[]}     
E, [2024-04-16T16:48:54.152203 #1] ERROR -- : OpenTelemetry error: Unable to export 4 spans
Order confirmation email sent to: jack@example.com
10.244.0.52 - - [16/Apr/2024:16:49:04 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0016
2024-04-16 16:49:17 - NoMethodError - undefined method `each' for nil:NilClass:
        /email_server/views/confirmation.erb:44:in `__tilt_2840'
        /usr/local/bundle/gems/tilt-2.3.0/lib/tilt/template.rb:207:in `bind_call'
        /usr/local/bundle/gems/tilt-2.3.0/lib/tilt/template.rb:207:in `evaluate'
        /usr/local/bundle/gems/tilt-2.3.0/lib/tilt/template.rb:102:in `render'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:866:in `render'
        /usr/local/bundle/gems/opentelemetry-instrumentation-sinatra-0.23.2/lib/opentelemetry/instrumentation/sinatra/extensions/tracer_extension.rb:27:in `block in render'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace/tracer.rb:37:in `block in in_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace.rb:70:in `block in with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/context.rb:87:in `with_value'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace.rb:70:in `with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace/tracer.rb:37:in `in_span'
        /usr/local/bundle/gems/opentelemetry-instrumentation-sinatra-0.23.2/lib/opentelemetry/instrumentation/sinatra/extensions/tracer_extension.rb:23:in `render' 
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:748:in `erb'
        email_server.rb:43:in `block in send_email'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace/tracer.rb:37:in `block in in_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace.rb:70:in `block in with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/context.rb:87:in `with_value'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace.rb:70:in `with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace/tracer.rb:37:in `in_span'
        email_server.rb:38:in `send_email'
        email_server.rb:27:in `block in <main>'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1763:in `call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1763:in `block in compile!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1066:in `block (3 levels) in route!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1084:in `route_eval'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1066:in `block (2 levels) in route!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1115:in `block in process_route'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1113:in `catch'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1113:in `process_route'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1064:in `block in route!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1061:in `each'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1061:in `route!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1185:in `block in dispatch!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1156:in `catch'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1156:in `invoke'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1180:in `dispatch!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:996:in `block in call!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1156:in `catch'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1156:in `invoke'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:996:in `call!'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:985:in `call'
        /usr/local/bundle/gems/opentelemetry-instrumentation-sinatra-0.23.2/lib/opentelemetry/instrumentation/sinatra/middlewares/tracer_middleware.rb:19:in `call' 
        /usr/local/bundle/gems/opentelemetry-instrumentation-rack-0.23.4/lib/opentelemetry/instrumentation/rack/middlewares/tracer_middleware.rb:81:in `block (3 levels) in call'
        /usr/local/bundle/gems/opentelemetry-instrumentation-rack-0.23.4/lib/opentelemetry/instrumentation/rack.rb:45:in `block in with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/context.rb:87:in `with_value'
        /usr/local/bundle/gems/opentelemetry-instrumentation-rack-0.23.4/lib/opentelemetry/instrumentation/rack.rb:45:in `with_span'
        /usr/local/bundle/gems/opentelemetry-instrumentation-rack-0.23.4/lib/opentelemetry/instrumentation/rack/middlewares/tracer_middleware.rb:80:in `block (2 levels) in call'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace/tracer.rb:37:in `block in in_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace.rb:70:in `block in with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/context.rb:87:in `with_value'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace.rb:70:in `with_span'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/trace/tracer.rb:37:in `in_span'
        /usr/local/bundle/gems/opentelemetry-instrumentation-rack-0.23.4/lib/opentelemetry/instrumentation/rack/middlewares/tracer_middleware.rb:77:in `block in call'
        /usr/local/bundle/gems/opentelemetry-api-1.2.3/lib/opentelemetry/context.rb:71:in `with_current'
        /usr/local/bundle/gems/opentelemetry-instrumentation-rack-0.23.4/lib/opentelemetry/instrumentation/rack/middlewares/tracer_middleware.rb:74:in `call'       
        /usr/local/bundle/gems/rack-protection-3.1.0/lib/rack/protection/xss_header.rb:20:in `call'
        /usr/local/bundle/gems/rack-protection-3.1.0/lib/rack/protection/path_traversal.rb:18:in `call'
        /usr/local/bundle/gems/rack-protection-3.1.0/lib/rack/protection/json_csrf.rb:28:in `call'
        /usr/local/bundle/gems/rack-protection-3.1.0/lib/rack/protection/base.rb:53:in `call'
        /usr/local/bundle/gems/rack-protection-3.1.0/lib/rack/protection/base.rb:53:in `call'
        /usr/local/bundle/gems/rack-protection-3.1.0/lib/rack/protection/frame_options.rb:33:in `call'
        /usr/local/bundle/gems/rack-2.2.8/lib/rack/logger.rb:17:in `call'
        /usr/local/bundle/gems/rack-2.2.8/lib/rack/common_logger.rb:38:in `call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:261:in `call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:254:in `call'
        /usr/local/bundle/gems/rack-2.2.8/lib/rack/head.rb:12:in `call'
        /usr/local/bundle/gems/rack-2.2.8/lib/rack/method_override.rb:24:in `call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:219:in `call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:2074:in `call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1633:in `block in call'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1849:in `synchronize'
        /usr/local/bundle/gems/sinatra-3.1.0/lib/sinatra/base.rb:1633:in `call'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/configuration.rb:272:in `call'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/request.rb:100:in `block in handle_request'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/thread_pool.rb:378:in `with_force_shutdown'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/request.rb:99:in `handle_request'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/server.rb:443:in `process_client'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/server.rb:241:in `block in run'
        /usr/local/bundle/gems/puma-6.4.0/lib/puma/thread_pool.rb:155:in `block in spawn_thread'
10.244.0.52 - - [16/Apr/2024:16:49:17 +0000] "POST /send_order_confirmation HTTP/1.1" 500 - 0.0018
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:50:58 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0021
Order confirmation email sent to: jack@example.com
10.244.0.52 - - [16/Apr/2024:16:51:36 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0019
Order confirmation email sent to: reed@example.com
10.244.0.52 - - [16/Apr/2024:16:51:54 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0032
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:51:55 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0020
Order confirmation email sent to: jeff@example.com
10.244.0.52 - - [16/Apr/2024:16:52:27 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0022
Order confirmation email sent to: steve@example.com
10.244.0.52 - - [16/Apr/2024:16:52:47 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0019
Order confirmation email sent to: larry_sergei@example.com
10.244.0.52 - - [16/Apr/2024:16:54:00 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0023
Order confirmation email sent to: moore@example.com
10.244.0.52 - - [16/Apr/2024:16:54:58 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: jack@example.com
10.244.0.52 - - [16/Apr/2024:16:55:03 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: mark@example.com
10.244.0.52 - - [16/Apr/2024:16:55:19 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:55:29 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0016
Order confirmation email sent to: jack@example.com
10.244.0.52 - - [16/Apr/2024:16:55:36 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0024
Order confirmation email sent to: steve@example.com
10.244.0.52 - - [16/Apr/2024:16:55:38 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0018
Order confirmation email sent to: bill@example.com
10.244.0.52 - - [16/Apr/2024:16:55:40 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0020
Order confirmation email sent to: moore@example.com
10.244.0.52 - - [16/Apr/2024:16:58:21 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0024
Order confirmation email sent to: moore@example.com
10.244.0.52 - - [16/Apr/2024:17:03:55 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0558
10.244.0.52 - - [16/Apr/2024:17:04:41 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0033
Order confirmation email sent to: bill@example.com
Order confirmation email sent to: steve@example.com
10.244.0.52 - - [16/Apr/2024:17:06:48 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0025
Order confirmation email sent to: jeff@example.com
10.244.0.52 - - [16/Apr/2024:17:06:50 +0000] "POST /send_order_confirmation HTTP/1.1" 200 - 0.0017

Understand the log above. 
'''

generate_more_prompt = """
Now generate 20 logs combining all these services given below:
"Note: Logs have to be realistic and don't hallucinate"

kubernetes
my-otel-demo-adservice
my-otel-demo-cartservice
my-otel-demo-checkoutservice
my-otel-demo-currencyservice
my-otel-demo-emailservice
my-otel-demo-flagd
my-otel-demo-frontend
my-otel-demo-frontendproxy
my-otel-demo-grafana
my-otel-demo-jaeger-agent
my-otel-demo-jaeger-collector
my-otel-demo-jaeger-query
my-otel-demo-kafka
my-otel-demo-loadgenerator
my-otel-demo-otelcol
my-otel-demo-paymentservice
my-otel-demo-productcatalogservice
my-otel-demo-prometheus-server
my-otel-demo-quoteservice
my-otel-demo-recommendationservice
my-otel-demo-redis
my-otel-demo-shippingservice
otel-demo-opensearch
otel-demo-opensearch-headless

Keep them unique, and formatted as per the log above.
"""

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Arguments for script.')
    parser.add_argument('--N', type=int, default=300, help='Final Number of Logs needed.')
    args = parser.parse_args()

    augmented_logs =[]
    messages = [
                {"role": "system", "content": "You are a DevOPs expert, and are skilled in Kubernetes. Your task is to analyze some application logs."},
                {"role": "user", "content": initial_log_prompt}
            ]
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    messages.append({
        'role': 'assistant',
        'content': completion.choices[0].message
    })
    for i in range(args.N//20):
        messages.append({
            'role': 'user',
            'content': generate_more_prompt
        })
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        messages.append({
            'role': 'assistant',
            'content': completion.choices[0].message
        })
        augmented_logs.append(completion.choices[0].message)

    with open('./augmented_logs.txt', 'w') as f:
        f.write('\n'.join(augmented_logs))
        