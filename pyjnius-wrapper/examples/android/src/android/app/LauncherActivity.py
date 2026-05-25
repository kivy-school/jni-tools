from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LauncherActivity"]

class LauncherActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LauncherActivity"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    setTitle = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    onSetContentView = JavaMethod("()V")
    onListItemClick = JavaMethod("(Landroid/widget/ListView;Landroid/view/View;IJ)V")
    intentForPosition = JavaMethod("(I)Landroid/content/Intent;")
    itemForPosition = JavaMethod("(I)Landroid/app/LauncherActivity$ListItem;")
    getTargetIntent = JavaMethod("()Landroid/content/Intent;")
    onQueryPackageManager = JavaMethod("(Landroid/content/Intent;)Ljava/util/List;")
    makeListItems = JavaMethod("()Ljava/util/List;")

    class IconResizer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/LauncherActivity/IconResizer"
        __javaconstructor__ = [("(Landroid/app/LauncherActivity;)V", False)]
        createIconThumbnail = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/graphics/drawable/Drawable;")

    class ListItem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/LauncherActivity/ListItem"
        __javaconstructor__ = [("()V", False)]
        className = JavaField("Ljava/lang/String;")
        extras = JavaField("Landroid/os/Bundle;")
        icon = JavaField("Landroid/graphics/drawable/Drawable;")
        label = JavaField("Ljava/lang/CharSequence;")
        packageName = JavaField("Ljava/lang/String;")
        resolveInfo = JavaField("Landroid/content/pm/ResolveInfo;")