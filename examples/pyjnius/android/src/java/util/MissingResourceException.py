from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MissingResourceException"]

class MissingResourceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/MissingResourceException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getKey = JavaMethod("()Ljava/lang/String;")
    getClassName = JavaMethod("()Ljava/lang/String;")