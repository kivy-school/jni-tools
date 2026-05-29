from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatatypeFactory"]

class DatatypeFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/DatatypeFactory"
    DATATYPEFACTORY_PROPERTY = JavaStaticField("Ljava/lang/String;")
    DATATYPEFACTORY_IMPLEMENTATION_CLASS = JavaStaticField("Ljava/lang/String;")
    newInstance = JavaMultipleMethod([("()Ljavax/xml/datatype/DatatypeFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/datatype/DatatypeFactory;", True, False)])
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/datatype/DatatypeFactory;")
    newDuration = JavaMultipleMethod([("(ZIIIIII)Ljavax/xml/datatype/Duration;", False, False), ("(ZLjava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigDecimal;)Ljavax/xml/datatype/Duration;", False, False), ("(J)Ljavax/xml/datatype/Duration;", False, False), ("(Ljava/lang/String;)Ljavax/xml/datatype/Duration;", False, False)])
    newDurationDayTime = JavaMultipleMethod([("(ZLjava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)Ljavax/xml/datatype/Duration;", False, False), ("(ZIIII)Ljavax/xml/datatype/Duration;", False, False), ("(Ljava/lang/String;)Ljavax/xml/datatype/Duration;", False, False), ("(J)Ljavax/xml/datatype/Duration;", False, False)])
    newDurationYearMonth = JavaMultipleMethod([("(J)Ljavax/xml/datatype/Duration;", False, False), ("(ZII)Ljavax/xml/datatype/Duration;", False, False), ("(Ljava/lang/String;)Ljavax/xml/datatype/Duration;", False, False), ("(ZLjava/math/BigInteger;Ljava/math/BigInteger;)Ljavax/xml/datatype/Duration;", False, False)])
    newXMLGregorianCalendar = JavaMultipleMethod([("(IIIIIIII)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(Ljava/math/BigInteger;IIIIILjava/math/BigDecimal;I)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("()Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(Ljava/lang/String;)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(Ljava/util/GregorianCalendar;)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False)])
    newXMLGregorianCalendarTime = JavaMultipleMethod([("(IIIII)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(IIILjava/math/BigDecimal;I)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(IIII)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False)])
    newXMLGregorianCalendarDate = JavaMethod("(IIII)Ljavax/xml/datatype/XMLGregorianCalendar;")