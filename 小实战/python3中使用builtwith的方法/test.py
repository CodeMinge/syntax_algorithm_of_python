#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import builtwith

tech_used = builtwith.parse('http://www.163.com')
print(tech_used)

tech_used = builtwith.parse('http://www.baidu.com')
print(tech_used)