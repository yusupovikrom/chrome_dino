from PIL import ImageGrab
import pyautogui
import sys
import os

if sys.platform in ['win32', 'win64', 'windows']:
    import pygetwindow as gw
    #Get the list of windows title
    windows = gw.getAllTitles()
    #Get dino window info
    #Get window name using hard code
    dino_win ='Google Chrome chrome://dino/'
    x1,y1,width,height = gw.getWindowGeometry(dino_win)
    x2 = x1 + width
    y2 = y1 + height
    #Define the dino bbox
    dino_bbox = (x1,y1,x2,y2)
    #Get the screen shot of dino window
    dino_screen = ImageGrab.grab(bbox=dino_bbox)
    #Save the screen shot
    dino_screen.save('dino_screen.png')

elif sys.platform in ['linux', 'linux2']:
    try:
        import pgi
        pgi.require_version('Wnck', '3.0')
        from pgi.repository import Wnck
    except:
        print('Please install Wnck')
        Wnck = None
    if Wnck is not None:
        screen = Wnck.Screen.get_default()
        screen.force_update()
        windows = screen.get_windows()
        for window in windows:
            if window.get_name() == 'chrome://dino/ - Google Chrome':
                x1,y1,width,height = window.get_geometry()
                x2 = x1 + width
                y2 = y1 + height
                dino_bbox = (x1,y1,x2,y2)
                dino_screen = ImageGrab.grab(bbox=dino_bbox)
                image = f'screen_idx.png'
                dino_screen.save(image)
                # os.remove(image)
                break