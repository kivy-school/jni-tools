from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CrossProcessCursorWrapper"]

class CrossProcessCursorWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CrossProcessCursorWrapper"
    __javaconstructor__ = [("(Landroid/database/Cursor;)V", False)]
    fillWindow = JavaMethod("(ILandroid/database/CursorWindow;)V")
    getWindow = JavaMethod("()Landroid/database/CursorWindow;")
    onMove = JavaMethod("(II)Z")