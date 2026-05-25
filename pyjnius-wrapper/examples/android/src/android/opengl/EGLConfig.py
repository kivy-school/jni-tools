from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLConfig"]

class EGLConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLConfig"
    equals = JavaMethod("(Ljava/lang/Object;)Z")