from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppInfo"]

class AppInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/AppInfo"
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getIcon = JavaMethod("()Landroid/graphics/Bitmap;")
    getName = JavaMethod("()Ljava/lang/String;")