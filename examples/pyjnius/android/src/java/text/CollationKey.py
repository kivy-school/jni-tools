from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationKey"]

class CollationKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/CollationKey"
    getSourceString = JavaMethod("()Ljava/lang/String;")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/text/CollationKey;)I", False, False)])
    toByteArray = JavaMethod("()[B")