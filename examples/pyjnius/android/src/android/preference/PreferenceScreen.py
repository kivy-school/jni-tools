from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceScreen"]

class PreferenceScreen(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceScreen"
    DEFAULT_ORDER = JavaStaticField("I")
    getRootAdapter = JavaMethod("()Landroid/widget/ListAdapter;")
    getDialog = JavaMethod("()Landroid/app/Dialog;")
    onDismiss = JavaMethod("(Landroid/content/DialogInterface;)V")
    bind = JavaMethod("(Landroid/widget/ListView;)V")
    onItemClick = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)V")