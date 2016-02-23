#!/bin/bash
a[0]=$(pgrep $1)
echo ${a[0]}
