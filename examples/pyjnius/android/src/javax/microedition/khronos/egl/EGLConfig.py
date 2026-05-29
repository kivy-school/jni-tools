from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLConfig"]

class EGLConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGLConfig"
    __javaconstructor__ = [("()V", False)]