# Pi_Digital_Signage
Project to make Raspis into easy to use digital signage platforms

## Plan/Thoughts

### App
Single App for all roles
Images vs Videos vs mixed
OMXPlayer on Pi Zero, VLC on everything else. FFPlay?
Transcode on local node, then send transcoded video
Minimise transcoding
Web interface
Web API for sync/ main UI Pi to client Pis
Discovery of other nodes
Play off of USB with config file - autogenerate
OSD for progress before playback begins
Output Rotation

### Networking

Mesh?
WiFi AP
Join existing network
Internet enabled management

### Install

script to install on Pis/ Raspi and other linux
SD image for flashing?
Power tolerance: read only sections?

### Other

Windows compatibility
Multi display output compatibility
Video Rotation

## Procedure

Build play/transcode pipeline
Build USB direct playback - Prioritise videos over pictures
Build single device web UI
Build multidevice APIs/ discovery/ UI
Build sync functionality
Build internet enabled control - remote server?
