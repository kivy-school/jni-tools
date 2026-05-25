from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SmsManager"]

class SmsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/gsm/SmsManager"
    RESULT_ERROR_GENERIC_FAILURE = JavaStaticField("I")
    RESULT_ERROR_NO_SERVICE = JavaStaticField("I")
    RESULT_ERROR_NULL_PDU = JavaStaticField("I")
    RESULT_ERROR_RADIO_OFF = JavaStaticField("I")
    STATUS_ON_SIM_FREE = JavaStaticField("I")
    STATUS_ON_SIM_READ = JavaStaticField("I")
    STATUS_ON_SIM_SENT = JavaStaticField("I")
    STATUS_ON_SIM_UNREAD = JavaStaticField("I")
    STATUS_ON_SIM_UNSENT = JavaStaticField("I")
    getDefault = JavaStaticMethod("()Landroid/telephony/gsm/SmsManager;")
    sendTextMessage = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)V")
    divideMessage = JavaMethod("(Ljava/lang/String;)Ljava/util/ArrayList;")
    sendMultipartTextMessage = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/ArrayList;Ljava/util/ArrayList;Ljava/util/ArrayList;)V")
    sendDataMessage = JavaMethod("(Ljava/lang/String;Ljava/lang/String;S[BLandroid/app/PendingIntent;Landroid/app/PendingIntent;)V")