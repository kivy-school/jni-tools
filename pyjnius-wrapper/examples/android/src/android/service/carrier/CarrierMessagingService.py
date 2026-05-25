from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CarrierMessagingService"]

class CarrierMessagingService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/carrier/CarrierMessagingService"
    __javaconstructor__ = [("()V", False)]
    DOWNLOAD_STATUS_ERROR = JavaStaticField("I")
    DOWNLOAD_STATUS_OK = JavaStaticField("I")
    DOWNLOAD_STATUS_RETRY_ON_CARRIER_NETWORK = JavaStaticField("I")
    RECEIVE_OPTIONS_DEFAULT = JavaStaticField("I")
    RECEIVE_OPTIONS_DROP = JavaStaticField("I")
    RECEIVE_OPTIONS_SKIP_NOTIFY_WHEN_CREDENTIAL_PROTECTED_STORAGE_UNAVAILABLE = JavaStaticField("I")
    SEND_FLAG_REQUEST_DELIVERY_STATUS = JavaStaticField("I")
    SEND_STATUS_ERROR = JavaStaticField("I")
    SEND_STATUS_OK = JavaStaticField("I")
    SEND_STATUS_RETRY_ON_CARRIER_NETWORK = JavaStaticField("I")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onFilterSms = JavaMethod("(Landroid/service/carrier/MessagePdu;Ljava/lang/String;IILandroid/service/carrier/CarrierMessagingService$ResultCallback;)V")
    onReceiveTextSms = JavaMethod("(Landroid/service/carrier/MessagePdu;Ljava/lang/String;IILandroid/service/carrier/CarrierMessagingService$ResultCallback;)V")
    onSendTextSms = JavaMultipleMethod([("(Ljava/lang/String;ILjava/lang/String;Landroid/service/carrier/CarrierMessagingService$ResultCallback;)V", False, False), ("(Ljava/lang/String;ILjava/lang/String;ILandroid/service/carrier/CarrierMessagingService$ResultCallback;)V", False, False)])
    onSendDataSms = JavaMultipleMethod([("([BILjava/lang/String;ILandroid/service/carrier/CarrierMessagingService$ResultCallback;)V", False, False), ("([BILjava/lang/String;IILandroid/service/carrier/CarrierMessagingService$ResultCallback;)V", False, False)])
    onSendMultipartTextSms = JavaMultipleMethod([("(Ljava/util/List;ILjava/lang/String;Landroid/service/carrier/CarrierMessagingService$ResultCallback;)V", False, False), ("(Ljava/util/List;ILjava/lang/String;ILandroid/service/carrier/CarrierMessagingService$ResultCallback;)V", False, False)])
    onSendMms = JavaMethod("(Landroid/net/Uri;ILandroid/net/Uri;Landroid/service/carrier/CarrierMessagingService$ResultCallback;)V")
    onDownloadMms = JavaMethod("(Landroid/net/Uri;ILandroid/net/Uri;Landroid/service/carrier/CarrierMessagingService$ResultCallback;)V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")

    class ResultCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/carrier/CarrierMessagingService/ResultCallback"
        onReceiveResult = JavaMethod("(Ljava/lang/Object;)V")

    class SendMmsResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/carrier/CarrierMessagingService/SendMmsResult"
        __javaconstructor__ = [("(I[B)V", False)]
        getSendStatus = JavaMethod("()I")
        getSendConfPdu = JavaMethod("()[B")

    class SendMultipartSmsResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/carrier/CarrierMessagingService/SendMultipartSmsResult"
        __javaconstructor__ = [("(I[I)V", False)]
        getMessageRefs = JavaMethod("()[I")
        getSendStatus = JavaMethod("()I")

    class SendSmsResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/carrier/CarrierMessagingService/SendSmsResult"
        __javaconstructor__ = [("(II)V", False)]
        getMessageRef = JavaMethod("()I")
        getSendStatus = JavaMethod("()I")