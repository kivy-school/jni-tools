from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLSurface"]

class EGLSurface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGLSurface"
    __javaconstructor__ = [("()V", False)]