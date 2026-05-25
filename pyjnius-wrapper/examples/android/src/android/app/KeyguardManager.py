from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyguardManager"]

class KeyguardManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/KeyguardManager"
    createConfirmDeviceCredentialIntent = JavaMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/content/Intent;")
    newKeyguardLock = JavaMethod("(Ljava/lang/String;)Landroid/app/KeyguardManager$KeyguardLock;")
    isKeyguardLocked = JavaMethod("()Z")
    isKeyguardSecure = JavaMethod("()Z")
    inKeyguardRestrictedInputMode = JavaMethod("()Z")
    isDeviceLocked = JavaMethod("()Z")
    isDeviceSecure = JavaMethod("()Z")
    requestDismissKeyguard = JavaMethod("(Landroid/app/Activity;Landroid/app/KeyguardManager$KeyguardDismissCallback;)V")
    exitKeyguardSecurely = JavaMethod("(Landroid/app/KeyguardManager$OnKeyguardExitResult;)V")
    addKeyguardLockedStateListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/app/KeyguardManager$KeyguardLockedStateListener;)V")
    removeKeyguardLockedStateListener = JavaMethod("(Landroid/app/KeyguardManager$KeyguardLockedStateListener;)V")

    class KeyguardDismissCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager/KeyguardDismissCallback"
        __javaconstructor__ = [("()V", False)]
        onDismissError = JavaMethod("()V")
        onDismissSucceeded = JavaMethod("()V")
        onDismissCancelled = JavaMethod("()V")

    class KeyguardLock(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager/KeyguardLock"
        disableKeyguard = JavaMethod("()V")
        reenableKeyguard = JavaMethod("()V")

    class KeyguardLockedStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager/KeyguardLockedStateListener"
        onKeyguardLockedStateChanged = JavaMethod("(Z)V")

    class OnKeyguardExitResult(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/KeyguardManager/OnKeyguardExitResult"
        onKeyguardExitResult = JavaMethod("(Z)V")