from analyze import analyze
from aylienapiclient import textapi

client = textapi.Client("username", "password")

def summarizeArticle(url):
	summary = ""
<<<<<<< HEAD
=======
	print("pull conflict")
>>>>>>> 0f5cc99bc2db426d2fa016ff353258fa641fa6bc
	summaryResponse = client.Summarize({'url': url, 'sentences_number': 4})
	for sentence in summaryResponse['sentences']:
  		summary += "--" + sentence +"\n\n"
	return analyze(summary)
