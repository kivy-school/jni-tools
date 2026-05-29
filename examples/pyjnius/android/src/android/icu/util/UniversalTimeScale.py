from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UniversalTimeScale"]

class UniversalTimeScale(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/UniversalTimeScale"
    DB2_TIME = JavaStaticField("I")
    DOTNET_DATE_TIME = JavaStaticField("I")
    EPOCH_OFFSET_PLUS_1_VALUE = JavaStaticField("I")
    EPOCH_OFFSET_VALUE = JavaStaticField("I")
    EXCEL_TIME = JavaStaticField("I")
    FROM_MAX_VALUE = JavaStaticField("I")
    FROM_MIN_VALUE = JavaStaticField("I")
    ICU4C_TIME = JavaStaticField("I")
    JAVA_TIME = JavaStaticField("I")
    MAC_OLD_TIME = JavaStaticField("I")
    MAC_TIME = JavaStaticField("I")
    MAX_SCALE = JavaStaticField("I")
    TO_MAX_VALUE = JavaStaticField("I")
    TO_MIN_VALUE = JavaStaticField("I")
    UNITS_VALUE = JavaStaticField("I")
    UNIX_MICROSECONDS_TIME = JavaStaticField("I")
    UNIX_TIME = JavaStaticField("I")
    WINDOWS_FILE_TIME = JavaStaticField("I")
    bigDecimalFrom = JavaMultipleMethod([("(DI)Landroid/icu/math/BigDecimal;", True, False), ("(Landroid/icu/math/BigDecimal;I)Landroid/icu/math/BigDecimal;", True, False), ("(JI)Landroid/icu/math/BigDecimal;", True, False)])
    getTimeScaleValue = JavaStaticMethod("(II)J")
    toBigDecimal = JavaMultipleMethod([("(JI)Landroid/icu/math/BigDecimal;", True, False), ("(Landroid/icu/math/BigDecimal;I)Landroid/icu/math/BigDecimal;", True, False)])
    toLong = JavaStaticMethod("(JI)J")
    from = JavaStaticMethod("(JI)J")