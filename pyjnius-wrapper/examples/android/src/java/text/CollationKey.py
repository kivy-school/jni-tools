from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationKey"]

class CollationKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/CollationKey"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    compareTo = JavaMethod("(Ljava/text/CollationKey;)I")
    getSourceString = JavaMethod("()Ljava/lang/String;")
    toByteArray = JavaMethod("()[B")