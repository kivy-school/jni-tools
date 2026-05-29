from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLObjectHandle"]

class EGLObjectHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLObjectHandle"
    __javaconstructor__ = [("(I)V", False), ("(J)V", False)]
    getHandle = JavaMethod("()I")
    getNativeHandle = JavaMethod("()J")
    hashCode = JavaMethod("()I")