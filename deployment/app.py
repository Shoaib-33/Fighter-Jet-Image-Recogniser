from fastai.vision.all import *
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath
import pathlib
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

cap_labels = ['AIDC F-CK-1 Ching-kuo', 'Boeing F-15EX Eagle II', 'Chengdu J-10 (China)', 'Chengdu J-20 (China)', 'Dassault Rafale', 'English Electric Lightning', 'Eurofighter Typhoon', 'Focke-Wulf Fw 190', 'General Dynamics F-16 Fighting Falcon aircraft', 'Grumman F-14 Tomcat', 'KAI KF-21 Boramae', 'Lockheed Martin F-22 Raptor', 'Lockheed Martin F-35 Lightning II', 'Lockheed P-80 Shooting Star', 'Lockheed YF-12', 'McDonnell Douglas F-4 Phantom II', 'Mikoyan MiG-29', 'Mikoyan Mig-31', 'Mikoyan-Gurevich MiG-25', 'Shenyang FC-31 Gyrfalcon', 'Sukhoi Su-27', 'Sukhoi Su-35 (Russia)', 'Sukhoi Su-57']


model = load_learner('latest.pkl')

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(cap_labels, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'images/euro.jpg',
    'images/F-16.jpg',
    'images/mig-31.jpg',
    'images/su57.jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)