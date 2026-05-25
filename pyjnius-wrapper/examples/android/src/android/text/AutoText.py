from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutoText"]

class AutoText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/AutoText"
    get = JavaStaticMethod("(Ljava/lang/CharSequence;IILandroid/view/View;)Ljava/lang/String;")
    getSize = JavaStaticMethod("(Landroid/view/View;)I")