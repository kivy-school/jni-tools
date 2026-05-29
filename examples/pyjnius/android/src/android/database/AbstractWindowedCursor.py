from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractWindowedCursor"]

class AbstractWindowedCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/AbstractWindowedCursor"
    __javaconstructor__ = [("()V", False)]
    FIELD_TYPE_BLOB = JavaStaticField("I")
    FIELD_TYPE_FLOAT = JavaStaticField("I")
    FIELD_TYPE_INTEGER = JavaStaticField("I")
    FIELD_TYPE_NULL = JavaStaticField("I")
    FIELD_TYPE_STRING = JavaStaticField("I")
    setWindow = JavaMethod("(Landroid/database/CursorWindow;)V")
    hasWindow = JavaMethod("()Z")
    isBlob = JavaMethod("(I)Z")
    isLong = JavaMethod("(I)Z")
    getShort = JavaMethod("(I)S")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getFloat = JavaMethod("(I)F")
    getDouble = JavaMethod("(I)D")
    getType = JavaMethod("(I)I")
    copyStringToBuffer = JavaMethod("(ILandroid/database/CharArrayBuffer;)V")
    getBlob = JavaMethod("(I)[B")
    getWindow = JavaMethod("()Landroid/database/CursorWindow;")
    isFloat = JavaMethod("(I)Z")
    isString = JavaMethod("(I)Z")
    getString = JavaMethod("(I)Ljava/lang/String;")
    isNull = JavaMethod("(I)Z")