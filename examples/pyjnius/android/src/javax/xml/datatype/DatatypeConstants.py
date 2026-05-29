from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatatypeConstants"]

class DatatypeConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/DatatypeConstants"
    JANUARY = JavaStaticField("I")
    FEBRUARY = JavaStaticField("I")
    MARCH = JavaStaticField("I")
    APRIL = JavaStaticField("I")
    MAY = JavaStaticField("I")
    JUNE = JavaStaticField("I")
    JULY = JavaStaticField("I")
    AUGUST = JavaStaticField("I")
    SEPTEMBER = JavaStaticField("I")
    OCTOBER = JavaStaticField("I")
    NOVEMBER = JavaStaticField("I")
    DECEMBER = JavaStaticField("I")
    LESSER = JavaStaticField("I")
    EQUAL = JavaStaticField("I")
    GREATER = JavaStaticField("I")
    INDETERMINATE = JavaStaticField("I")
    FIELD_UNDEFINED = JavaStaticField("I")
    YEARS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    MONTHS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    DAYS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    HOURS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    MINUTES = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    SECONDS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    DATETIME = JavaStaticField("Ljavax/xml/namespace/QName;")
    TIME = JavaStaticField("Ljavax/xml/namespace/QName;")
    DATE = JavaStaticField("Ljavax/xml/namespace/QName;")
    GYEARMONTH = JavaStaticField("Ljavax/xml/namespace/QName;")
    GMONTHDAY = JavaStaticField("Ljavax/xml/namespace/QName;")
    GYEAR = JavaStaticField("Ljavax/xml/namespace/QName;")
    GMONTH = JavaStaticField("Ljavax/xml/namespace/QName;")
    GDAY = JavaStaticField("Ljavax/xml/namespace/QName;")
    DURATION = JavaStaticField("Ljavax/xml/namespace/QName;")
    DURATION_DAYTIME = JavaStaticField("Ljavax/xml/namespace/QName;")
    DURATION_YEARMONTH = JavaStaticField("Ljavax/xml/namespace/QName;")
    MAX_TIMEZONE_OFFSET = JavaStaticField("I")
    MIN_TIMEZONE_OFFSET = JavaStaticField("I")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/xml/datatype/DatatypeConstants$Field"
        toString = JavaMethod("()Ljava/lang/String;")
        getId = JavaMethod("()I")