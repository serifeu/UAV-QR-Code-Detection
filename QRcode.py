import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)  # Kamera açma
cap.set(4, 400)  # Çözünürlük 

while True:
    success, img = cap.read()  

    # QR kodlarını çözme
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')  # Veriyi çöz
        print(f"Okunan QR Kod: {myData}")  # Okunan veriyi yazdır

        #  kare 
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 5)

        #  yazı 
        (x, y, w, h) = barcode.rect
        cv2.putText(img, myData, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow("QR Kod Okuma", img)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
