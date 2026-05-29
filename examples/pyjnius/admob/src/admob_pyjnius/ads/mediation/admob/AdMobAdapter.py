from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdMobAdapter"]

class AdMobAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/ads/mediation/admob/AdMobAdapter"
    __javaconstructor__ = [("()V", False)]
    NEW_BUNDLE = JavaStaticField("Ljava/lang/String;")
    buildExtrasBundle = JavaMethod("(Landroid/os/Bundle;Landroid/os/Bundle;)Landroid/os/Bundle;")