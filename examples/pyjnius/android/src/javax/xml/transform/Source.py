from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Source"]

class Source(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Source"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    isEmpty = JavaMethod("()Z")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")