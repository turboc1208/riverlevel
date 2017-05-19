import my_appapi as appapi
import urllib.request
import json
             
class riverlevel(appapi.my_appapi):

  def initialize(self):
    # self.LOGLEVEL="DEBUG"
    if "stationid" in self.args:
      self.stationid=self.args["stationid"]
    else:
      self.log("stationid must be set in ap./ha	pdaemon.cfg file")
    if "interval" in self.args:
      self.interval=self.args["interval"]
    else:
      self.interval=7
    if "controlname" in self.args:
      self.control_name=self.args["controlname"]
    else:  
      self.control_name="sensor.river_level"
    if "country" in self.args:
      self.log("country in appdaemon.cfg={}".format(self.args["country"]))
      self.country=self.args["country"]
    else:
      self.country="US"
      self.log("set default country={}".format(self.country))
    self.log("riverlevel App")
    self.run_every(self.timer_handler,self.datetime(),60*self.interval)

  def timer_handler(self,kwargs):
    self.log("self.country={}".format(self.country))
    if self.country=="UK":
      url=str("http://environment.data.gov.uk/flood-monitoring/id/stations/{}".format(self.stationid))
      self.log("uk url={}".format(url))
      data=urllib.request.urlopen(url).read()
      jd=json.loads(data.decode("utf-8"))
      if "latestReading" in jd["items"]["measures"]:
        newlevel=jd["items"]["measures"]["latestReading"]["value"]
      else:
        newlevel=jd["items"]["measures"][0]["latestReading"]["value"] 
      lat=0.0
      lon=0.0 
    elif self.country=="US":
      url="https://waterservices.usgs.gov/nwis/iv/?format=json&sites={}&parameterCd=00060,00065&siteStatus=all".format(self.stationid)
      self.log("us url={}".format(url))
      data=urllib.request.urlopen(url).read()
      jd=json.loads(data.decode("utf-8"))
      for ts in jd["value"]["timeSeries"]:
        if ts["variable"]["variableCode"][0]["variableID"]==45807202:
          lat=ts["sourceInfo"]["geoLocation"]["geogLocation"]["latitude"]
          lon=ts["sourceInfo"]["geoLocation"]["geogLocation"]["longitude"]
          newlevel=ts["values"][0]["value"][0]["value"]
          break

    self.log("River Level {} ={}".format(self.stationid,newlevel))
    self.set_state(self.control_name,state=newlevel,attributes={"name":self.stationid,"latitude":lat,"longitude":lon})   
