from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeZoneNames"]

class TimeZoneNames(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/TimeZoneNames"
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/text/TimeZoneNames;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/TimeZoneNames;", True, False)])
    getTZDBInstance = JavaStaticMethod("(Landroid/icu/util/ULocale;)Landroid/icu/text/TimeZoneNames;")
    getAvailableMetaZoneIDs = JavaMultipleMethod([("()Ljava/util/Set;", False, False), ("(Ljava/lang/String;)Ljava/util/Set;", False, False)])
    getMetaZoneID = JavaMethod("(Ljava/lang/String;J)Ljava/lang/String;")
    getReferenceZoneID = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getMetaZoneDisplayName = JavaMethod("(Ljava/lang/String;Landroid/icu/text/TimeZoneNames$NameType;)Ljava/lang/String;")
    getDisplayName = JavaMethod("(Ljava/lang/String;Landroid/icu/text/TimeZoneNames$NameType;J)Ljava/lang/String;")
    getTimeZoneDisplayName = JavaMethod("(Ljava/lang/String;Landroid/icu/text/TimeZoneNames$NameType;)Ljava/lang/String;")
    getExemplarLocationName = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")

    class NameType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/TimeZoneNames/NameType"
        values = JavaStaticMethod("()[Landroid/icu/text/TimeZoneNames$NameType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/TimeZoneNames$NameType;")
        LONG_GENERIC = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")
        LONG_STANDARD = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")
        LONG_DAYLIGHT = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")
        SHORT_GENERIC = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")
        SHORT_STANDARD = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")
        SHORT_DAYLIGHT = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")
        EXEMPLAR_LOCATION = JavaStaticField("Landroid/icu/text/TimeZoneNames/NameType;")