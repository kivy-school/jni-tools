from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleAdapter"]

class SimpleAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SimpleAdapter"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/util/List;I[Ljava/lang/String;[I)V", False)]
    getCount = JavaMethod("()I")
    getItem = JavaMethod("(I)Ljava/lang/Object;")
    getItemId = JavaMethod("(I)J")
    getView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    setDropDownViewResource = JavaMethod("(I)V")
    setDropDownViewTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getDropDownViewTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getDropDownView = JavaMethod("(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;")
    getViewBinder = JavaMethod("()Landroid/widget/SimpleAdapter$ViewBinder;")
    setViewBinder = JavaMethod("(Landroid/widget/SimpleAdapter$ViewBinder;)V")
    setViewImage = JavaMultipleMethod([("(Landroid/widget/ImageView;I)V", False, False), ("(Landroid/widget/ImageView;Ljava/lang/String;)V", False, False)])
    setViewText = JavaMethod("(Landroid/widget/TextView;Ljava/lang/String;)V")
    getFilter = JavaMethod("()Landroid/widget/Filter;")

    class ViewBinder(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SimpleAdapter/ViewBinder"
        setViewValue = JavaMethod("(Landroid/view/View;Ljava/lang/Object;Ljava/lang/String;)Z")