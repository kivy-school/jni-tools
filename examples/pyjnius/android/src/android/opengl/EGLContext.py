from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLContext"]

class EGLContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLContext"
    equals = JavaMethod("(Ljava/lang/Object;)Z")