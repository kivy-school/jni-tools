from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebBackForwardList"]

class WebBackForwardList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebBackForwardList"
    __javaconstructor__ = [("()V", False)]
    getSize = JavaMethod("()I")
    getCurrentIndex = JavaMethod("()I")
    getCurrentItem = JavaMethod("()Landroid/webkit/WebHistoryItem;")
    getItemAtIndex = JavaMethod("(I)Landroid/webkit/WebHistoryItem;")