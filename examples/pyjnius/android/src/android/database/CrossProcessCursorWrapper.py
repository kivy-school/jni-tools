from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CrossProcessCursorWrapper"]

class CrossProcessCursorWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CrossProcessCursorWrapper"
    __javaconstructor__ = [("(Landroid/database/Cursor;)V", False)]
    FIELD_TYPE_BLOB = JavaStaticField("I")
    FIELD_TYPE_FLOAT = JavaStaticField("I")
    FIELD_TYPE_INTEGER = JavaStaticField("I")
    FIELD_TYPE_NULL = JavaStaticField("I")
    FIELD_TYPE_STRING = JavaStaticField("I")
    onMove = JavaMethod("(II)Z")
    fillWindow = JavaMethod("(ILandroid/database/CursorWindow;)V")
    getWindow = JavaMethod("()Landroid/database/CursorWindow;")