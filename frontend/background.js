/*
 *Sends message to conent script when the icon is clicked on.
 */
chrome.browserAction.onClicked.addListener(function(tab) {

  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});

  });
});

//Message received back from content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {

    if( request.message === "retrieved_url" ) {
    	
    	var params = request.url;
    	var http = new XMLHttpRequest();
    	http.open("POST", "http://localhost:8080", true);

		http.setRequestHeader("Content-type", "text/plain");

		http.onreadystatechange = function() {
			if(http.readyState == 4 && http.status == 200) {

				chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, {"message": "summary_returned","summary":http.responseText});

        });
		  }
    }

		http.send(params);
    
  }
});