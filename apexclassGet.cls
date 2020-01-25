// paste to console developer or in your class as you want 
Http http = new Http();
HttpRequest request = new HttpRequest();


request.setEndpoint('http://b5a60fef.ngrok.io/'); // # Exposed local webserver by ngrok please see read me file  and also add this address to remote site settings
request.setMethod('GET');
HttpResponse response = http.send(request);
// If the request is successful, parse the JSON response.
if (response.getStatusCode() == 200) {
    // Deserialize the JSON string into collections of primitive data types.
    List<account> results = ( List<account>) JSON.deserialize(response.getBody(), List<account>.class);
    // Cast the values in the 'animals' key as a list
	insert results;    
        System.debug(results);
    }

