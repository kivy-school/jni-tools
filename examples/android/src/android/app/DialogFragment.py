from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialogFragment"]

class DialogFragment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/DialogFragment"
    __javaconstructor__ = [("()V", False)]
    STYLE_NORMAL = JavaStaticField("I")
    STYLE_NO_FRAME = JavaStaticField("I")
    STYLE_NO_INPUT = JavaStaticField("I")
    STYLE_NO_TITLE = JavaStaticField("I")
    setStyle = JavaMethod("(II)V")
    show = JavaMultipleMethod([("(Landroid/app/FragmentManager;Ljava/lang/String;)V", False, False), ("(Landroid/app/FragmentTransaction;Ljava/lang/String;)I", False, False)])
    dismiss = JavaMethod("()V")
    dismissAllowingStateLoss = JavaMethod("()V")
    getDialog = JavaMethod("()Landroid/app/Dialog;")
    getTheme = JavaMethod("()I")
    setCancelable = JavaMethod("(Z)V")
    isCancelable = JavaMethod("()Z")
    setShowsDialog = JavaMethod("(Z)V")
    getShowsDialog = JavaMethod("()Z")
    onAttach = JavaMethod("(Landroid/content/Context;)V")
    onDetach = JavaMethod("()V")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onGetLayoutInflater = JavaMethod("(Landroid/os/Bundle;)Landroid/view/LayoutInflater;")
    onCreateDialog = JavaMethod("(Landroid/os/Bundle;)Landroid/app/Dialog;")
    onCancel = JavaMethod("(Landroid/content/DialogInterface;)V")
    onDismiss = JavaMethod("(Landroid/content/DialogInterface;)V")
    onActivityCreated = JavaMethod("(Landroid/os/Bundle;)V")
    onStart = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onStop = JavaMethod("()V")
    onDestroyView = JavaMethod("()V")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")