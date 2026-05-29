from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyResourceBundle"]

class PropertyResourceBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PropertyResourceBundle"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/io/Reader;)V", False)]
    getKeys = JavaMethod("()Ljava/util/Enumeration;")
    handleGetObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")