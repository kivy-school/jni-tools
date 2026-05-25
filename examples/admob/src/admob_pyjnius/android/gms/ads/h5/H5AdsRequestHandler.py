from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["H5AdsRequestHandler"]

class H5AdsRequestHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/h5/H5AdsRequestHandler"
    __javaconstructor__ = [("(Landroid/content/Context;Lcom/google/android/gms/ads/h5/OnH5AdsEventListener;)V", False)]
    clearAdObjects = JavaMethod("()V")
    shouldInterceptRequest = JavaMethod("(Ljava/lang/String;)Z")
    handleH5AdsRequest = JavaMethod("(Ljava/lang/String;)Z")