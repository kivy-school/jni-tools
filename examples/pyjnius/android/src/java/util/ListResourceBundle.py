from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListResourceBundle"]

class ListResourceBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ListResourceBundle"
    __javaconstructor__ = [("()V", False)]
    getKeys = JavaMethod("()Ljava/util/Enumeration;")
    handleGetObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")