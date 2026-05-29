from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteInput"]

class ExecuteInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInput"
    getAppPackageName = JavaMethod("()Ljava/lang/String;")
    getAppParams = JavaMethod("()Landroid/os/PersistableBundle;")