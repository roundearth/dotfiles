#!/bin/bash

if [ $(dunstctl is-paused) = false ]; then
	dunstctl set-paused true
else
	dunstctl set-paused false
fi
