from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLObjectHandle"]

class EGLObjectHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLObjectHandle"
    getNativeHandle = JavaMethod("()J")
    hashCode = JavaMethod("()I")
    getHandle = JavaMethod("()I")