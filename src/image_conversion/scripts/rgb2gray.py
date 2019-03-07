#!/usr/bin/env python
#encoding: utf8

import rospy, cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class Conversion():

    def __init__(self):
	self.pub = rospy.Publisher("/cv_camera/image_gray", Image, queue_size=1)
        self.sub = rospy.Subscriber("/cv_camera/image_raw", Image, self.callback)
        self.bridge = CvBridge()

    def callback(self, img):
        try:
            img_cv2 = self.bridge.imgmsg_to_cv2(img, "bgr8")
	    gimg = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
	    gimg_ros = self.bridge.cv2_to_imgmsg(gimg, "mono8")
	    self.pub.publish(gimg_ros)
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == "__main__":
    rospy.init_node("bgr8_gray")
    Con = Conversion()

    try:
	rospy.spin()
    except KeyboardInterrupt:
	print("Shutting down.")
