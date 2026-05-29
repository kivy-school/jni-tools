from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyReader"]

class PropertyReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/PropertyReader"
    readColor = JavaMultipleMethod([("(II)V", False, False), ("(IJ)V", False, False), ("(ILandroid/graphics/Color;)V", False, False)])
    readGravity = JavaMethod("(II)V")
    readIntEnum = JavaMethod("(II)V")
    readIntFlag = JavaMethod("(II)V")
    readResourceId = JavaMethod("(II)V")
    readObject = JavaMethod("(ILjava/lang/Object;)V")
    readInt = JavaMethod("(II)V")
    readChar = JavaMethod("(IC)V")
    readFloat = JavaMethod("(IF)V")
    readLong = JavaMethod("(IJ)V")
    readByte = JavaMethod("(IB)V")
    readShort = JavaMethod("(IS)V")
    readBoolean = JavaMethod("(IZ)V")
    readDouble = JavaMethod("(ID)V")

    class PropertyTypeMismatchException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/PropertyReader$PropertyTypeMismatchException"
        __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]