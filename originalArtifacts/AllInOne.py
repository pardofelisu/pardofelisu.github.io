#code that ensures OpenGL, and other dependencies are downloaded
#if not, initiates installation process
import sys
import subprocess


try:
    try:
        import OpenGL
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyOpenGL', 'PyOpenGL_accelerate'])
        import OpenGL
        

        #insures GLFW is installed
    try:
        import glfw
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'glfw'])
        import glfw

    #insures numpy is installed
    try:
        import numpy
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
        import numpy        


    #checks for glew installation
    try:
        import glew
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyglew'])
        import glew

except Exception as e:
    print(f"An error occurred while installing dependencies: {e}")
    sys.exit(1)