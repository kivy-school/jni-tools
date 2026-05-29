from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourceCursorTreeAdapter"]

class ResourceCursorTreeAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ResourceCursorTreeAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/database/Cursor;IIII)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;III)V", False), ("(Landroid/content/Context;Landroid/database/Cursor;II)V", False)]
    newChildView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;ZLandroid/view/ViewGroup;)Landroid/view/View;")
    newGroupView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;ZLandroid/view/ViewGroup;)Landroid/view/View;")