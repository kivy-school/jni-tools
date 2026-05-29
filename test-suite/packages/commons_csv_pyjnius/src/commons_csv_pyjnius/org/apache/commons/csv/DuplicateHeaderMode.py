from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DuplicateHeaderMode"]

class DuplicateHeaderMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/commons/csv/DuplicateHeaderMode"
    ALLOW_ALL = JavaStaticField("Lorg/apache/commons/csv/DuplicateHeaderMode;")
    ALLOW_EMPTY = JavaStaticField("Lorg/apache/commons/csv/DuplicateHeaderMode;")
    DISALLOW = JavaStaticField("Lorg/apache/commons/csv/DuplicateHeaderMode;")
    values = JavaStaticMethod("()[Lorg/apache/commons/csv/DuplicateHeaderMode;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lorg/apache/commons/csv/DuplicateHeaderMode;")
    ALLOW_ALL = JavaStaticField("Lorg/apache/commons/csv/DuplicateHeaderMode;")
    ALLOW_EMPTY = JavaStaticField("Lorg/apache/commons/csv/DuplicateHeaderMode;")
    DISALLOW = JavaStaticField("Lorg/apache/commons/csv/DuplicateHeaderMode;")