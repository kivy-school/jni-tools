from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatatypeFactory"]

class DatatypeFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/datatype/DatatypeFactory"
    __javaconstructor__ = [("()V", False)]
    DATATYPEFACTORY_IMPLEMENTATION_CLASS = JavaStaticField("Ljava/lang/String;")
    DATATYPEFACTORY_PROPERTY = JavaStaticField("Ljava/lang/String;")
    newInstance = JavaMultipleMethod([("()Ljavax/xml/datatype/DatatypeFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/datatype/DatatypeFactory;", True, False)])
    newDuration = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/xml/datatype/Duration;", False, False), ("(J)Ljavax/xml/datatype/Duration;", False, False), ("(ZLjava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigDecimal;)Ljavax/xml/datatype/Duration;", False, False), ("(ZIIIIII)Ljavax/xml/datatype/Duration;", False, False)])
    newDurationDayTime = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/xml/datatype/Duration;", False, False), ("(J)Ljavax/xml/datatype/Duration;", False, False), ("(ZLjava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)Ljavax/xml/datatype/Duration;", False, False), ("(ZIIII)Ljavax/xml/datatype/Duration;", False, False)])
    newDurationYearMonth = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/xml/datatype/Duration;", False, False), ("(J)Ljavax/xml/datatype/Duration;", False, False), ("(ZLjava/math/BigInteger;Ljava/math/BigInteger;)Ljavax/xml/datatype/Duration;", False, False), ("(ZII)Ljavax/xml/datatype/Duration;", False, False)])
    newXMLGregorianCalendar = JavaMultipleMethod([("()Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(Ljava/lang/String;)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(Ljava/util/GregorianCalendar;)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(Ljava/math/BigInteger;IIIIILjava/math/BigDecimal;I)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(IIIIIIII)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False)])
    newXMLGregorianCalendarDate = JavaMethod("(IIII)Ljavax/xml/datatype/XMLGregorianCalendar;")
    newXMLGregorianCalendarTime = JavaMultipleMethod([("(IIII)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(IIILjava/math/BigDecimal;I)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False), ("(IIIII)Ljavax/xml/datatype/XMLGregorianCalendar;", False, False)])