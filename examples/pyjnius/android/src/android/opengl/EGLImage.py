from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLImage"]

class EGLImage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLImage"
    equals = JavaMethod("(Ljava/lang/Object;)Z")