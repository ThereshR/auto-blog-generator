# generate_blog.py

from utils.trends import get_trending_topics_serpapi
from models.blog_writer import generate_blog
import os

def main():
    print("🚀 Starting blog generation process...")

    topics = get_trending_topics_serpapi(geo='IN', limit=2)
    
    print("📈 Trending Topics:", topics)

    for topic in topics:
        print(f"📝 Generating blog for: {topic}")
        blog = generate_blog(topic)

        filename = topic.replace(" ", "_").replace("/", "-")
        output_path = f"data/blogs/{filename}.md"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(blog)

        print(f"✅ Blog saved at: {output_path}")

    print("✅ Blog generation completed!")

if __name__ == "__main__":
    print("🐍 Running generate_blog.py...")
    main()
