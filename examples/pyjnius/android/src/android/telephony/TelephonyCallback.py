from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TelephonyCallback"]

class TelephonyCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/TelephonyCallback"
    __javaconstructor__ = [("()V", False)]

    class UserMobileDataStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$UserMobileDataStateListener"
        onUserMobileDataStateChanged = JavaMethod("(Z)V")

    class SignalStrengthsListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$SignalStrengthsListener"
        onSignalStrengthsChanged = JavaMethod("(Landroid/telephony/SignalStrength;)V")

    class ServiceStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$ServiceStateListener"
        onServiceStateChanged = JavaMethod("(Landroid/telephony/ServiceState;)V")

    class RegistrationFailedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$RegistrationFailedListener"
        onRegistrationFailed = JavaMethod("(Landroid/telephony/CellIdentity;Ljava/lang/String;III)V")

    class PreciseDataConnectionStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$PreciseDataConnectionStateListener"
        onPreciseDataConnectionStateChanged = JavaMethod("(Landroid/telephony/PreciseDataConnectionState;)V")

    class PhysicalChannelConfigListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$PhysicalChannelConfigListener"
        onPhysicalChannelConfigChanged = JavaMethod("(Ljava/util/List;)V")

    class MessageWaitingIndicatorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$MessageWaitingIndicatorListener"
        onMessageWaitingIndicatorChanged = JavaMethod("(Z)V")

    class ImsCallDisconnectCauseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$ImsCallDisconnectCauseListener"
        onImsCallDisconnectCauseChanged = JavaMethod("(Landroid/telephony/ims/ImsReasonInfo;)V")

    class EmergencyNumberListListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$EmergencyNumberListListener"
        onEmergencyNumberListChanged = JavaMethod("(Ljava/util/Map;)V")

    class DisplayInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$DisplayInfoListener"
        onDisplayInfoChanged = JavaMethod("(Landroid/telephony/TelephonyDisplayInfo;)V")

    class DataConnectionStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$DataConnectionStateListener"
        onDataConnectionStateChanged = JavaMethod("(II)V")

    class DataActivityListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$DataActivityListener"
        onDataActivity = JavaMethod("(I)V")

    class DataActivationStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$DataActivationStateListener"
        onDataActivationStateChanged = JavaMethod("(I)V")

    class CellLocationListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$CellLocationListener"
        onCellLocationChanged = JavaMethod("(Landroid/telephony/CellLocation;)V")

    class CellInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$CellInfoListener"
        onCellInfoChanged = JavaMethod("(Ljava/util/List;)V")

    class CarrierNetworkListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$CarrierNetworkListener"
        onCarrierNetworkChange = JavaMethod("(Z)V")

    class CallStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$CallStateListener"
        onCallStateChanged = JavaMethod("(I)V")

    class CallForwardingIndicatorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$CallForwardingIndicatorListener"
        onCallForwardingIndicatorChanged = JavaMethod("(Z)V")

    class CallDisconnectCauseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$CallDisconnectCauseListener"
        onCallDisconnectCauseChanged = JavaMethod("(II)V")

    class BarringInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$BarringInfoListener"
        onBarringInfoChanged = JavaMethod("(Landroid/telephony/BarringInfo;)V")

    class ActiveDataSubscriptionIdListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback$ActiveDataSubscriptionIdListener"
        onActiveDataSubscriptionIdChanged = JavaMethod("(I)V")