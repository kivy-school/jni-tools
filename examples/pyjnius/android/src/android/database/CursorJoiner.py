from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorJoiner"]

class CursorJoiner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/CursorJoiner"
    __javaconstructor__ = [("(Landroid/database/Cursor;[Ljava/lang/String;Landroid/database/Cursor;[Ljava/lang/String;)V", False)]
    remove = JavaMethod("()V")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    hasNext = JavaMethod("()Z")
    next = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/database/CursorJoiner$Result;", False, False)])

    class Result(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/database/CursorJoiner$Result"
        BOTH = JavaStaticField("Landroid/database/CursorJoiner$Result;")
        LEFT = JavaStaticField("Landroid/database/CursorJoiner$Result;")
        RIGHT = JavaStaticField("Landroid/database/CursorJoiner$Result;")
        values = JavaStaticMethod("()[Landroid/database/CursorJoiner$Result;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/database/CursorJoiner$Result;")
        BOTH = JavaStaticField("Landroid/database/CursorJoiner$Result;")
        LEFT = JavaStaticField("Landroid/database/CursorJoiner$Result;")
        RIGHT = JavaStaticField("Landroid/database/CursorJoiner$Result;")