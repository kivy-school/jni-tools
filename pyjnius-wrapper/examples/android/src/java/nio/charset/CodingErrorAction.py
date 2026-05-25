from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CodingErrorAction"]

class CodingErrorAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CodingErrorAction"
    IGNORE = JavaStaticField("Ljava/nio/charset/CodingErrorAction;")
    REPLACE = JavaStaticField("Ljava/nio/charset/CodingErrorAction;")
    REPORT = JavaStaticField("Ljava/nio/charset/CodingErrorAction;")
    toString = JavaMethod("()Ljava/lang/String;")