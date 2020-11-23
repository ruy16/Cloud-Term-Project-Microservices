#!/bin/bash
set -mx

/entrypoint.sh &

/dockerstartup/vnc_startup.sh

fg %1