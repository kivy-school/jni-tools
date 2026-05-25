from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeUtils"]

class TimeUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/TimeUtils"
    getTimeZone = JavaStaticMethod("(IZJLjava/lang/String;)Ljava/util/TimeZone;")
    getTimeZoneIdsForCountryCode = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/List;")
    getTimeZoneDatabaseVersion = JavaStaticMethod("()Ljava/lang/String;")
    isTimeBetween = JavaStaticMethod("(Ljava/time/LocalTime;Ljava/time/LocalTime;Ljava/time/LocalTime;)Z")