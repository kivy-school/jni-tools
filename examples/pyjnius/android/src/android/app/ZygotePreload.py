from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZygotePreload"]

class ZygotePreload(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ZygotePreload"
    doPreload = JavaMethod("(Landroid/content/pm/ApplicationInfo;)V")