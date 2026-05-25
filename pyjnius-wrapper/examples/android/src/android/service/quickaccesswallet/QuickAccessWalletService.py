from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuickAccessWalletService"]

class QuickAccessWalletService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/QuickAccessWalletService"
    __javaconstructor__ = [("()V", False)]
    ACTION_VIEW_WALLET = JavaStaticField("Ljava/lang/String;")
    ACTION_VIEW_WALLET_SETTINGS = JavaStaticField("Ljava/lang/String;")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onWalletCardsRequested = JavaMethod("(Landroid/service/quickaccesswallet/GetWalletCardsRequest;Landroid/service/quickaccesswallet/GetWalletCardsCallback;)V")
    onWalletCardSelected = JavaMethod("(Landroid/service/quickaccesswallet/SelectWalletCardRequest;)V")
    onWalletDismissed = JavaMethod("()V")
    sendWalletServiceEvent = JavaMethod("(Landroid/service/quickaccesswallet/WalletServiceEvent;)V")
    getTargetActivityPendingIntent = JavaMethod("()Landroid/app/PendingIntent;")