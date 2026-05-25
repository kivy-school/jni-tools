from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyReader"]

class PropertyReader(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/PropertyReader"
    readBoolean = JavaMethod("(IZ)V")
    readByte = JavaMethod("(IB)V")
    readChar = JavaMethod("(IC)V")
    readDouble = JavaMethod("(ID)V")
    readFloat = JavaMethod("(IF)V")
    readInt = JavaMethod("(II)V")
    readLong = JavaMethod("(IJ)V")
    readShort = JavaMethod("(IS)V")
    readObject = JavaMethod("(ILjava/lang/Object;)V")
    readColor = JavaMultipleMethod([("(II)V", False, False), ("(IJ)V", False, False), ("(ILandroid/graphics/Color;)V", False, False)])
    readGravity = JavaMethod("(II)V")
    readIntEnum = JavaMethod("(II)V")
    readIntFlag = JavaMethod("(II)V")
    readResourceId = JavaMethod("(II)V")

    class PropertyTypeMismatchException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/PropertyReader/PropertyTypeMismatchException"
        __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/String;)V", False)]