import cv2
import numpy as np
import restore as re
import fprint as fp
import secret as sc
import random
import tester as te

#This program is the main driver for the project.  It tests the image, fingerprint image functionalities
#display menu
print("\n\n\n\t\t\t\tFinal Project")

print("\n1. Test Secret Sharing on Image\n2. Test biometric encryption/decryption on dataset")

#prompt user for input to test functionality, loop until a valid selection
selection = input("\n\nPlease select an option or press q to quit:")
while selection != '1' and selection !='2' and selection !='3' and selection!='q':
	selection = input("\n\nPlease select an option or press q to quit:")

#quit and close the application
if (selection == 'q'):
	print("Thank you.")
	

	
#if 1, 2 or 3 are selected		
else:
	selection = int(selection)
	print("\n\nYou have selected %d" % selection)

	#image test functionality
	if selection == 1:
		print("\nRunning Secret Sharing on Image Tests")
		#begin image tests
		#get a valid filename
		fname = input("Please enter a filename: ")
		fname = "../DATA/pictures/" + fname
		print(fname)
		img = cv2.imread(fname)
		
		while isinstance(img, np.ndarray) == False:
			print("Error.  Not a valid filename.")
			fname =  input("Please enter a valid filename: ")
			fname = "../DATA/pictures/" + fname
			img = cv2.imread(fname)

		#get value for t
		t = input("Please enter an int value for parameter t: ")
		while isinstance(t,int) == False:
			try:
				t = int(t)

			except ValueError:
				t = input("Please enter a valid value for parameter t: ")
				continue
			if t < 1:
				t = input("Please enter a value greater than or equal to 1: ")
						
		#get value for n
		n = input("Please enter an int value for parameter n: ")
		while isinstance(n,int) == False:
			try:
				n = int(n)
			except ValueError:
				n = input("Please enter a valid value for parameter n: ")
				continue
			if t > n:
				n = input("Please enter a value greater than or equal to t: ")

		#run secret sharing on image
		te.image_test(fname,t,n)

		#begin image restoration
		print("Restoring an image.")
		pictures = []
		key = []
		command = input("Enter the filename of a share, 'r' to restore or 'q' to quit:")
		#enter the names of the files you wish to use to restore
		#press r when you have a valid number of images to restore
		#press q if you want to quit
		#loop until r is pressed
		while command != 'r':
			#quit if user inputs q
			if command == 'q':
				break
			else:
				#enter the name of the file and the corresponding key value
				print(command)
				command = "../DATA/pictures/" + command
				image = cv2.imread(command)
				if isinstance(image, np.ndarray):
					pictures.append(command)
					keyval = input("Enter key value of image: ")
					try:
						keyval = int(keyval)
					except ValueError:
						continue
					while isinstance(keyval,int) == False:
						keyval = input("Please enter a correct value:")
						try:
							keyval = int(keyval)
						except ValueError:
							continue
					key.append(keyval)
					command = input("Enter a filename, 'r' to restore or 'q' to quit: ")
				#if file is not an image instance, inform the user
				else:

					while isinstance(image, np.ndarray) == False:
						command = input("Please enter a correct filename or 'q' to quit: ")
						if command == 'q':
							break
						image = cv2.imread(command)
		#begin restoration, throw exception if image can't be restored
		try:
			restored = re.restoreImg(pictures,key)
			restored = np.asarray(restored)
			cv2.imshow("restored", restored)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		except:
			print("Restoration failed")



			

	#test the data encryption on a test set of fingerprints
	#employs a 3,6 secret sharing scheme
	if selection == 2:
		print("\nRunning Biometric encryption/decryption tests on dataset")
		print("Creating 3,6 sharing scheme on thumbprint biometric data.")

		#choose a random image to encrypt
		r1 = random.randint(1,9)
		r2 = random.randint(1,8)
		imstring = "../DATA/DB1_B/10" + str(r1) + "_" + str(r2) + ".tif"

		#show the selected image
		img = cv2.imread(imstring,0)
		
		
		cv2.imshow(imstring,img)
		
		#prepare the data by skeletonization
		skel = fp.prep_data(img)
		
		cv2.imshow('Thinned', skel)
		
		
		#find cornerness points
		corners, keypoints = fp.feature_detect(skel, "Keypoints")
			
		#encrypt the points
		print("Encoding points and writing to \"keypt\" and \"answerkey\" files")
		fp.encrypt_prints(keypoints)

		cv2.waitKey(0)

		#restore the fingerprint points
		print("Getting files.")
		#create the set of files
		filen =[]
		for i in range(0,6):
			filen.append("../DATA/keypt" + str(i) + ".txt")

		print("Restoring Points and writing to file \"decrypted\" ")
		restored = fp.restore_points(filen,len(keypoints))
		#draw circles around restored points
		for i in restored:
			cv2.circle(skel,(i[0],i[1]),5,(255,0,0),1)

		#show image
		cv2.imshow("restored",skel)

		cv2.waitKey(0)
		cv2.destroyAllWindows()


		