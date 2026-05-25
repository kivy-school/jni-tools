from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SafeBrowsingResponse"]

class SafeBrowsingResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/SafeBrowsingResponse"
    __javaconstructor__ = [("()V", False)]
    showInterstitial = JavaMethod("(Z)V")
    proceed = JavaMethod("(Z)V")
    backToSafety = JavaMethod("(Z)V")