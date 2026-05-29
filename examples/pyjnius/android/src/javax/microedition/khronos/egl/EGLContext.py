from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLContext"]

class EGLContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGLContext"
    __javaconstructor__ = [("()V", False)]
    getEGL = JavaStaticMethod("()Ljavax/microedition/khronos/egl/EGL;")
    getGL = JavaMethod("()Ljavax/microedition/khronos/opengles/GL;")