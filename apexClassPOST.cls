// paste to console developer or in your class as you want
Http http = new Http();
HttpRequest request = new HttpRequest();
request.setEndpoint('http://e0150e07.ngrok.io/test'); // # Exposed local webserver by ngrok please see read me file  and also add this address to remote site settings

Account acc = [select Name ,website, phone from account limit 1];
string json_record =  JSON.serialize(acc);
system.debug(json_record);
request.setMethod('POST');
request.setHeader('Content-Type', 'application/json;charset=UTF-8');
// Set the body as a JSON object
request.setBody(json_record);
HttpResponse response = http.send(request);
 System.debug('The status code returned was not expected: ' +
        response.getStatusCode() + ' ' + response.getBody());

