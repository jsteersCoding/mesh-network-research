#!/bin/bash
iw dev mesh0 mesh leave
iw dev mesh0 mesh join ACTI_MESH beacon-interval 10
iw dev wlan0 set txpower fixed 1dBm
