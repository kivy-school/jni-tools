from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidPropertiesFormatException"]

class InvalidPropertiesFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/InvalidPropertiesFormatException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False)]