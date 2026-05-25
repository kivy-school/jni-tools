from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceScreen"]

class PreferenceScreen(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceScreen"
    getRootAdapter = JavaMethod("()Landroid/widget/ListAdapter;")
    onCreateRootAdapter = JavaMethod("()Landroid/widget/ListAdapter;")
    bind = JavaMethod("(Landroid/widget/ListView;)V")
    onClick = JavaMethod("()V")
    onDismiss = JavaMethod("(Landroid/content/DialogInterface;)V")
    getDialog = JavaMethod("()Landroid/app/Dialog;")
    onItemClick = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)V")
    isOnSameScreenAsChildren = JavaMethod("()Z")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")