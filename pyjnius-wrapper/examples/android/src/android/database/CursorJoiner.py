from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorJoiner"]

class CursorJoiner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CursorJoiner"
    __javaconstructor__ = [("(Landroid/database/Cursor;[Ljava/lang/String;Landroid/database/Cursor;[Ljava/lang/String;)V", False)]
    iterator = JavaMethod("()Ljava/util/Iterator;")
    hasNext = JavaMethod("()Z")
    next = JavaMethod("()Landroid/database/CursorJoiner$Result;")
    remove = JavaMethod("()V")

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/database/CursorJoiner/Result"
        values = JavaStaticMethod("()[Landroid/database/CursorJoiner$Result;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/database/CursorJoiner$Result;")
        RIGHT = JavaStaticField("Landroid/database/CursorJoiner/Result;")
        LEFT = JavaStaticField("Landroid/database/CursorJoiner/Result;")
        BOTH = JavaStaticField("Landroid/database/CursorJoiner/Result;")