from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MatrixCursor"]

class MatrixCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/MatrixCursor"
    __javaconstructor__ = [("([Ljava/lang/String;I)V", False), ("([Ljava/lang/String;)V", False)]
    newRow = JavaMethod("()Landroid/database/MatrixCursor$RowBuilder;")
    addRow = JavaMultipleMethod([("([Ljava/lang/Object;)V", False, False), ("(Ljava/lang/Iterable;)V", False, False)])
    getCount = JavaMethod("()I")
    getColumnNames = JavaMethod("()[Ljava/lang/String;")
    getString = JavaMethod("(I)Ljava/lang/String;")
    getShort = JavaMethod("(I)S")
    getInt = JavaMethod("(I)I")
    getLong = JavaMethod("(I)J")
    getFloat = JavaMethod("(I)F")
    getDouble = JavaMethod("(I)D")
    getBlob = JavaMethod("(I)[B")
    getType = JavaMethod("(I)I")
    isNull = JavaMethod("(I)Z")

    class RowBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/database/MatrixCursor/RowBuilder"
        add = JavaMultipleMethod([("(Ljava/lang/Object;)Landroid/database/MatrixCursor$RowBuilder;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)Landroid/database/MatrixCursor$RowBuilder;", False, False)])