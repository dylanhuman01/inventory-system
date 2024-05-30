import cv2
from pyzbar.pyzbar import decode
import requests

def scan_barcode():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            barcode = obj.data.decode('utf-8')
            print(f'Scanned Barcode: {barcode}')
            response = requests.post('http://127.0.0.1:5000/scan', data={'barcode': barcode})
            if response.status_code == 200:
                item_data = response.json()
                print(f"Item Name: {item_data['name']}")
                print(f"Description: {item_data['description']}")
                print(f"Category: {item_data['category']}")
                print(f"Serial Number: {item_data['serial_number']}")
                print(f"Purchase Date: {item_data['purchase_date']}")
                print(f"Warranty Expiry: {item_data['warranty_expiry']}")
                print(f"Location: {item_data['location']}")
                print(f"Status: {item_data['status']}")
            else:
                print('Item not found.')

        cv2.imshow('Barcode Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_barcode()

