from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillCallback"]

class FillCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillCallback"
    onFailure = JavaMethod("(Ljava/lang/CharSequence;)V")
    onSuccess = JavaMethod("(Landroid/service/autofill/FillResponse;)V")