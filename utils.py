import cv2

def overlay(background,foreground):
	# normalize alpha channels from 0-255 to 0-1
	alpha_background = background[:,:,3] / 255.0
	alpha_foreground = foreground[:,:,3] / 255.0

	# set adjusted colors
	for color in range(0, 3):
		background[:,:,color] = alpha_foreground * foreground[:,:,color] + \
			alpha_background * background[:,:,color] * (1 - alpha_foreground)

	# set adjusted alpha and denormalize back to 0-255
	background[:,:,3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255

	return background


def generate_image(img_2_save,k,iter):
	print(f"Processing {k+1}/{iter} image")
	try:
		background = img_2_save[0]
		for index in range(1,len(img_2_save)):
			background = overlay(background,img_2_save[index])

		name_nfts = f"image_{k+1}"
		cv2.imwrite(f"./images/{name_nfts}.png", background)

	except Exception as e:
		print("Error", e)