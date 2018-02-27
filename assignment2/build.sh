#!/bin/env bash
mvn -e clean compile assembly:single
mvn package
rm -rf ./output1
