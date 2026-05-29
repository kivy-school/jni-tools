from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractWindowedCursor"]

class AbstractWindowedCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/AbstractWindowedCursor"
    __javaconstructor__ = [("()V", False)]
    mWindow = JavaField("Landroid/database/CursorWindow;")
    getBlob = JavaMethod("(I)[B")
    getString = JavaMethod("(I)Ljava/lang/String;")
    copyStringToBuffer = JavaMethod("(ILandroid/database/CharArrayBuffer;)V")
    getShort = JavaMethod("(I)S")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getFloat = JavaMethod("(I)F")
    getDouble = JavaMethod("(I)D")
    isNull = JavaMethod("(I)Z")
    isBlob = JavaMethod("(I)Z")
    isString = JavaMethod("(I)Z")
    isLong = JavaMethod("(I)Z")
    isFloat = JavaMethod("(I)Z")
    getType = JavaMethod("(I)I")
    checkPosition = JavaMethod("()V")
    getWindow = JavaMethod("()Landroid/database/CursorWindow;")
    setWindow = JavaMethod("(Landroid/database/CursorWindow;)V")
    hasWindow = JavaMethod("()Z")