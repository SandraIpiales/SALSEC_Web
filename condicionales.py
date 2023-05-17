import cv2

def condicionalesLetras(dedos, frame,pw,res2):
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    print("holii",pw)
    """if dedos == [1, 1, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
            res2="A"
            cv2.putText(frame, 'A exito', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Imagen Capturada', (50, 100), font, 3, (0, 0, 0), 2, cv2.LINE_AA)

            print("A mov")
            return res2"""
            

    if dedos == [0, 0, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'E', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("E")

    if dedos == [0, 0, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'I', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("I")

    if dedos == [1, 1, 1, 0, 0, 1]:

            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'O', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)

            print("O")

    if dedos == [0, 0, 1, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'U', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("U")

    # abecedario
    if dedos == [0, 0, 1, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'B', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("B")
    if dedos ==[1,0,1,0,0,0]:
             cv2.rectangle(frame,(0,0),(100,100),(255,255,255), -1)
             cv2.putText(frame,'C',(20,80),font,3,(0,0,0),2,cv2.LINE_AA)
             print("C")
    if dedos == [0, 0, 0, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'D', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("D")
    if dedos == [1, 1, 0, 0, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'K', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("K")
    if dedos == [1, 1, 0, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'L', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("L")
    if dedos == [0, 1, 0, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'W', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("W")
    if dedos == [0, 1, 0, 0, 1, 1]:
            print("PP",pw)
            if pw <190:
                cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
                cv2.putText(frame, 'N', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
                print("N")
            else:
                cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                cv2.putText(frame, 'V', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
                print("V")
    if dedos == [1, 1, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'Y', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("Y")
    if dedos == [1, 1, 1, 1, 1, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'F', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("F")
    if dedos == [0, 1, 1, 1, 1, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'P', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("P")

    if dedos == [0, 0, 1, 1, 1, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'T', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("T")

def condicionalesLetrasA(dedos, frame,pw,res2):
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    print("holii",pw)
    if dedos == [1, 1, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
            res2="A"
            cv2.putText(frame, 'A exito', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Imagen Capturada', (50, 100), font, 3, (0, 0, 0), 2, cv2.LINE_AA)

            print("A mov")
            return res2