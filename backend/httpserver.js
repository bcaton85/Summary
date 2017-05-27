var sys = require("util");
var url = require("url");
var http = require("http");
var qs = require('querystring');
const ap = require("./articleparser.js");

http.createServer(function(request, response) {
	var path = url.parse(request.url).pathname;
	var body = '';

	        request.on('error',function(err){
	        	console.log(err);
	        }).on('data', function (data) {
	            body += data;
	           
	            if (body.length > 1e6)
	                request.connection.destroy();

	        }).on('end', function () {
	             ap.parseArticle(body, function(summary){

					response.statusCode = 200;

					response.setHeader('Content-Type','text/plain');
					response.write(summary);
					response.end();

	             });  
	        });
    
}).listen(8080);
 
console.log("Server running at http://localhost:8080/");