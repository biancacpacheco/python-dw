#!/bin/bash

echo -e "\n\n"
echo -e "=======================================" 
echo -e "========TESTING DESING WIZARD==========" 
echo -e "=======================================" 

python2 -m tests.unit.test_design_wizard
#python3 -m tests.unit.test_design_wizard

echo -e "\n\n"
echo -e "=======================================" 
echo -e "============TESTING ENTITY=============" 
echo -e "=======================================" 

python2 -m tests.unit.test_entity
#python3 -m tests.unit.test_entity

echo -e "\n\n"
echo -e "=======================================" 
echo -e "===========TESTING RELATION============" 
echo -e "=======================================" 

python2 -m tests.unit.test_relation
#python3 -m tests.unit.test_relation


find . -name "__pycache__" -type d -exec rm -r "{}" \; 2> /dev/null
find . -name "*.pyc" -type f -delete
