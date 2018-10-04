from analyze import analyze
from aylienapiclient import textapi

client = textapi.Client("username", "password")

def summarizeArticle(url):
	summary = ""
	print("confflict")
	summaryResponse = client.Summarize({'url': url, 'sentences_number': 4})
	for sentence in summaryResponse['sentences']:
  		summary += "--" + sentence +"\n\n"
	return analyze(summary)
