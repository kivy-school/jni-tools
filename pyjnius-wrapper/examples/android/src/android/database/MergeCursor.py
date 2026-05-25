from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MergeCursor"]

class MergeCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/MergeCursor"
    __javaconstructor__ = [("([Landroid/database/Cursor;)V", False)]
    getCount = JavaMethod("()I")
    onMove = JavaMethod("(II)Z")
    getString = JavaMethod("(I)Ljava/lang/String;")
    getShort = JavaMethod("(I)S")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getFloat = JavaMethod("(I)F")
    getDouble = JavaMethod("(I)D")
    getType = JavaMethod("(I)I")
    isNull = JavaMethod("(I)Z")
    getBlob = JavaMethod("(I)[B")
    getColumnNames = JavaMethod("()[Ljava/lang/String;")
    deactivate = JavaMethod("()V")
    close = JavaMethod("()V")
    registerContentObserver = JavaMethod("(Landroid/database/ContentObserver;)V")
    unregisterContentObserver = JavaMethod("(Landroid/database/ContentObserver;)V")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    requery = JavaMethod("()Z")