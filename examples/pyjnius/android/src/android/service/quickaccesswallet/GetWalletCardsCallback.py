from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetWalletCardsCallback"]

class GetWalletCardsCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/GetWalletCardsCallback"
    onFailure = JavaMethod("(Landroid/service/quickaccesswallet/GetWalletCardsError;)V")
    onSuccess = JavaMethod("(Landroid/service/quickaccesswallet/GetWalletCardsResponse;)V")