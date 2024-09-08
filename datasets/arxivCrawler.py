import feedparser

def fetch_arxiv_papers(query, max_results=100):
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'search_query={query}'
    results_limit = f'&max_results={max_results}'
    sort_by = '&sortBy=submittedDate&sortOrder=descending'

    query_url = f"{base_url}{search_query}{results_limit}{sort_by}"

    feed = feedparser.parse(query_url)
    papers = []
    
    for entry in feed.entries:
        paper = {
            'title': entry.title,
            'abstract': entry.summary,
            'published': entry.published,
            'pdf_url': entry.link,
            'authors': [author.name for author in entry.authors]
        }
        papers.append(paper)
        
    return papers

# Example usage:
papers = fetch_arxiv_papers('optimization', max_results=100)
for paper in papers:
    print(paper['title'])