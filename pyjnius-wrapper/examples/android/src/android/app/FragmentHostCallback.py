from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentHostCallback"]

class FragmentHostCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentHostCallback"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/os/Handler;I)V", False)]
    onDump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    onShouldSaveFragmentState = JavaMethod("(Landroid/app/Fragment;)Z")
    onGetLayoutInflater = JavaMethod("()Landroid/view/LayoutInflater;")
    onUseFragmentManagerInflaterFactory = JavaMethod("()Z")
    onGetHost = JavaMethod("()Ljava/lang/Object;")
    onInvalidateOptionsMenu = JavaMethod("()V")
    onStartActivityFromFragment = JavaMethod("(Landroid/app/Fragment;Landroid/content/Intent;ILandroid/os/Bundle;)V")
    onStartIntentSenderFromFragment = JavaMethod("(Landroid/app/Fragment;Landroid/content/IntentSender;ILandroid/content/Intent;IIILandroid/os/Bundle;)V")
    onRequestPermissionsFromFragment = JavaMethod("(Landroid/app/Fragment;[Ljava/lang/String;I)V")
    onHasWindowAnimations = JavaMethod("()Z")
    onGetWindowAnimations = JavaMethod("()I")
    onAttachFragment = JavaMethod("(Landroid/app/Fragment;)V")
    onFindViewById = JavaMethod("(I)Landroid/view/View;")
    onHasView = JavaMethod("()Z")