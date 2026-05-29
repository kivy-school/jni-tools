from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGL"]

class EGL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGL"