from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSWorkManagerHelper"]

class OSWorkManagerHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSWorkManagerHelper"
    INSTANCE = JavaStaticField("Lcom/onesignal/OSWorkManagerHelper;")
    getInstance = JavaStaticMethod("(Landroid/content/Context;)Landroidx/work/WorkManager;")