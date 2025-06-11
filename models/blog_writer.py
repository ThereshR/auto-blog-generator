# models/blog_writer.py
import subprocess
from utils.research import get_research_snippets

def generate_blog(topic):
    try:
        research_list = get_research_snippets(topic)
        research = "\n".join(research_list)

        prompt = f"""
Use the following research to write a high-quality 500-word blog on the topic "{topic}".

Research:
{research}

Begin your blog below:
"""
        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Ollama error: {e.stderr.decode()}")
        return "[Blog generation failed]"
