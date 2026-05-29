from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextStyle"]

class TextStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/TextStyle"
    FULL = JavaStaticField("Ljava/time/format/TextStyle;")
    FULL_STANDALONE = JavaStaticField("Ljava/time/format/TextStyle;")
    SHORT = JavaStaticField("Ljava/time/format/TextStyle;")
    SHORT_STANDALONE = JavaStaticField("Ljava/time/format/TextStyle;")
    NARROW = JavaStaticField("Ljava/time/format/TextStyle;")
    NARROW_STANDALONE = JavaStaticField("Ljava/time/format/TextStyle;")
    values = JavaStaticMethod("()[Ljava/time/format/TextStyle;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/format/TextStyle;")
    isStandalone = JavaMethod("()Z")
    asStandalone = JavaMethod("()Ljava/time/format/TextStyle;")
    asNormal = JavaMethod("()Ljava/time/format/TextStyle;")
    FULL = JavaStaticField("Ljava/time/format/TextStyle;")
    FULL_STANDALONE = JavaStaticField("Ljava/time/format/TextStyle;")
    SHORT = JavaStaticField("Ljava/time/format/TextStyle;")
    SHORT_STANDALONE = JavaStaticField("Ljava/time/format/TextStyle;")
    NARROW = JavaStaticField("Ljava/time/format/TextStyle;")
    NARROW_STANDALONE = JavaStaticField("Ljava/time/format/TextStyle;")