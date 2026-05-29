from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObbScanner"]

class ObbScanner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/ObbScanner"
    getObbInfo = JavaStaticMethod("(Ljava/lang/String;)Landroid/content/res/ObbInfo;")