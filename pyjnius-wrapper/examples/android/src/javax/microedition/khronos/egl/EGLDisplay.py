from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLDisplay"]

class EGLDisplay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGLDisplay"
    __javaconstructor__ = [("()V", False)]