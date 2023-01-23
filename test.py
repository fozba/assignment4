#/usr/bin/env python
#
# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import subprocess

class TestSolution(unittest.TestCase):
    
    def clean_parse(self, lines):

        clean_lines = [ line.split() for line in lines.split('\n') ]

        return clean_lines

    def test_parse1(self):

        result = subprocess.run(['bash', 'parse1.sh'], stdout=subprocess.PIPE)
        lines = result.stdout.decode('utf-8')

        clean_lines = self.clean_parse(lines)

        assert ['1.473248', '2.027327'] in clean_lines
        assert ['2.027327', '1.473248'] in clean_lines
        

    def test_parse2(self):

        result = subprocess.run(['bash', 'parse2.sh'], stdout=subprocess.PIPE)
        lines = result.stdout.decode('utf-8')

        clean_lines = self.clean_parse(lines)

        assert ['1.473248', '2.027327'] in clean_lines
        

if __name__ == '__main__':
    unittest.main()
