from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSRuntimeException"]

class RSRuntimeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/RSRuntimeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]