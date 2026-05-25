from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApplicationInfoHelper"]

class ApplicationInfoHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/ApplicationInfoHelper"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/ApplicationInfoHelper$Companion;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/ApplicationInfoHelper/Companion"
        getInfo = JavaMethod("(Landroid/content/Context;)Landroid/content/pm/ApplicationInfo;")