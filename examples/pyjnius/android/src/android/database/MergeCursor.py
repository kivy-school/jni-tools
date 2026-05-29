from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MergeCursor"]

class MergeCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/MergeCursor"
    __javaconstructor__ = [("([Landroid/database/Cursor;)V", False)]
    FIELD_TYPE_BLOB = JavaStaticField("I")
    FIELD_TYPE_FLOAT = JavaStaticField("I")
    FIELD_TYPE_INTEGER = JavaStaticField("I")
    FIELD_TYPE_NULL = JavaStaticField("I")
    FIELD_TYPE_STRING = JavaStaticField("I")
    onMove = JavaMethod("(II)Z")
    getShort = JavaMethod("(I)S")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getFloat = JavaMethod("(I)F")
    getDouble = JavaMethod("(I)D")
    close = JavaMethod("()V")
    getCount = JavaMethod("()I")
    getType = JavaMethod("(I)I")
    deactivate = JavaMethod("()V")
    getBlob = JavaMethod("(I)[B")
    getColumnNames = JavaMethod("()[Ljava/lang/String;")
    registerContentObserver = JavaMethod("(Landroid/database/ContentObserver;)V")
    requery = JavaMethod("()Z")
    unregisterContentObserver = JavaMethod("(Landroid/database/ContentObserver;)V")
    getString = JavaMethod("(I)Ljava/lang/String;")
    registerDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    unregisterDataSetObserver = JavaMethod("(Landroid/database/DataSetObserver;)V")
    isNull = JavaMethod("(I)Z")