#
# Copyright 2011 Twitter, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Example demonstrating the use of predefined subassemblies.

The data is expected in the pycascading_data/ folder if run in local mode,
and in the pycascading_data/ folder in the user's HDFS home if run with Hadoop. 
"""

from pycascading.helpers import *


def main():
    flow = Flow()
    repeats = flow.source(Hfs(TextDelimited(Fields(['col1', 'col2']), ' ',
                                            [String, Integer]),
                              'pycascading_data/repeats.txt'))
    output = flow.tsv_sink('pycascading_data/out')

    # This selects the distinct records considering all fields
    repeats | SubAssembly(Unique, Fields.ALL) | output

    flow.run()
