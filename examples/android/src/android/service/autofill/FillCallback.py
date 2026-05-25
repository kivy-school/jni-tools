from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillCallback"]

class FillCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillCallback"
    onSuccess = JavaMethod("(Landroid/service/autofill/FillResponse;)V")
    onFailure = JavaMethod("(Ljava/lang/CharSequence;)V")