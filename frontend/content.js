
//Listens for message from background.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {

    // Sends message with article url back to the background script when clicked
    if( request.message === "clicked_browser_action" ) {
    	var href = window.location.href;
       chrome.runtime.sendMessage({"message": "retrieved_url", "url": href});
    }

    // Format and display the parsed article
    if(request.message === "summary_returned"){
      var summary = request.summary.summary;
      var summaryArray = summary.split("--");
      var summaryFormatted = [
        "Objectivity: "+summaryArray[0],
        "-- "+summaryArray[1],
        "-- "+summaryArray[2],
        "-- "+summaryArray[3],
        "-- "+summaryArray[4]
      ];

      var display = humane.create({timeout: 0, clickToClose: true});
      display.log(summaryFormatted);
    }
  }
);