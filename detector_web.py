from flask import Flask
from flask import render_template
from flask import Response
from flask import send_file
import cv2
import mediapipe as mp
import condicionales
from normalizacionCords import obtenerAngulos
import random
app = Flask(__name__, template_folder='templates', static_folder='static')
lectura_actual = 0
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles

#cap = cv2.VideoCapture("Letras/Letra_o.mp4")
cap = cv2.VideoCapture(0)

wCam, hCam = 920, 720
cap.set(3, wCam)
cap.set(4, hCam)
cont =random.randint(0, 1000000)
path = './capture/'
nombreimagen=path + 'IMG_%04d.jpg' % cont

def generate( nombreimagen):
   lectura_actual = 0   
   with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.75) as hands:

    while True:
          ret, frame = cap.read()
          if ret == False:
            break
          height, width, _ = frame.shape
          frame = cv2.flip(frame, 1)
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          results = hands.process(frame_rgb)
          if results.multi_hand_landmarks is not None:
            # Accediendo a los puntos de referencia, de acuerdo a su nombre   
                angulosid = obtenerAngulos(results, width, height)[0]
                pw= obtenerAngulos(results, width, height)[2]
                dedos = []
                # pulgar externo angle
                if angulosid[5] > 125:
                    dedos.append(1)
                else:
                    dedos.append(0)

                # pulgar interno
                if angulosid[4] > 150:
                    dedos.append(1)
                else:
                    dedos.append(0)

                # 4 dedos
                for id in range(0, 4):
                    if angulosid[id] > 90:
                        dedos.append(1)
                    else:
                        dedos.append(0)


                TotalDedos = dedos.count(1)
                res2="nada"
                condicionales.condicionalesLetrasA(dedos, frame,pw,res2)
                etiqueta=condicionales.condicionalesLetrasA(dedos, frame,pw,res2)
                print("Holiii",etiqueta)
                

                pinky = obtenerAngulos(results, width, height)[1]
                pinkY=pinky[1] + pinky[0]   
                resta = pinkY - lectura_actual
                lectura_actual = pinkY
                print("ubi",abs(resta), pinkY, lectura_actual)
                print("Coordenadas", dedos)
                if dedos == [0, 0, 1, 0, 0, 0]:
                    if abs(resta) > 30:
                        print("jota en movimento")
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                        cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
                
        
                if(etiqueta=="A"):
                    if (ret == True):

                        cv2.imwrite(nombreimagen, frame) 
                        print("ENTRAMOOOO")
                        #cap.release()
                        if (cv2.waitKey(1) == ord('s')):
                            break
                    else:
                        break
                #testing--------------------------------------
                # print(dedos)
                # print("meñique:", angle1, "anular:", angle2, "medio:", angle3,
                #       "indice:", angle4, "pulgar 1:", angle5, "pulgar 2:", angle6)
                # print (angle1, angle2, angle3, angle4, angle5, angle6)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
          ret, buffer = cv2.imencode('.jpg', frame)
          frame = buffer.tobytes()
          yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/")
def index():
     return render_template('index.html')
@app.route('/menu')
def menu():

    return render_template('menu.html') 
@app.route('/letraA')
def letraA():
    return render_template('letraA.html') 
@app.route('/monitoreo')
def monitoreo():
    return render_template('monitoreo.html') 
@app.route('/encabezado')
def encabezado():
    return render_template('encabezado.html') 

@app.route("/video_feed")
def video_feed():
     return Response(generate(nombreimagen),
          mimetype = "multipart/x-mixed-replace; boundary=frame")
@app.route('/download')
def Download_File():
    print(nombreimagen)
    return send_file(nombreimagen,as_attachment=True)

if __name__ == "__main__":
     app.run(debug=True)

cap.release()