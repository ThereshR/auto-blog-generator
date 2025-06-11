# utils/research.py

from serpapi import GoogleSearch
import json

SERPAPI_API_KEY = "062cc029422ad823c6f30acbbf49ca9e102eca0b7219a82984f3cc4146be4569"  # Replace with your actual SerpAPI key

def get_research_snippets(topic, limit=3):
    print(f"🔍 Researching topic: {topic}")
    
    params = {
        "engine": "google",
        "q": f'"{topic}" research insights',  # Better search query
        "num": limit * 2,  # Get more results to filter from
        "api_key": SERPAPI_API_KEY,
        "hl": "en",  # Language
        "gl": "us"   # Country
    }
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        print("🔍 Debug - API Response keys:", list(results.keys()))
        
        snippets = []
        organic_results = results.get("organic_results", [])
        
        if not organic_results:
            print("⚠️ No organic results found")
            return ["No search results available for this topic."]
        
        for result in organic_results[:limit]:
            snippet = result.get("snippet", "").strip()
            title = result.get("title", "").strip()
            
            # Combine title and snippet for better context
            if snippet:
                if title and title not in snippet:
                    combined = f"{title}: {snippet}"
                else:
                    combined = snippet
                snippets.append(combined)
            elif title:
                snippets.append(title)
        
        # Filter out very short snippets
        quality_snippets = [s for s in snippets if len(s) > 20]
        
        if not quality_snippets:
            return ["Limited information available for this topic."]
        
        return quality_snippets[:limit]
    
    except KeyError as e:
        print(f"⚠️ Key error in API response: {e}")
        return [f"Data parsing error for topic '{topic}'."]
    
    except Exception as e:
        print(f"⚠️ Research failed for '{topic}': {e}")
        print(f"Error type: {type(e)}")
        return ["Research service temporarily unavailable."]