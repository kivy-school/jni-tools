from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Duration"]

class Duration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/Duration"
    __javaconstructor__ = [("()V", False)]
    getSign = JavaMethod("()I")
    subtract = JavaMethod("(Ljavax/xml/datatype/Duration;)Ljavax/xml/datatype/Duration;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compare = JavaMethod("(Ljavax/xml/datatype/Duration;)I")
    add = JavaMethod("(Ljavax/xml/datatype/Duration;)Ljavax/xml/datatype/Duration;")
    getField = JavaMethod("(Ljavax/xml/datatype/DatatypeConstants$Field;)Ljava/lang/Number;")
    negate = JavaMethod("()Ljavax/xml/datatype/Duration;")
    multiply = JavaMultipleMethod([("(I)Ljavax/xml/datatype/Duration;", False, False), ("(Ljava/math/BigDecimal;)Ljavax/xml/datatype/Duration;", False, False)])
    getXMLSchemaType = JavaMethod("()Ljavax/xml/namespace/QName;")
    normalizeWith = JavaMethod("(Ljava/util/Calendar;)Ljavax/xml/datatype/Duration;")
    isLongerThan = JavaMethod("(Ljavax/xml/datatype/Duration;)Z")
    isShorterThan = JavaMethod("(Ljavax/xml/datatype/Duration;)Z")
    getHours = JavaMethod("()I")
    getMinutes = JavaMethod("()I")
    getTimeInMillis = JavaMultipleMethod([("(Ljava/util/Calendar;)J", False, False), ("(Ljava/util/Date;)J", False, False)])
    isSet = JavaMethod("(Ljavax/xml/datatype/DatatypeConstants$Field;)Z")
    addTo = JavaMultipleMethod([("(Ljava/util/Date;)V", False, False), ("(Ljava/util/Calendar;)V", False, False)])
    getYears = JavaMethod("()I")
    getMonths = JavaMethod("()I")
    getDays = JavaMethod("()I")
    getSeconds = JavaMethod("()I")