from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MatrixCursor"]

class MatrixCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/MatrixCursor"
    __javaconstructor__ = [("([Ljava/lang/String;)V", False), ("([Ljava/lang/String;I)V", False)]
    FIELD_TYPE_BLOB = JavaStaticField("I")
    FIELD_TYPE_FLOAT = JavaStaticField("I")
    FIELD_TYPE_INTEGER = JavaStaticField("I")
    FIELD_TYPE_NULL = JavaStaticField("I")
    FIELD_TYPE_STRING = JavaStaticField("I")
    addRow = JavaMultipleMethod([("([Ljava/lang/Object;)V", False, False), ("(Ljava/lang/Iterable;)V", False, False)])
    newRow = JavaMethod("()Landroid/database/MatrixCursor$RowBuilder;")
    getShort = JavaMethod("(I)S")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getFloat = JavaMethod("(I)F")
    getDouble = JavaMethod("(I)D")
    getCount = JavaMethod("()I")
    getType = JavaMethod("(I)I")
    getBlob = JavaMethod("(I)[B")
    getColumnNames = JavaMethod("()[Ljava/lang/String;")
    getString = JavaMethod("(I)Ljava/lang/String;")
    isNull = JavaMethod("(I)Z")

    class RowBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/database/MatrixCursor$RowBuilder"
        add = JavaMultipleMethod([("(Ljava/lang/Object;)Landroid/database/MatrixCursor$RowBuilder;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)Landroid/database/MatrixCursor$RowBuilder;", False, False)])