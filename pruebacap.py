from flask import Flask
from flask import render_template
from flask import Response
import cv2
import mediapipe as mp
import condicionales
from normalizacionCords import obtenerAngulos
import random
app = Flask(__name__, template_folder='templates', static_folder='static')


camara = cv2.VideoCapture(0)

def obtener_frame_camara():
    ok, frame = camara.read()
    if not ok:
        return False, None
    # Codificar la imagen como JPG
    _, bufer = cv2.imencode(".jpg", frame)
    imagen = bufer.tobytes()
    return True, imagen


# Una función generadora para stremear la cámara
# https://flask.palletsprojects.com/en/1.1.x/patterns/streaming/
def generador_frames():
    while True:
        ok, imagen = obtener_frame_camara()
        if not ok:
            break
        else:
            # Regresar la imagen en modo de respuesta HTTP
            yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + imagen + b"\r\n"

# Más tarde...

# Cuando visiten la ruta
@app.route("/streaming_camara")
def streaming_camara():
    return Response(generador_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



# Cuando toman la foto
@app.route("/tomar_foto_descargar")
def descargar_foto():
    ok, frame = obtener_frame_camara()
    if not ok:
        abort(500)
        return
    respuesta = Response(frame)
    respuesta.headers["Content-Type"] = "image/jpeg"
    respuesta.headers["Content-Transfer-Encoding"] = "Binary"
    respuesta.headers["Content-Disposition"] = "attachment; filename=\"foto.jpg\""
    return respuesta



if __name__ == "__main__":
     app.run(debug=True)