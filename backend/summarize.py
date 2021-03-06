from analyze import analyze
from aylienapiclient import textapi

client = textapi.Client("", "")

def summarizeArticle(url):
	summary = ""
	summaryResponse = client.Summarize({'url': url, 'sentences_number': 4})
	for sentence in summaryResponse['sentences']:
		summary += "--" + sentence +"\n\n"
	return summary
