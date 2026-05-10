import cv2 

image = cv2.imread(r'C:\Users\Bhavya garg\OneDrive\Desktop\Ai\cat.jpg')

# cv2.namedWindow('Win1',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Win1', 500,500)

# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(f'Image details : {image.shape}')

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

resize = cv2.resize(gray_img, (240,250))

cv2.imshow('Image', gray_img)
key = cv2.waitKey(0)

if key == ord('g'):
    cv2.imwrite('Img.jpg',resize)
    print("Image saved successfully!")
else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f'Image details: {resize.shape}')

