Track river levels on rivers in the US and UK (other countries coming if people send me a link to the rest API for json.

Install:
  Download the py file from this repository into your appdaemon app directory.  

Update your appdaemon.cfg file with the following information.
<ul>
<li>[unique name]
<li>module=riverlevel
<li>class=riverlevel
<li>country=&LTtwo letter country identifier only US and UK currently supported&GT
<li>controlname=&LTname of HA sensor to display information in&GT sensor.mississippi_at_memphis for example.  It does not have to already exist.  It will be created for you if it does not exist.
<li>stationid=&LTstationid of station to retrieve information on&GT
</ul>
The following is an example of an appdaemon.cfg file listing information for two rivers, one in the US and one in the UK.
<pre>
[riverlevel2]
module=riverlevel
class=riverlevel
controlname=sensor.river_1029TH
stationid=1029TH
country=UK
[riverlevel3]
module=riverlevel
class=riverlevel
controlname=sensor.river_mem
stationid=07032000
country=US
</pre>
<p>
US data retrieved from : https://waterservices.usgs.gov/rest/IV-Service.html
UK data retrieved from : http://environment.data.gov.uk/flood-monitoring/doc/reference
