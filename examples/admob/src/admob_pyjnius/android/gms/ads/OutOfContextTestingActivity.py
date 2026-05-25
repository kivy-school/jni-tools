from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutOfContextTestingActivity"]

class OutOfContextTestingActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/OutOfContextTestingActivity"
    __javaconstructor__ = [("()V", False)]
    CLASS_NAME = JavaStaticField("Ljava/lang/String;")
    AD_UNIT_KEY = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")