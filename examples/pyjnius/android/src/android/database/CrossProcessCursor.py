from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CrossProcessCursor"]

class CrossProcessCursor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CrossProcessCursor"
    getWindow = JavaMethod("()Landroid/database/CursorWindow;")
    fillWindow = JavaMethod("(ILandroid/database/CursorWindow;)V")
    onMove = JavaMethod("(II)Z")