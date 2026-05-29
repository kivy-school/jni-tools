from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListResourceBundle"]

class ListResourceBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ListResourceBundle"
    __javaconstructor__ = [("()V", False)]
    handleGetObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getKeys = JavaMethod("()Ljava/util/Enumeration;")
    handleKeySet = JavaMethod("()Ljava/util/Set;")
    getContents = JavaMethod("()[[Ljava/lang/Object;")