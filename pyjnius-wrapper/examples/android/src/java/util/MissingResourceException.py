from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MissingResourceException"]

class MissingResourceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/MissingResourceException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getClassName = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()Ljava/lang/String;")