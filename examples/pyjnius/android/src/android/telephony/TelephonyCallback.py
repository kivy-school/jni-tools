from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TelephonyCallback"]

class TelephonyCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/TelephonyCallback"
    __javaconstructor__ = [("()V", False)]

    class ActiveDataSubscriptionIdListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/ActiveDataSubscriptionIdListener"
        onActiveDataSubscriptionIdChanged = JavaMethod("(I)V")

    class BarringInfoListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/BarringInfoListener"
        onBarringInfoChanged = JavaMethod("(Landroid/telephony/BarringInfo;)V")

    class CallDisconnectCauseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/CallDisconnectCauseListener"
        onCallDisconnectCauseChanged = JavaMethod("(II)V")

    class CallForwardingIndicatorListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/CallForwardingIndicatorListener"
        onCallForwardingIndicatorChanged = JavaMethod("(Z)V")

    class CallStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/CallStateListener"
        onCallStateChanged = JavaMethod("(I)V")

    class CarrierNetworkListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/CarrierNetworkListener"
        onCarrierNetworkChange = JavaMethod("(Z)V")

    class CellInfoListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/CellInfoListener"
        onCellInfoChanged = JavaMethod("(Ljava/util/List;)V")

    class CellLocationListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/CellLocationListener"
        onCellLocationChanged = JavaMethod("(Landroid/telephony/CellLocation;)V")

    class DataActivationStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/DataActivationStateListener"
        onDataActivationStateChanged = JavaMethod("(I)V")

    class DataActivityListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/DataActivityListener"
        onDataActivity = JavaMethod("(I)V")

    class DataConnectionStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/DataConnectionStateListener"
        onDataConnectionStateChanged = JavaMethod("(II)V")

    class DisplayInfoListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/DisplayInfoListener"
        onDisplayInfoChanged = JavaMethod("(Landroid/telephony/TelephonyDisplayInfo;)V")

    class EmergencyNumberListListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/EmergencyNumberListListener"
        onEmergencyNumberListChanged = JavaMethod("(Ljava/util/Map;)V")

    class ImsCallDisconnectCauseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/ImsCallDisconnectCauseListener"
        onImsCallDisconnectCauseChanged = JavaMethod("(Landroid/telephony/ims/ImsReasonInfo;)V")

    class MessageWaitingIndicatorListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/MessageWaitingIndicatorListener"
        onMessageWaitingIndicatorChanged = JavaMethod("(Z)V")

    class PhysicalChannelConfigListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/PhysicalChannelConfigListener"
        onPhysicalChannelConfigChanged = JavaMethod("(Ljava/util/List;)V")

    class PreciseDataConnectionStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/PreciseDataConnectionStateListener"
        onPreciseDataConnectionStateChanged = JavaMethod("(Landroid/telephony/PreciseDataConnectionState;)V")

    class RegistrationFailedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/RegistrationFailedListener"
        onRegistrationFailed = JavaMethod("(Landroid/telephony/CellIdentity;Ljava/lang/String;III)V")

    class ServiceStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/ServiceStateListener"
        onServiceStateChanged = JavaMethod("(Landroid/telephony/ServiceState;)V")

    class SignalStrengthsListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/SignalStrengthsListener"
        onSignalStrengthsChanged = JavaMethod("(Landroid/telephony/SignalStrength;)V")

    class UserMobileDataStateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyCallback/UserMobileDataStateListener"
        onUserMobileDataStateChanged = JavaMethod("(Z)V")