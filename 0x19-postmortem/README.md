**Issue summary**

From 5:00PM to 6:00PM EAT, the apache web server running on the docker container was down. Users were experiencing
Empty reply from server message errors, affecting 80% of the users trying to request the web page. The
root cause of this was that the apache web server had not been started.

**Timeline**

* 5:00PM - Outage begins
* 5:00PM - Teams are alerted using pager notifications
* 5:15PM - Executing netstat to check TCP connections and ping to verify that the server is reachable
* 5:28PM - Executing curl to try and request the same web page
* 5:30PM - Executing curl with a different port assignment
* 5:42PM - Escalating the issue to the DevOps team
* 5:45PM - Checking the status of the web server
* 5:58PM - Executing a script that started the apache web server
* 6:00PM - Executing curl and getting the page content (Success)

**Root cause and resolution**

The issue was caused by attempting to make a plain HTTP request against the HTTPS(TLS/SSL) web server port.
The HTTP client thus was not able to establish an encrypted session with the plain HTTP port which caused
it to fail with the empty reply from server error that users encountered. When a client made an HTTP
request, the server did not respond with a valid HTTP response code. This violated the HTTP standard, thus
triggering the empty reply from server error message.

Upon encountering the issue, I executed the ping command to verify that the web server was reachable, and
also running the netstat command to check TCP connections and TCP socket information. Since the web server
was not reachable, I decided to check the server status and found out that the server was not running.
I started the server using a bash script:
  _service apache2 start_
and executed curl,
  _curl 0:8080_
which displayed the contents of the web page as desired:
**Hello Holberton**

**Corrective and preventative measures**

* Add monitoring on server status
* Ensure that the server is started before requests are made by users
* Using the HTTP test tool in the event that the problem persists
* Using a different port
* Using https instead of HTTP
* If the error is caused by a server redirection, try executing the curl command using curl -L
* Check firewall rules and ensure that required ports and services are enabled in the firewall
