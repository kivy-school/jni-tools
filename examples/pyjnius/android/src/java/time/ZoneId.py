from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneId"]

class ZoneId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/ZoneId"
    SHORT_IDS = JavaStaticField("Ljava/util/Map;")
    systemDefault = JavaStaticMethod("()Ljava/time/ZoneId;")
    getAvailableZoneIds = JavaStaticMethod("()Ljava/util/Set;")
    of = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Map;)Ljava/time/ZoneId;", True, False), ("(Ljava/lang/String;)Ljava/time/ZoneId;", True, False)])
    ofOffset = JavaStaticMethod("(Ljava/lang/String;Ljava/time/ZoneOffset;)Ljava/time/ZoneId;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/ZoneId;")
    getId = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    getRules = JavaMethod("()Ljava/time/zone/ZoneRules;")
    normalized = JavaMethod("()Ljava/time/ZoneId;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")