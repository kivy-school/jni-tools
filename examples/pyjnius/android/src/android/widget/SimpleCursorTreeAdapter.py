from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleCursorTreeAdapter"]

class SimpleCursorTreeAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SimpleCursorTreeAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/database/Cursor;I[Ljava/lang/String;[II[Ljava/lang/String;[I)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;II[Ljava/lang/String;[II[Ljava/lang/String;[I)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;II[Ljava/lang/String;[III[Ljava/lang/String;[I)V", False)]
    getViewBinder = JavaMethod("()Landroid/widget/SimpleCursorTreeAdapter$ViewBinder;")
    setViewBinder = JavaMethod("(Landroid/widget/SimpleCursorTreeAdapter$ViewBinder;)V")
    setViewText = JavaMethod("(Landroid/widget/TextView;Ljava/lang/String;)V")

    class ViewBinder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleCursorTreeAdapter$ViewBinder"
        setViewValue = JavaMethod("(Landroid/view/View;Landroid/database/Cursor;I)Z")