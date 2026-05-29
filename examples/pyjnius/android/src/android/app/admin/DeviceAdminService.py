from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceAdminService"]

class DeviceAdminService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DeviceAdminService"
    __javaconstructor__ = [("()V", False)]
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")