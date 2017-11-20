//Recieved button click, send message to notify content script
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
  });
});

//Message received back from content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {

    //Send post request to python server with the url
    if( request.message === "retrieved_url" ) { 	

      var params = {url: request.url};
    	var http = new XMLHttpRequest();
    	http.open("POST", "http://localhost:8080", true);
		  http.setRequestHeader("Content-type", "application/json");

      //Recieve the the parsed article back from the server and send it to the content script
		  http.onreadystatechange = function() {
			if(http.readyState == 4 && http.status == 200) {

				chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, {"message": "summary_returned","summary":JSON.parse(http.responseText)});

        });
		  }
    }
    
    http.send(JSON.stringify(params));
    
  }
});