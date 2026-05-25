from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZygotePreload"]

class ZygotePreload(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ZygotePreload"
    doPreload = JavaMethod("(Landroid/content/pm/ApplicationInfo;)V")