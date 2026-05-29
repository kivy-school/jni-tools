from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollFeedbackProvider"]

class ScrollFeedbackProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollFeedbackProvider"
    onScrollLimit = JavaMethod("(IIIZ)V")
    createProvider = JavaStaticMethod("(Landroid/view/View;)Landroid/view/ScrollFeedbackProvider;")
    onSnapToItem = JavaMethod("(III)V")
    onScrollProgress = JavaMethod("(IIII)V")