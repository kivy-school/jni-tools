from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuoteMode"]

class QuoteMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/commons/csv/QuoteMode"
    ALL = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    ALL_NON_NULL = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    MINIMAL = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    NON_NUMERIC = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    NONE = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    values = JavaStaticMethod("()[Lorg/apache/commons/csv/QuoteMode;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lorg/apache/commons/csv/QuoteMode;")
    ALL = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    ALL_NON_NULL = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    MINIMAL = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    NON_NUMERIC = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")
    NONE = JavaStaticField("Lorg/apache/commons/csv/QuoteMode;")