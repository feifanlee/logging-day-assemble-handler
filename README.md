# logging-day-assemble-handler

## this class is to resolve

* python logging
* ratation log
* keep all log
* assemble old log file by day

## how to use

* put *myHandler.py* in running directory
* set handler into myHandler.AdHandler in config file
> class=myHandler.AdHandler
* args are:
	+ log basefilename
	+ log rotation unit
	+ log rotation interval
	+ forget others
> args=('./log/abc.log','H',2)




