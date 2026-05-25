from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Source"]

class Source(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Source"
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")