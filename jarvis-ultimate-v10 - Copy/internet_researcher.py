from duckduckgo_search import DDGS

class InternetResearcher:
    def __init__(self):
        self.region = "wt-wt" # Global search

    def search_web(self, query, max_results=5):
        """Fetches live search results using DuckDuckGo."""
        try:
            results_text = []
            with DDGS() as ddgs:
                results = list(ddgs.text(query, region=self.region, safesearch='moderate', max_results=max_results))
                for r in results:
                    results_text.append(f"Title: {r.get('title')}\nURL: {r.get('href')}\nSummary: {r.get('body')}")
            
            if not results_text:
                return f"No web results found for '{query}'."
            return "\n\n".join(results_text)
            
        except Exception as e:
            return f"Internet research error: {str(e)}"

    def search_news(self, query, max_results=5):
        """Fetches recent news headlines."""
        try:
            news_text = []
            with DDGS() as ddgs:
                results = list(ddgs.news(query, region=self.region, safesearch='moderate', max_results=max_results))
                for r in results:
                    news_text.append(f"Headline: {r.get('title')}\nSource: {r.get('source')}\nURL: {r.get('url')}")
            
            if not news_text:
                return f"No news results found for '{query}'."
            return "\n\n".join(news_text)
            
        except Exception as e:
            return f"News research error: {str(e)}"