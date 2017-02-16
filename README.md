# CMPE-273

What is psutil?

psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network) in Python.
Requirements

This Code does the following:
 - Uses psutil and implements a network socket monitoring tool that can check how many TCP sockets are being created by a web application.
 - Lists all processes that have any socket connections (meaning the laddr and raddr fields exist).
 - Groups by the PID and sort the output by the number of the connections per process.
