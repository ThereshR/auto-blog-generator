# data/research.py
import requests

def get_research(topic):
    headers = {"Authorization": "Bearer YOUR_PERPLEXITY_KEY"}
    payload = {"query": topic}
    res = requests.post("https://api.perplexity.ai/v1/query", json=payload, headers=headers)
    return res.json().get("answer", "")
