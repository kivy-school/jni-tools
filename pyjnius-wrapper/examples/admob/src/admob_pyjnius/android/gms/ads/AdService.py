from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdService"]

class AdService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdService"
    __javaconstructor__ = [("()V", False)]
    CLASS_NAME = JavaStaticField("Ljava/lang/String;")
    onHandleIntent = JavaMethod("(Landroid/content/Intent;)V")