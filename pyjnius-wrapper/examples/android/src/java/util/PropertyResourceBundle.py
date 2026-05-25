from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyResourceBundle"]

class PropertyResourceBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PropertyResourceBundle"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/Reader;)V", False)]
    handleGetObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getKeys = JavaMethod("()Ljava/util/Enumeration;")
    handleKeySet = JavaMethod("()Ljava/util/Set;")