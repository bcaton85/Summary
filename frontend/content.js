//Listens for message from background.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {

    if( request.message === "clicked_browser_action" ) {

    	var href = window.location.href;
    	//Sends message back to background.js
       chrome.runtime.sendMessage({"message": "retrieved_url", "url": href});

    }

    if(request.message === "summary_returned"){
    	alert(request.summary);
    }
  }
);