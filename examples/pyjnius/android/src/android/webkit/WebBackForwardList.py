from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebBackForwardList"]

class WebBackForwardList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebBackForwardList"
    __javaconstructor__ = [("()V", False)]
    getCurrentItem = JavaMethod("()Landroid/webkit/WebHistoryItem;")
    getCurrentIndex = JavaMethod("()I")
    getItemAtIndex = JavaMethod("(I)Landroid/webkit/WebHistoryItem;")
    getSize = JavaMethod("()I")
    clone = JavaMethod("()Landroid/webkit/WebBackForwardList;")