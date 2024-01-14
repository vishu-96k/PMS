#final with adding state  

import cv2
import easyocr

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

plate_cascade = cv2.CascadeClassifier(harcascade)

# Specify the language you want to use for OCR
reader = easyocr.Reader(['en'])

while True:
    success, img = cap.read()

    if not success:
        print("Failed to capture image")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        if 'img_roi' in locals():
            cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1

            # Use EasyOCR to extract text from the saved image
            result = reader.readtext("plates/scaned_img_" + str(count - 1) + ".jpg")

            # Print only the extracted number
            if result:
                number = result[0][1]  # Assuming the first result contains the license plate number
                print("License Plate Number:", number)

                # Check if the license plate number starts with "MH"
                if number.startswith("Mh"):
                    print("State: Maharashtra")

                if number.startswith("MH"):
                    print("State: Maharashtra")

                if number.startswith("mh"):
                    print("State: Maharashtra")

                if number.startswith("mH"):
                    print("State: Maharashtra")

                if number.startswith("ka"):
                    print("State: karnataka")

                if number.startswith("Ka"):
                    print("State: karnataka")

                if number.startswith("kA"):
                    print("State: karnataka")

                if number.startswith("KA"):
                    print("State: karnataka")
                
                else:
                    print("State: Unknown")
            else:
                print("No license plate number detected.")

        else:
            print("No plate detected. Cannot save image.")

    elif key == 27:  # Press 'Esc' key to exit the loop
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
