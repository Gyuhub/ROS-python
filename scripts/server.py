#!/usr/bin/env python
from __future__ import print_function

from python_test.srv import PythonTest, PythonTestResponse
import rospy

def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]" %(req.a, req.b, (req.a + req.b)))
    return PythonTestResponse(req.a + req.b)

def server():
    rospy.init_node("server")
    s = rospy.Service("add_two_ints", PythonTest, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == '__main__':
    server()