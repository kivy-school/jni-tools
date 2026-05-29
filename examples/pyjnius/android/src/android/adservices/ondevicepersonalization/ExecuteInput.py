from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteInput"]

class ExecuteInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInput"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/PersistableBundle;)V", False)]
    getAppPackageName = JavaMethod("()Ljava/lang/String;")
    getAppParams = JavaMethod("()Landroid/os/PersistableBundle;")