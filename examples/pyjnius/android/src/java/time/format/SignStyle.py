from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignStyle"]

class SignStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/SignStyle"
    NORMAL = JavaStaticField("Ljava/time/format/SignStyle;")
    ALWAYS = JavaStaticField("Ljava/time/format/SignStyle;")
    NEVER = JavaStaticField("Ljava/time/format/SignStyle;")
    NOT_NEGATIVE = JavaStaticField("Ljava/time/format/SignStyle;")
    EXCEEDS_PAD = JavaStaticField("Ljava/time/format/SignStyle;")
    values = JavaStaticMethod("()[Ljava/time/format/SignStyle;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/format/SignStyle;")
    NORMAL = JavaStaticField("Ljava/time/format/SignStyle;")
    ALWAYS = JavaStaticField("Ljava/time/format/SignStyle;")
    NEVER = JavaStaticField("Ljava/time/format/SignStyle;")
    NOT_NEGATIVE = JavaStaticField("Ljava/time/format/SignStyle;")
    EXCEEDS_PAD = JavaStaticField("Ljava/time/format/SignStyle;")