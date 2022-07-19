from kubernetes import client, config
from kubernetes.stream import stream

config = client.Configuration()

config.api_key['authorization'] = open('/var/run/secrets/kubernetes.io/serviceaccount/token').read()
config.api_key_prefix['authorization'] = 'Bearer'
config.host = 'https://kubernetes.default'
config.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
config.verify_ssl=True

# api_client는 "2. 연결 정보 설정하기" 항목을 참고한다
api_client = client.CoreV1Api(client.ApiClient(config))

# 첫 번째 argument에 당신이 사용하는 namespace를 입력한다
ret = api_client.list_namespaced_pod("fed-repl-mjh", watch=False)

print("Listing pods with their IPs:")



for i in ret.items:
    print(i)
    print(f"{i.status.pod_ip}\t{i.metadata.name}")
