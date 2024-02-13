#!/usr/bin/env bash


rsync -avc  * $IGNITE_DEST:ignite/
ssh $IGNITE_DEST "rsync -avh ignite/* /opt/ignite/ --delete-excluded"

