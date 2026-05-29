from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleAdapter"]

class SimpleAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SimpleAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/util/List;I[Ljava/lang/String;[I)V", False)]
    IGNORE_ITEM_VIEW_TYPE = JavaStaticField("I")
    NO_SELECTION = JavaStaticField("I")
    getCount = JavaMethod("()I")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getFilter = JavaMethod("()Landroid/widget/Filter;")
    getViewBinder = JavaMethod("()Landroid/widget/SimpleAdapter$ViewBinder;")
    setDropDownViewResource = JavaMethod("(I)V")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    setViewBinder = JavaMethod("(Landroid/widget/SimpleAdapter$ViewBinder;)V")
    setViewImage = JavaMultipleMethod([("(Landroid/widget/ImageView;Ljava/lang/String;)V", False, False), ("(Landroid/widget/ImageView;I)V", False, False)])
    setViewText = JavaMethod("(Landroid/widget/TextView;Ljava/lang/String;)V")

    class ViewBinder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleAdapter$ViewBinder"
        setViewValue = JavaMethod("(Landroid/view/View;Ljava/lang/Object;Ljava/lang/String;)Z")