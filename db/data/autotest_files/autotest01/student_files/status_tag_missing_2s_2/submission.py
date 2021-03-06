#!/usr/bin/env python

"""
This student submission file is used to test the autotester
It represents the test case where:

  The xml is missing a <status> tag in the second script
  which should not affect the test in the first script
"""
import sys
import os
import json

if os.path.basename(sys.argv[1]) == 'autotest_02.sh':
  print(json.dumps({'name': 'status_missing_bad_test', 'input': 'NA', 'expected': 'NA', 'actual': 'NA', 'marks_earned': 2, 'marks_total': 2}))
else:
  print(json.dumps({'name': 'status_missing_good_test', 'input': 'NA', 'expected': 'NA', 'actual': 'NA', 'marks_earned': 2, 'marks_total': 2, 'status': 'pass'}))
