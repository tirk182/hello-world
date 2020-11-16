
# Overview

This guide is to be used to incorporate a more streamlined troubleshooting process for the Uptime Connect family of devices and the other services they support onboard a locomotive.

The primary contacts for UC Troubleshooting are below:

Andrew T. Smith ([atsmith@progressrail.com](mailto:atsmith@progressrail.com))

Jeremy Crawford ([jcrawford@progressrail.com](mailto:jcrawford@progressrail.com))

# Materials

 1. PRS Laptop or Desktop
 2. Administrator Privileges on Assigned PRS Laptop or Desktop
 3. Elevated Windows 10 CMD Prompt
 4. Access to Orion


# Common Tasks

**_Find the UC Local-IP with Orion:_**

?Never used Orion

**_Find the UC Local-IP with the SDWAN Server_**

Finding the Local-IP will require a person to login to the SDWAN Routing Server as user “pradmin” and using the CLI to find the Local-IP.

 1. Login to the SDWAN Routing Server:
       _`ssh`_ [_pradmin@10.236.0.105_](mailto:pradmin@10.236.0.105)
 2. Once prompted for a password type “`pass_key`”.
 3. You should now be at a CLI “`>`” prompt.
 4. Type in _enable_ and type the password _prs_ once prompted.


<![if !vml]>![](file:///C:/Users/ballen/AppData/Local/Temp/msohtmlclip1/01/clip_image001.png)

You are now in the SDWAN Routing Server and can start searching for UC Local-IPs.

To search for a specific UC:

`show running-config interface SDWAN UC-####`_

If the server returns a blank “Current Configuration”, then the UC Serial Number you input is not saved in the SDWAN server. Please use the the same command above, but supplement the UC Serial Number with the locomotive Road Number.

Example: _`show running-config interface SDWAN EMDX1609`_

If you are still met with a blank “Current Configuration”, contact Andrew T. Smith and he will be able to find the Local-IP for you.

If SDWAN has the config for the UC Serial Number input, then it will return the UC config as below:

_<![if !vml]>![](file:///C:/Users/ballen/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)<![endif]>_

**_Check for UC Connectivity:_**

Test the local IP for connectivity to the Back Office by logging into the Back-Office server 10.236.1.12 and either attempt to SSH to the UC using the local IP or ping the local IP address. For these steps, you will need to know the UC Serial Number or Locomotive Road Number, and the UC Local-IP.

To login to our Back Office Server, use the following command in an elevated Windows CMD Prompt: 
_ssh_ [_pradmin@10.236.1.12_](mailto:pradmin@10.236.1.12)

When prompted for a password, type in “`pass_key`”.

2.) To test for connectivity, we can either SSH into the UC in question or ping it while inside 10.236.1.12.

SSH: _`ssh 10.200.XXX.XXX_ (UC Local-IP)`

If you receive a password prompt, then the UC is online and can be reached from the Back-Office.

PING: _ping 10.200.XXX.XXX_ (UC Local-IP)

If you receive a response back from the UC, then it is online and can be reached from the Back-Office.

**_For ITSC to determine where a ticket goes:_**

The following steps will walk you through a basic troubleshooting session with a customer to try and determine what could be wrong with a Locomotive that is not reporting to Intellitrain or cannot transmit Powerview data.

Ask the user what is wrong. Please gather as much information as possible.

Connecting to Intellitrain?

Powerview not sending data?

All of the above?

Get the UC Serial Number and the Locomotive, that it is installed on, Road Number.

If the User is calling for an Intellitrain issue, follow these steps:

If the locomotive is FMG, BNSF, or KCSM, make sure there is an Ethernet cable running from the ETH1 port on the UC to Port 12 on the EMD Switch.

If the locomotive is not FMG, BNSF, or KCSM, make sure there is an ethernet cable running from the ETH0 port on the UC to Port 12 on the EMD Switch.

If the User is calling for an issue with Powerview not sending data, follow these steps:

Ask if the user is currently on the locomotive in question.
If so, make sure there is a cable plugged into ETH1 on the UC that goes to the Powerview/LDARS computer and pass the ticket with High priority to Andrew T. Smith, Josh Bushkofsky, and Richard E. Arnold.

If not, skip to the next step.

Look up the UC Serial Number for the UC local IP. If the Serial number does not pull results, look up the Road Number for the UC local IP.

* Test the local IP for connectivity to the Back Office by logging into the Back-Office server 10.236.1.12 and either attempt to SSH to the UC using the local IP or ping the local IP address.

If you can SSH to the UC or get a response back from the ping, then the UC is online.

If the user is calling to report that the Unit is not updating Intellitrain, send to Paul Jezior and Brian Meyers at this point.

If the user is calling to report that the locomotive is not sending Powerview data, send to Andrew T. Smith, Josh Bushkofsky, and Richard Arnold at this point. *

If the UC is not responding to an SSH request or ping request, then the UC is down. Send to Andrew T. Smith at this point.


