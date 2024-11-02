from flask import Flask, render_template, request
import arxiv

app = Flask(__name__)

def search_by_topic(topic):
    # Use arXiv API to search by topic
    search = arxiv.Search(
        query=topic,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'authors': ', '.join([author.name for author in result.authors]),
            'published': result.published,
            'abstract': result.summary,
            'pdf_url': result.pdf_url
        })
    return papers

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']  # Get the topic from the form
        papers = search_by_topic(topic)  # Search papers by topic
        return render_template('index.html', papers=papers, topic=topic)
    
    return render_template('index.html')  # Render the form on GET request

if __name__ == '__main__':
    app.run(debug=True)