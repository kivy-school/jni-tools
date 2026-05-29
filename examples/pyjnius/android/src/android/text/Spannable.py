from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spannable"]

class Spannable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Spannable"
    setSpan = JavaMethod("(Ljava/lang/Object;III)V")
    removeSpan = JavaMethod("(Ljava/lang/Object;)V")

    class Factory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Spannable/Factory"
        __javaconstructor__ = [("()V", False)]
        getInstance = JavaStaticMethod("()Landroid/text/Spannable$Factory;")
        newSpannable = JavaMethod("(Ljava/lang/CharSequence;)Landroid/text/Spannable;")