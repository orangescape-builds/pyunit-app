#!/usr/bin/env bash

find . -name "test_*.py" -print | while read f; do
        echo "$f"
        ###
        python3 -m coverage run "$f"
        python3 -m coverage xml -o coverage.xml
        ###
done

#cp -r ./coverage.xml /var/lib/jenkins/workspace/pyunit/coverage.xml
#cp -r ./python_unittests_xml /var/lib/jenkins/workspace/pyunit/python_unittests_xml