from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnReceiveContentListener"]

class OnReceiveContentListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/OnReceiveContentListener"
    onReceiveContent = JavaMethod("(Landroid/view/View;Landroid/view/ContentInfo;)Landroid/view/ContentInfo;")