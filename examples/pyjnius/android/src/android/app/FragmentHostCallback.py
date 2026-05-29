from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentHostCallback"]

class FragmentHostCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentHostCallback"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/os/Handler;I)V", False)]
    onGetLayoutInflater = JavaMethod("()Landroid/view/LayoutInflater;")
    onDump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    onFindViewById = JavaMethod("(I)Landroid/view/View;")
    onGetHost = JavaMethod("()Ljava/lang/Object;")
    onGetWindowAnimations = JavaMethod("()I")
    onHasView = JavaMethod("()Z")
    onHasWindowAnimations = JavaMethod("()Z")
    onInvalidateOptionsMenu = JavaMethod("()V")
    onRequestPermissionsFromFragment = JavaMethod("(Landroid/app/Fragment;[Ljava/lang/String;I)V")
    onShouldSaveFragmentState = JavaMethod("(Landroid/app/Fragment;)Z")
    onStartActivityFromFragment = JavaMethod("(Landroid/app/Fragment;Landroid/content/Intent;ILandroid/os/Bundle;)V")
    onStartIntentSenderFromFragment = JavaMethod("(Landroid/app/Fragment;Landroid/content/IntentSender;ILandroid/content/Intent;IIILandroid/os/Bundle;)V")
    onUseFragmentManagerInflaterFactory = JavaMethod("()Z")
    onAttachFragment = JavaMethod("(Landroid/app/Fragment;)V")