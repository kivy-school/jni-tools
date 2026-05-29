from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormatStyle"]

class FormatStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/FormatStyle"
    FULL = JavaStaticField("Ljava/time/format/FormatStyle;")
    LONG = JavaStaticField("Ljava/time/format/FormatStyle;")
    MEDIUM = JavaStaticField("Ljava/time/format/FormatStyle;")
    SHORT = JavaStaticField("Ljava/time/format/FormatStyle;")
    values = JavaStaticMethod("()[Ljava/time/format/FormatStyle;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/format/FormatStyle;")
    FULL = JavaStaticField("Ljava/time/format/FormatStyle;")
    LONG = JavaStaticField("Ljava/time/format/FormatStyle;")
    MEDIUM = JavaStaticField("Ljava/time/format/FormatStyle;")
    SHORT = JavaStaticField("Ljava/time/format/FormatStyle;")