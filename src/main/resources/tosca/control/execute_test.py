#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from tosca.core.client import ToscaClient

def process(task_vars):

    client = ToscaClient.new_instance(task_vars['server'])

    results = client.execute(task_vars['result_type'], task_vars['polling_interval'], task_vars['client_timeout'], task_vars['consider_execution_result'], task_vars['test_configuration'])

    print "Done"

    print "The results are ", results

    print "Running testResultsPassed"
    testResultsPassed(results, task_vars['test_configuration'])

    return results

def testResultsPassed(results, consider_execution_result):
    print "in testResultsPassed"


if __name__ == '__main__' or __name__ == '__builtin__':
    test_results = process(locals())
