from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLSurface"]

class EGLSurface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLSurface"
    equals = JavaMethod("(Ljava/lang/Object;)Z")