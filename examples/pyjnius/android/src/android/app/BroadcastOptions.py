from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastOptions"]

class BroadcastOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/BroadcastOptions"
    DEFERRAL_POLICY_DEFAULT = JavaStaticField("I")
    DEFERRAL_POLICY_NONE = JavaStaticField("I")
    DEFERRAL_POLICY_UNTIL_ACTIVE = JavaStaticField("I")
    DELIVERY_GROUP_POLICY_ALL = JavaStaticField("I")
    DELIVERY_GROUP_POLICY_MOST_RECENT = JavaStaticField("I")
    fromBundle = JavaStaticMethod("(Landroid/os/Bundle;)Landroid/app/BroadcastOptions;")
    getDeferralPolicy = JavaMethod("()I")
    setDeferralPolicy = JavaMethod("(I)Landroid/app/BroadcastOptions;")
    clearDeferralPolicy = JavaMethod("()V")
    clearDeliveryGroupMatchingKey = JavaMethod("()V")
    clearDeliveryGroupPolicy = JavaMethod("()V")
    getDeliveryGroupMatchingKey = JavaMethod("()Ljava/lang/String;")
    getDeliveryGroupPolicy = JavaMethod("()I")
    setDeliveryGroupMatchingKey = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/app/BroadcastOptions;")
    setDeliveryGroupPolicy = JavaMethod("(I)Landroid/app/BroadcastOptions;")
    makeBasic = JavaStaticMethod("()Landroid/app/BroadcastOptions;")
    isShareIdentityEnabled = JavaMethod("()Z")
    setShareIdentityEnabled = JavaMethod("(Z)Landroid/app/BroadcastOptions;")
    toBundle = JavaMethod("()Landroid/os/Bundle;")