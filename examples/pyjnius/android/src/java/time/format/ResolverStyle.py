from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResolverStyle"]

class ResolverStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/ResolverStyle"
    STRICT = JavaStaticField("Ljava/time/format/ResolverStyle;")
    SMART = JavaStaticField("Ljava/time/format/ResolverStyle;")
    LENIENT = JavaStaticField("Ljava/time/format/ResolverStyle;")
    values = JavaStaticMethod("()[Ljava/time/format/ResolverStyle;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/format/ResolverStyle;")
    STRICT = JavaStaticField("Ljava/time/format/ResolverStyle;")
    SMART = JavaStaticField("Ljava/time/format/ResolverStyle;")
    LENIENT = JavaStaticField("Ljava/time/format/ResolverStyle;")