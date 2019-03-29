import numpy as np
import cv2
def run_main():
    img = cv2.imread('/home/wad/homeWork/computerVisionClass/HomeWork1/image4.JPG',0)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    # img = cv2.medianBlur(img,55)
    img = cv2.bilateralFilter(img,25,100,100)
    img = cv2.medianBlur(img,5)
    
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,0.9,120,param1=50,param2=30,minRadius=100,maxRadius=180)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),18)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),1)

    cv2.imshow('detected circles',cimg)
    cv2.imshow('detected circles',img)
    cv2.imwrite('/home/wad/homeWork/computerVisionClass/HomeWork1/image4Hasil.JPG',cimg)
    cv2.imwrite('/home/wad/homeWork/computerVisionClass/HomeWork1/image1sadsadsadHasil.JPG',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#     roi = cv2.imread('/home/wad/homeWork/computerVisionClass/HomeWork1/image3.JPG')
#     roi = roi[1000:3000,800:2700]
#     gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     gray_blur = cv2.GaussianBlur(gray, (17, 17), 0)
#     thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                        cv2.THRESH_BINARY_INV, 17,5)
#     kernel = np.ones((3, 3), np.uint8)
#     closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=100)
#     cont_img = closing.copy()
#     im2,contours, _ = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         # if area < 2000 or area > 4000:
#             # continue
#         if len(cnt) < 5:
#             continue
#         ellipse = cv2.fitEllipse(cnt)
#         cv2.ellipse(roi, ellipse, (255,0,0), 2)
#     cv2.imshow("Morphological Closing", closing)
#     cv2.imshow("Adaptive Thresholding", thresh)
#     # cv2.imshow('Contours', roi)
#     cv2.imwrite('/home/wad/homeWork/computerVisionClass/HomeWork1/image3Hasil.JPG',roi)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Rhys Dunn - 2015
# # Learning image vision/OpenCV


# # import libraries


#     # load image
#     img = cv2.imread("/home/wad/homeWork/computerVisionClass/HomeWork1/image3.JPG")


#     # prep image - blur and convert to grey scale
#     grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(grey, (5, 5), 0)
#     cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # show blurred image and grey scaled image
#     cv2.imshow("grey scale", grey)
#     cv2.imshow("blurred", blurred)
#     cv2.waitKey(0)
#     img2 = cv2.imread("/home/wad/homeWork/computerVisionClass/HomeWork1/image3.JPG",0)
#     img2 = cv2.medianBlur(img2,5)
#     cimg = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
#     # canny edge detector
#     outline = cv2.Canny(blurred, 10, 150,10)
#     circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)

#     circles = np.uint16(np.around(circles))
#     for i in circles[0,:]:
#     # draw the outer circle
#         cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#         # draw the center of the circle
#         cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

#     # show canny edge detector
#     cv2.imshow('detected circles',cimg)

#     cv2.imshow("The edges", outline)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     # find the contours
#     _,cnts, _ = cv2.findContours(outline, cv2.RETR_EXTERNAL,
#                 cv2.CHAIN_APPROX_SIMPLE)


#     # draw contours: -1 will draw all contours
#     cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
#     cv2.imshow("Result", img)
#     cv2.imwrite('/home/wad/homeWork/computerVisionClass/HomeWork1/image3Hasil2.JPG',img)
#     cv2.waitKey(0)


#     # Print how many coins we found
#     print("I found %i coins" % len(cnts))

if __name__ == "__main__":
    run_main()
