from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebHistoryItem"]

class WebHistoryItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebHistoryItem"
    __javaconstructor__ = [("()V", False)]
    getTitle = JavaMethod("()Ljava/lang/String;")
    getFavicon = JavaMethod("()Landroid/graphics/Bitmap;")
    getOriginalUrl = JavaMethod("()Ljava/lang/String;")
    getUrl = JavaMethod("()Ljava/lang/String;")