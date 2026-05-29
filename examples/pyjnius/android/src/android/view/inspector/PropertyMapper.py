from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyMapper"]

class PropertyMapper(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/PropertyMapper"
    mapBoolean = JavaMethod("(Ljava/lang/String;I)I")
    mapByte = JavaMethod("(Ljava/lang/String;I)I")
    mapChar = JavaMethod("(Ljava/lang/String;I)I")
    mapDouble = JavaMethod("(Ljava/lang/String;I)I")
    mapFloat = JavaMethod("(Ljava/lang/String;I)I")
    mapInt = JavaMethod("(Ljava/lang/String;I)I")
    mapLong = JavaMethod("(Ljava/lang/String;I)I")
    mapShort = JavaMethod("(Ljava/lang/String;I)I")
    mapObject = JavaMethod("(Ljava/lang/String;I)I")
    mapColor = JavaMethod("(Ljava/lang/String;I)I")
    mapGravity = JavaMethod("(Ljava/lang/String;I)I")
    mapIntEnum = JavaMethod("(Ljava/lang/String;ILjava/util/function/IntFunction;)I")
    mapResourceId = JavaMethod("(Ljava/lang/String;I)I")
    mapIntFlag = JavaMethod("(Ljava/lang/String;ILjava/util/function/IntFunction;)I")

    class PropertyConflictException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/PropertyMapper/PropertyConflictException"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]