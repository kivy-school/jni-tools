from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AdvancedProtectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/advancedprotection/AdvancedProtectionManager"
    isAdvancedProtectionEnabled = JavaMethod("()Z")
    registerAdvancedProtectionCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/security/advancedprotection/AdvancedProtectionManager$Callback;)V")
    unregisterAdvancedProtectionCallback = JavaMethod("(Landroid/security/advancedprotection/AdvancedProtectionManager$Callback;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/advancedprotection/AdvancedProtectionManager$Callback"
        onAdvancedProtectionChanged = JavaMethod("(Z)V")