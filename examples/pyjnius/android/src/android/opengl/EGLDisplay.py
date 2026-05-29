from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLDisplay"]

class EGLDisplay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLDisplay"
    equals = JavaMethod("(Ljava/lang/Object;)Z")