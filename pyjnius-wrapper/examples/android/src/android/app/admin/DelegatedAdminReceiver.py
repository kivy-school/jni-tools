from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DelegatedAdminReceiver"]

class DelegatedAdminReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DelegatedAdminReceiver"
    __javaconstructor__ = [("()V", False)]
    onChoosePrivateKeyAlias = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;ILandroid/net/Uri;Ljava/lang/String;)Ljava/lang/String;")
    onNetworkLogsAvailable = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;JI)V")
    onSecurityLogsAvailable = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")