import PySimpleGUI as sg
import os
import shutil
from PIL import Image

folder_path = sg.popup_get_folder('Select the folder containing the images')
if folder_path:
    dest_folder_path = sg.popup_get_folder('Select the destination folder')
    if dest_folder_path:
        categories = [f for f in os.listdir(dest_folder_path) if os.path.isdir(os.path.join(dest_folder_path, f))]
        script_path = os.path.dirname(os.path.abspath(__file__))
        for file in os.listdir(folder_path):
            if file.endswith('.jpg') or file.endswith('.png'):
                if file.endswith('.jpg'):
                    im = Image.open(f'{folder_path}/{file}')
                    width, height = im.size
                    if width > 1000 or height > 1000:
                        im.thumbnail((1000, 1000), Image.LANCZOS)
                    im.save(f'{script_path}/tmp.png')
                    image_path = f'{script_path}/tmp.png'
                else:
                    im = Image.open(f'{folder_path}/{file}')
                    width, height = im.size
                    if width > 1000 or height > 1000:
                        im.thumbnail((1000, 1000), Image.LANCZOS)
                    im.save(f'{script_path}/tmp.png')
                    image_path = f'{script_path}/tmp.png'
                layout = [
                    [sg.Text(file)],
                    [sg.Image(image_path)],
                    [sg.Text('Which category does this image belong to?')],
                    [sg.Combo(categories)],
                    [sg.Button('OK')]
                ]
                window = sg.Window('Image Categorization', layout)
                event, values = window.read()
                window.close()

                category = values[1]
                if category in categories:
                    shutil.move(f'{folder_path}/{file}', f'{dest_folder_path}/{category}/{file}')
                if os.path.exists(f'{script_path}/tmp.png'):
                    os.remove(f'{script_path}/tmp.png')
