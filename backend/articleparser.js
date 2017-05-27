var sys = require("util");
var AYLIENTextAPI = require("aylien_textapi");

exports.parseArticle = function(articleUrl, callback){

  

  var textapi = new AYLIENTextAPI({
  	application_id: "6d860f5f",
  	application_key: "951d4533c5d65f1d97ea52d95e468cc2"
  });

  textapi.summarize({
    url: articleUrl,
    sentences_number: 4

  }, function(error, response) {


    if (error === null) {
      var summary='';

      response.sentences.forEach(concatSummary);

      function concatSummary(item){
        //console.log("--"+item+"\n");
        summary+="-- "+item+"\n\n";
      }

      //console.log(articleUrl+ summary);
      callback(summary);
    }
  });


}