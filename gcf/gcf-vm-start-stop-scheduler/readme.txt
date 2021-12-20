In this lab, we create two cloud functions 

start-vm and 
stop-vm 

We use a cloud scheduler to run once every 3 hours to stop the vm by calling the stop-vm gcf 

Permissions required:
=====================

There are 2 permissions involved here: 
svcaccount-1: "Runtime Service Account" - this is the the svc ac permissions assumed by the gcf as its identity
               to do what it needs to do.

svcaccount-2: "Permissions" - this is who can invoke the stop-vm gcf 


svcaccount-1: name: sa-cf-vm-start-stop assign role: Compute Instance Admin v1 
svcaccount-2: name: sa-cf-invoker assign role: Cloud Functions Invoker

Pre-requisites:
===============
Create a vm manually first called cf-vm in singapore region here:
'gcp-pse-335012', zone='asia-southeast1-b', instance='cf-vm')
