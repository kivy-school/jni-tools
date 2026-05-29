from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatatypeConstants"]

class DatatypeConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/DatatypeConstants"
    APRIL = JavaStaticField("I")
    AUGUST = JavaStaticField("I")
    DATE = JavaStaticField("Ljavax/xml/namespace/QName;")
    DATETIME = JavaStaticField("Ljavax/xml/namespace/QName;")
    DAYS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    DECEMBER = JavaStaticField("I")
    DURATION = JavaStaticField("Ljavax/xml/namespace/QName;")
    DURATION_DAYTIME = JavaStaticField("Ljavax/xml/namespace/QName;")
    DURATION_YEARMONTH = JavaStaticField("Ljavax/xml/namespace/QName;")
    EQUAL = JavaStaticField("I")
    FEBRUARY = JavaStaticField("I")
    FIELD_UNDEFINED = JavaStaticField("I")
    GDAY = JavaStaticField("Ljavax/xml/namespace/QName;")
    GMONTH = JavaStaticField("Ljavax/xml/namespace/QName;")
    GMONTHDAY = JavaStaticField("Ljavax/xml/namespace/QName;")
    GREATER = JavaStaticField("I")
    GYEAR = JavaStaticField("Ljavax/xml/namespace/QName;")
    GYEARMONTH = JavaStaticField("Ljavax/xml/namespace/QName;")
    HOURS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    INDETERMINATE = JavaStaticField("I")
    JANUARY = JavaStaticField("I")
    JULY = JavaStaticField("I")
    JUNE = JavaStaticField("I")
    LESSER = JavaStaticField("I")
    MARCH = JavaStaticField("I")
    MAX_TIMEZONE_OFFSET = JavaStaticField("I")
    MAY = JavaStaticField("I")
    MINUTES = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    MIN_TIMEZONE_OFFSET = JavaStaticField("I")
    MONTHS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    NOVEMBER = JavaStaticField("I")
    OCTOBER = JavaStaticField("I")
    SECONDS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")
    SEPTEMBER = JavaStaticField("I")
    TIME = JavaStaticField("Ljavax/xml/namespace/QName;")
    YEARS = JavaStaticField("Ljavax/xml/datatype/DatatypeConstants$Field;")

    class Field(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/xml/datatype/DatatypeConstants/Field"
        toString = JavaMethod("()Ljava/lang/String;")
        getId = JavaMethod("()I")