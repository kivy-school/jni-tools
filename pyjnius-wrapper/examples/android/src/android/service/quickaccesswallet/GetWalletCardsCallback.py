from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetWalletCardsCallback"]

class GetWalletCardsCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/GetWalletCardsCallback"
    onSuccess = JavaMethod("(Landroid/service/quickaccesswallet/GetWalletCardsResponse;)V")
    onFailure = JavaMethod("(Landroid/service/quickaccesswallet/GetWalletCardsError;)V")