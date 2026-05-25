from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MalformedParameterizedTypeException"]

class MalformedParameterizedTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/MalformedParameterizedTypeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]