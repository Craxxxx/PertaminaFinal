from flask import Blueprint, Response
import cv2
# from cctv_login.database_cctv import active_camera
from . import db
# from . import views
from .views import wincamss
import random
import string

# nosignalpath = "no-signal.mp4"

# GENERATE RANDOM STRING 
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.hexdigits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# GENERATE RANDOM STRING


# GENERATE FRAMES
def gen_frames(cam):  # generate frame by frame from camera
    camera = cv2.VideoCapture(cam)
    # print(camera)
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            pass
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
# GENERATE FRAMES


# get the 3x3 cam
playvid3 = Blueprint('playvid3',__name__)
@playvid3.route(f'/{get_random_string(16)}')
def video_feed1():
        # print("test1")
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(wincamss[0]),
            mimetype='multipart/x-mixed-replace; boundary=frame')


@playvid3.route(f'/{get_random_string(16)}')
def video_feed2():
        # print("test2")
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(wincamss[1]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid3.route(f'/{get_random_string(16)}')
def video_feed3():
        # print("test3")
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(wincamss[2]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid3.route(f'/{get_random_string(16)}')
def video_feed4():
        # print("test4")
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(wincamss[3]),
            mimetype='multipart/x-mixed-replace; boundary=frame')
            
@playvid3.route(f'/{get_random_string(16)}')
def video_feed5():
        # print("test5")
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(wincamss[4]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid3.route(f'/{get_random_string(16)}')
def video_feed6():
        # print("test6")
        """Video streaming route. Put this in the src attribute of an img tag."""
        # print("video6")
        return Response(gen_frames(wincamss[5]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid3.route(f'/{get_random_string(16)}')
def video_feed7():
        # print("test7")
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(wincamss[6]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid3.route(f'/{get_random_string(16)}')
def video_feed8():
        # print("test8")
        """Video streaming route. Put this in the src attribute of an img tag."""
        # print("video 8")
        return Response(gen_frames(wincamss[7]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid3.route(f'/{get_random_string(16)}')
def video_feed9():
        # print("test9")
        """Video streaming route. Put this in the src attribute of an img tag."""
        # print("video 9")
        return Response(gen_frames(wincamss[8]),
            mimetype='multipart/x-mixed-replace; boundary=frame')
# get the 3x3 cam


# get the 4x4 cam
# playvid = Blueprint('playvid',__name__)
# @playvid.route(f'/{get_random_string(16)}')
# def video_feed1():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][0]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed2():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][1]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed3():
    
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][2]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed4():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][3]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# playvid = Blueprint('playvid',__name__)
# @playvid.route(f'/{get_random_string(16)}')
# def video_feed1():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][0]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed2():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][1]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed3():
    
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][2]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed4():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][3]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# playvid = Blueprint('playvid',__name__)
# @playvid.route(f'/{get_random_string(16)}')
# def video_feed1():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][0]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed2():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][1]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed3():
    
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][2]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed4():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][3]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# playvid = Blueprint('playvid',__name__)
# @playvid.route(f'/{get_random_string(16)}')
# def video_feed1():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][0]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed2():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][1]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed3():
    
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][2]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')

# @playvid.route(f'/{get_random_string(16)}')
# def video_feed4():
#         """Video streaming route. Put this in the src attribute of an img tag."""
#         return Response(gen_frames(active_camera[3][3]),
#             mimetype='multipart/x-mixed-replace; boundary=frame')
# get the 4x4 cam



