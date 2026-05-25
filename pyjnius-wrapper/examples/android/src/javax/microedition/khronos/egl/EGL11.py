from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGL11"]

class EGL11(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/egl/EGL11"
    EGL_CONTEXT_LOST = JavaStaticField("I")