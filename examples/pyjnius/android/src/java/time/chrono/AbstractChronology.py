from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractChronology"]

class AbstractChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/AbstractChronology"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/time/chrono/Chronology;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;")