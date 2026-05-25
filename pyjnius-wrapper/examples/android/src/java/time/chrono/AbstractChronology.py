from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractChronology"]

class AbstractChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/AbstractChronology"
    __javaconstructor__ = [("()V", False)]
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;")
    compareTo = JavaMethod("(Ljava/time/chrono/Chronology;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")