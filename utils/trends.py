from serpapi import GoogleSearch
import json

SERPAPI_API_KEY = "062cc029422ad823c6f30acbbf49ca9e102eca0b7219a82984f3cc4146be4569"  # Replace with your real key

def get_trending_topics_serpapi(geo="IN", limit=2):
    print("📡 Fetching trending topics from SerpAPI...")
    
    params = {
        "engine": "google_trends_trending_now",  # More specific engine
        "geo": geo,
        "api_key": SERPAPI_API_KEY
    }
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        print("📨 Raw SerpAPI Response:")
        print(json.dumps(results, indent=2))
        
        # Handle different response structures
        trending_searches = []
        
        if "trending_searches" in results:
            trending_searches = results["trending_searches"]
        elif "trendingSearchesDays" in results:
            days = results["trendingSearchesDays"]
            if days and "trendingSearches" in days[0]:
                trending_searches = days[0]["trendingSearches"]
        
        if not trending_searches:
            print("⚠️ No trending searches found in response")
            return ["AI in healthcare", "Climate change impact"]
        
        topics = []
        for item in trending_searches[:limit]:
            if isinstance(item, dict):
                if "title" in item and "query" in item["title"]:
                    topics.append(item["title"]["query"])
                elif "query" in item:
                    topics.append(item["query"])
                elif isinstance(item, str):
                    topics.append(item)
        
        return topics if topics else ["AI in healthcare", "Climate change impact"]
        
    except Exception as e:
        print(f"⚠️ Error occurred: {e}")
        return ["AI in healthcare", "Climate change impact"]