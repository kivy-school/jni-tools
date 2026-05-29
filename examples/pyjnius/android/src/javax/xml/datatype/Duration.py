from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Duration"]

class Duration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/Duration"
    __javaconstructor__ = [("()V", False)]
    getXMLSchemaType = JavaMethod("()Ljavax/xml/namespace/QName;")
    getSign = JavaMethod("()I")
    getYears = JavaMethod("()I")
    getMonths = JavaMethod("()I")
    getDays = JavaMethod("()I")
    getHours = JavaMethod("()I")
    getMinutes = JavaMethod("()I")
    getSeconds = JavaMethod("()I")
    getTimeInMillis = JavaMultipleMethod([("(Ljava/util/Calendar;)J", False, False), ("(Ljava/util/Date;)J", False, False)])
    getField = JavaMethod("(Ljavax/xml/datatype/DatatypeConstants$Field;)Ljava/lang/Number;")
    isSet = JavaMethod("(Ljavax/xml/datatype/DatatypeConstants$Field;)Z")
    add = JavaMethod("(Ljavax/xml/datatype/Duration;)Ljavax/xml/datatype/Duration;")
    addTo = JavaMultipleMethod([("(Ljava/util/Calendar;)V", False, False), ("(Ljava/util/Date;)V", False, False)])
    subtract = JavaMethod("(Ljavax/xml/datatype/Duration;)Ljavax/xml/datatype/Duration;")
    multiply = JavaMultipleMethod([("(I)Ljavax/xml/datatype/Duration;", False, False), ("(Ljava/math/BigDecimal;)Ljavax/xml/datatype/Duration;", False, False)])
    negate = JavaMethod("()Ljavax/xml/datatype/Duration;")
    normalizeWith = JavaMethod("(Ljava/util/Calendar;)Ljavax/xml/datatype/Duration;")
    compare = JavaMethod("(Ljavax/xml/datatype/Duration;)I")
    isLongerThan = JavaMethod("(Ljavax/xml/datatype/Duration;)Z")
    isShorterThan = JavaMethod("(Ljavax/xml/datatype/Duration;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")