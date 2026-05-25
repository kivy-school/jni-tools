from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PermissionsActivity"]

class PermissionsActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/PermissionsActivity"
    __javaconstructor__ = [("()V", False)]
    registerAsCallback = JavaStaticMethod("(Ljava/lang/String;Lcom/onesignal/PermissionsActivity$PermissionCallback;)V")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onNewIntent = JavaMethod("(Landroid/content/Intent;)V")
    onRequestPermissionsResult = JavaMethod("(I[Ljava/lang/String;[I)V")