from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeUtils"]

class TimeUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/TimeUtils"
    isTimeBetween = JavaStaticMethod("(Ljava/time/LocalTime;Ljava/time/LocalTime;Ljava/time/LocalTime;)Z")
    getTimeZoneDatabaseVersion = JavaStaticMethod("()Ljava/lang/String;")
    getTimeZoneIdsForCountryCode = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/List;")
    getTimeZone = JavaStaticMethod("(IZJLjava/lang/String;)Ljava/util/TimeZone;")