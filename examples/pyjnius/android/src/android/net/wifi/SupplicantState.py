from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SupplicantState"]

class SupplicantState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/SupplicantState"
    values = JavaStaticMethod("()[Landroid/net/wifi/SupplicantState;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/wifi/SupplicantState;")
    isValidState = JavaStaticMethod("(Landroid/net/wifi/SupplicantState;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    DISCONNECTED = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    INTERFACE_DISABLED = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    INACTIVE = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    SCANNING = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    AUTHENTICATING = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    ASSOCIATING = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    ASSOCIATED = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    FOUR_WAY_HANDSHAKE = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    GROUP_HANDSHAKE = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    COMPLETED = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    DORMANT = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    UNINITIALIZED = JavaStaticField("Landroid/net/wifi/SupplicantState;")
    INVALID = JavaStaticField("Landroid/net/wifi/SupplicantState;")