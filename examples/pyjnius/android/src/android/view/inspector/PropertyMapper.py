from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyMapper"]

class PropertyMapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/PropertyMapper"
    mapDouble = JavaMethod("(Ljava/lang/String;I)I")
    mapColor = JavaMethod("(Ljava/lang/String;I)I")
    mapInt = JavaMethod("(Ljava/lang/String;I)I")
    mapGravity = JavaMethod("(Ljava/lang/String;I)I")
    mapByte = JavaMethod("(Ljava/lang/String;I)I")
    mapFloat = JavaMethod("(Ljava/lang/String;I)I")
    mapBoolean = JavaMethod("(Ljava/lang/String;I)I")
    mapIntEnum = JavaMethod("(Ljava/lang/String;ILjava/util/function/IntFunction;)I")
    mapIntFlag = JavaMethod("(Ljava/lang/String;ILjava/util/function/IntFunction;)I")
    mapLong = JavaMethod("(Ljava/lang/String;I)I")
    mapObject = JavaMethod("(Ljava/lang/String;I)I")
    mapResourceId = JavaMethod("(Ljava/lang/String;I)I")
    mapShort = JavaMethod("(Ljava/lang/String;I)I")
    mapChar = JavaMethod("(Ljava/lang/String;I)I")

    class PropertyConflictException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/PropertyMapper$PropertyConflictException"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]