from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLException"]

class GLException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLException"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/lang/String;)V", False)]