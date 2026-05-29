from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLSync"]

class EGLSync(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLSync"
    equals = JavaMethod("(Ljava/lang/Object;)Z")