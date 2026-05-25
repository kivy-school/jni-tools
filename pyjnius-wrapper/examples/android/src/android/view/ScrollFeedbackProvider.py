from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollFeedbackProvider"]

class ScrollFeedbackProvider(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollFeedbackProvider"
    createProvider = JavaStaticMethod("(Landroid/view/View;)Landroid/view/ScrollFeedbackProvider;")
    onSnapToItem = JavaMethod("(III)V")
    onScrollLimit = JavaMethod("(IIIZ)V")
    onScrollProgress = JavaMethod("(IIII)V")