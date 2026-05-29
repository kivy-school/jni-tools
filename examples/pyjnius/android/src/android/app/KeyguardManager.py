from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyguardManager"]

class KeyguardManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/KeyguardManager"
    isDeviceSecure = JavaMethod("()Z")
    isDeviceLocked = JavaMethod("()Z")
    newKeyguardLock = JavaMethod("(Ljava/lang/String;)Landroid/app/KeyguardManager$KeyguardLock;")
    isKeyguardSecure = JavaMethod("()Z")
    isKeyguardLocked = JavaMethod("()Z")
    addKeyguardLockedStateListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/app/KeyguardManager$KeyguardLockedStateListener;)V")
    createConfirmDeviceCredentialIntent = JavaMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/content/Intent;")
    exitKeyguardSecurely = JavaMethod("(Landroid/app/KeyguardManager$OnKeyguardExitResult;)V")
    inKeyguardRestrictedInputMode = JavaMethod("()Z")
    removeKeyguardLockedStateListener = JavaMethod("(Landroid/app/KeyguardManager$KeyguardLockedStateListener;)V")
    requestDismissKeyguard = JavaMethod("(Landroid/app/Activity;Landroid/app/KeyguardManager$KeyguardDismissCallback;)V")

    class OnKeyguardExitResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager$OnKeyguardExitResult"
        onKeyguardExitResult = JavaMethod("(Z)V")

    class KeyguardLockedStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager$KeyguardLockedStateListener"
        onKeyguardLockedStateChanged = JavaMethod("(Z)V")

    class KeyguardLock(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager$KeyguardLock"
        reenableKeyguard = JavaMethod("()V")
        disableKeyguard = JavaMethod("()V")

    class KeyguardDismissCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager$KeyguardDismissCallback"
        __javaconstructor__ = [("()V", False)]
        onDismissCancelled = JavaMethod("()V")
        onDismissSucceeded = JavaMethod("()V")
        onDismissError = JavaMethod("()V")