from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebHistoryItem"]

class WebHistoryItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebHistoryItem"
    __javaconstructor__ = [("()V", False)]
    getUrl = JavaMethod("()Ljava/lang/String;")
    getOriginalUrl = JavaMethod("()Ljava/lang/String;")
    getTitle = JavaMethod("()Ljava/lang/String;")
    getFavicon = JavaMethod("()Landroid/graphics/Bitmap;")
    clone = JavaMethod("()Landroid/webkit/WebHistoryItem;")