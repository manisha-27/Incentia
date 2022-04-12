import cv2

def get_merged_image(img1, img2):
    # img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    dim=(1000,600)
    resized_img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    resized_img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    blend = cv2.addWeighted(resized_img1, 0.6, resized_img2, 0.6, 0.0)
    return blend

