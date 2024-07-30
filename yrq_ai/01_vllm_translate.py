"""
curl http://192.168.10.59:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer token-abc123" \
-d '{
"model": "/mnt/nfs_share_test/yangruiqing/openchat-3.6-8b-20240522",
"messages": [
{"role": "system", "content": "You are a good assistant in translating English into Chinese."},
{"role": "user", "content": "OpenAI Compatible Server"}
]
}'  
"""

from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.10.59:8000/v1",
    api_key="token-abc123",
)

def get_tranlate(text):
    completion = client.chat.completions.create(
        model="/mnt/nfs_share_test/yangruiqing/openchat-3.6-8b-20240522",
        messages=[
            {
                "role": "system",
                "content": "You are a good assistant in translating English into Chinese.",
            },
            {"role": "user", "content": text},
        ],
    )
    return completion.choices[0].message.content


