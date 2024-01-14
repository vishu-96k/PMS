
#final with adding state and time and date with excel sheet

import cv2
import easyocr
from datetime import datetime
import pandas as pd
from datetime import datetime



harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

plate_cascade = cv2.CascadeClassifier(harcascade)

# Specify the language you want to use for OCR
reader = easyocr.Reader(['en'])

# Define a dictionary to map state codes to state names
state_mapping = {
    'MH': 'Maharashtra',
    'mH': 'Maharashtra',
    'Mh': 'Maharashtra',
    'mh': 'Maharashtra',
    'KA': 'Karnataka',
    'Ka': 'Karnataka',
    'kA': 'Karnataka',
    'ka': 'Karnataka',
    'DL': 'DELHI',
    'Dl': 'DELHI',
    'dL': 'DELHI',
    'DL': 'DELHI',
    'AP': 'Andhra Pradesh',
    'aP': 'Andhra Pradesh',
    'Ap': 'Andhra Pradesh',
    'ap': 'Andhra Pradesh',
    'AR': 'Arunachal Pradesh',
    'aR': 'Arunachal Pradesh',
    'Ar': 'Arunachal Pradesh',
    'ar': 'Arunachal Pradesh',
    'AS': 'Assam',
    'aS': 'Assam',
    'As': 'Assam',
    'as': 'Assam',
    'BR': 'Bihar',
    'bR': 'Bihar',
    'Br': 'Bihar',
    'br': 'Bihar',
    'CT': 'Chhattisgarh',
    'cT': 'Chhattisgarh',
    'Ct': 'Chhattisgarh',
    'ct': 'Chhattisgarh',
    'GA': 'Goa',
    'gA': 'Goa',
    'Ga': 'Goa',
    'ga': 'Goa',
    'GJ': 'Gujarat',
    'gJ': 'Gujarat',
    'Gj': 'Gujarat',
    'gj': 'Gujarat',
    'HR': 'Haryana',
    'hR': 'Haryana',
    'Hr': 'Haryana',
    'hr': 'Haryana',
    'HP': 'Himachal Pradesh',
    'hP': 'Himachal Pradesh',
    'Hp': 'Himachal Pradesh',
    'hp': 'Himachal Pradesh',
    'JH': 'Jharkhand',
    'jH': 'Jharkhand',
    'Jh': 'Jharkhand',
    'jh': 'Jharkhand',
    'KA': 'Karnataka',
    'kA': 'Karnataka',
    'Ka': 'Karnataka',
    'ka': 'Karnataka',
    'KL': 'Kerala',
    'kL': 'Kerala',
    'Kl': 'Kerala',
    'kl': 'Kerala',
    'MP': 'Madhya Pradesh',
    'mP': 'Madhya Pradesh',
    'Mp': 'Madhya Pradesh',
    'mp': 'Madhya Pradesh',
    'MH': 'Maharashtra',
    'mH': 'Maharashtra',
    'Mh': 'Maharashtra',
    'mh': 'Maharashtra',
    'MN': 'Manipur',
    'mN': 'Manipur',
    'Mn': 'Manipur',
    'mn': 'Manipur',
    'ML': 'Meghalaya',
    'mL': 'Meghalaya',
    'Ml': 'Meghalaya',
    'ml': 'Meghalaya',
    'MZ': 'Mizoram',
    'mZ': 'Mizoram',
    'Mz': 'Mizoram',
    'mz': 'Mizoram',
    'NL': 'Nagaland',
    'nL': 'Nagaland',
    'Nl': 'Nagaland',
    'nl': 'Nagaland',
    'OR': 'Odisha',
    'oR': 'Odisha',
    'Or': 'Odisha',
    'or': 'Odisha',
    'PB': 'Punjab',
    'pB': 'Punjab',
    'Pb': 'Punjab',
    'pb': 'Punjab',
    'RJ': 'Rajasthan',
    'rJ': 'Rajasthan',
    'Rj': 'Rajasthan',
    'rj': 'Rajasthan',
    'SK': 'Sikkim',
    'sK': 'Sikkim',
    'Sk': 'Sikkim',
    'sk': 'Sikkim',
    'TN': 'Tamil Nadu',
    'tN': 'Tamil Nadu',
    'Tn': 'Tamil Nadu',
    'tn': 'Tamil Nadu',
    'TG': 'Telangana',
    'tG': 'Telangana',
    'Tg': 'Telangana',
    'tg': 'Telangana',
    'TR': 'Tripura',
    'tR': 'Tripura',
    'Tr': 'Tripura',
    'tr': 'Tripura',
    'UP': 'Uttar Pradesh',
    'uP': 'Uttar Pradesh',
    'Up': 'Uttar Pradesh',
    'up': 'Uttar Pradesh',
    'UK': 'Uttarakhand',
    'uK': 'Uttarakhand',
    'Uk': 'Uttarakhand',
    'uk': 'Uttarakhand',
    'WB': 'West Bengal',
    'wB': 'West Bengal',
    'Wb': 'West Bengal',
    'wb': 'West Bengal',
    'AN': 'Andaman and Nicobar Islands',
    'aN': 'Andaman and Nicobar Islands',
    'An': 'Andaman and Nicobar Islands',
    'an': 'Andaman and Nicobar Islands',
    'CH': 'Chandigarh',
    'cH': 'Chandigarh',
    'Ch': 'Chandigarh',
    'ch': 'Chandigarh',
    'DN': 'Dadra and Nagar Haveli and Daman and Diu',
    'dN': 'Dadra and Nagar Haveli and Daman and Diu',
    'Dn': 'Dadra and Nagar Haveli and Daman and Diu',
    'dn': 'Dadra and Nagar Haveli and Daman and Diu',
    'DL': 'Delhi',
    'dL': 'Delhi',
    'Dl': 'Delhi',
    'dl': 'Delhi',
    'JK': 'Jammu and Kashmir',
    'jK': 'Jammu and Kashmir',
    'Jk': 'Jammu and Kashmir',
    'jk': 'Jammu and Kashmir',
    'LA': 'Ladakh',
    'lA': 'Ladakh',
    'La': 'Ladakh',
    'la': 'Ladakh',
    'LD': 'Lakshadweep',
    'lD': 'Lakshadweep',
    'Ld': 'Lakshadweep',
    'ld': 'Lakshadweep',
    'PY': 'Puducherry',
    'pY': 'Puducherry',
    'Py': 'Puducherry',
    'py': 'Puducherry',

    # Add more state codes as needed
}

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

            # Print license plate number, state, date, and time
            if result:
                number = result[0][1]  # Assuming the first result contains the license plate number
                print("License Plate Number:", number)

                # Check if the license plate number starts with a state code
                state_code = number[:2]
                if state_code in state_mapping:
                    state_name = state_mapping[state_code]
                    print("State:", state_name)
                else:
                    print("State: Unknown")

                # Get current date and time
                current_datetime = datetime.now()
                formatted_date = current_datetime.strftime("%d %m %Y")
                formatted_time = current_datetime.strftime("%I:%M:%S %p")
                print("Date:", formatted_date)
                print("Time:", formatted_time)

            else:
                print("No license plate number detected.")

        else:
            print("No plate detected. Cannot save image.")

    elif key == 27:  # Press 'Esc' key to exit the loop
        break


# Sample result data
result_data = {
    'state': state_name,
    'number': number
}

# Get the current date and time
current_datetime = datetime.now()

# Create a DataFrame with the result data
df = pd.DataFrame({
    'date': [current_datetime.strftime("%d %m %Y")],
    'time': [current_datetime.strftime("%I:%M:%S %p")],
    'state': [result_data['state']],
    'number': [result_data['number']]
})

# Try to read the existing Excel file, if it exists
try:
    existing_df = pd.read_excel('NUMBER_PLATE.xlsx')
    # Append the new data to the existing DataFrame
    df = pd.concat([existing_df, df], ignore_index=True)
except FileNotFoundError:
    # If the file doesn't exist, create a new DataFrame
    pass

# Write the DataFrame to the Excel file
df.to_excel('NUMBER_PLATE.xlsx', index=False)

print("Data added to Excel sheet successfully.")


# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
