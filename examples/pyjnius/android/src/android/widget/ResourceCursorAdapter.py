from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourceCursorAdapter"]

class ResourceCursorAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ResourceCursorAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;ILandroid/database/Cursor;I)V", False), ("(Landroid/content/Context;ILandroid/database/Cursor;Z)V", False), ("(Landroid/content/Context;ILandroid/database/Cursor;)V", False)]
    FLAG_AUTO_REQUERY = JavaStaticField("I")
    FLAG_REGISTER_CONTENT_OBSERVER = JavaStaticField("I")
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    setViewResource = JavaMethod("(I)V")
    newView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    newDropDownView = JavaMethod("(Landroid/content/Context;Landroid/database/Cursor;Landroid/view/ViewGroup;)Landroid/view/View;")
    setDropDownViewResource = JavaMethod("(I)V")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")