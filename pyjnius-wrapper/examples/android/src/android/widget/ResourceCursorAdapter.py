from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourceCursorAdapter"]

class ResourceCursorAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ResourceCursorAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;ILandroid/database/Cursor;)V", False), ("(Landroid/content/Context;ILandroid/database/Cursor;Z)V", False), ("(Landroid/content/Context;ILandroid/database/Cursor;I)V", False)]
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    newView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    newDropDownView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    setViewResource = JavaMethod("(I)V")
    setDropDownViewResource = JavaMethod("(I)V")