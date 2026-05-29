from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoneId"]

class ZoneId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/ZoneId"
    SHORT_IDS = JavaStaticField("Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Map;)Ljava/time/ZoneId;", True, False), ("(Ljava/lang/String;)Ljava/time/ZoneId;", True, False)])
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/ZoneId;")
    getId = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    normalized = JavaMethod("()Ljava/time/ZoneId;")
    getAvailableZoneIds = JavaStaticMethod("()Ljava/util/Set;")
    ofOffset = JavaStaticMethod("(Ljava/lang/String;Ljava/time/ZoneOffset;)Ljava/time/ZoneId;")
    systemDefault = JavaStaticMethod("()Ljava/time/ZoneId;")
    getRules = JavaMethod("()Ljava/time/zone/ZoneRules;")