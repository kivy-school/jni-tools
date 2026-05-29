from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MalformedParametersException"]

class MalformedParametersException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/MalformedParametersException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]