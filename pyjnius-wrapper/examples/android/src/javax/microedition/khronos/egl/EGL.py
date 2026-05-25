from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGL"]

class EGL(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGL"