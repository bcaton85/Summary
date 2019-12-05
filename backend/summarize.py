from analyze import analyze
from aylienapiclient import textapi

client = textapi.Client("6d860f5f", "951d4533c5d65f1d97ea52d95e468cc2")

def summarizeArticle(url):
	summary = ""
	summaryResponse = client.Summarize({'url': url, 'sentences_number': 4})
	for sentence in summaryResponse['sentences']:
		summary += "--" + sentence +"\n\n"
	return analyze(summary)
