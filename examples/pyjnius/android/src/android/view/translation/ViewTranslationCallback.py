from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewTranslationCallback"]

class ViewTranslationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationCallback"
    onShowTranslation = JavaMethod("(Landroid/view/View;)Z")
    onHideTranslation = JavaMethod("(Landroid/view/View;)Z")
    onClearTranslation = JavaMethod("(Landroid/view/View;)Z")