#!/bin/sh
ps -ef | grep crawl | awk {'print $2'} | xargs kill -9
