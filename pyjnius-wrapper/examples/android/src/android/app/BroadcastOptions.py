from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastOptions"]

class BroadcastOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/BroadcastOptions"
    DEFERRAL_POLICY_DEFAULT = JavaStaticField("I")
    DEFERRAL_POLICY_NONE = JavaStaticField("I")
    DEFERRAL_POLICY_UNTIL_ACTIVE = JavaStaticField("I")
    DELIVERY_GROUP_POLICY_ALL = JavaStaticField("I")
    DELIVERY_GROUP_POLICY_MOST_RECENT = JavaStaticField("I")
    makeBasic = JavaStaticMethod("()Landroid/app/BroadcastOptions;")
    setShareIdentityEnabled = JavaMethod("(Z)Landroid/app/BroadcastOptions;")
    isShareIdentityEnabled = JavaMethod("()Z")
    setDeferralPolicy = JavaMethod("(I)Landroid/app/BroadcastOptions;")
    getDeferralPolicy = JavaMethod("()I")
    clearDeferralPolicy = JavaMethod("()V")
    setDeliveryGroupPolicy = JavaMethod("(I)Landroid/app/BroadcastOptions;")
    getDeliveryGroupPolicy = JavaMethod("()I")
    clearDeliveryGroupPolicy = JavaMethod("()V")
    setDeliveryGroupMatchingKey = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/app/BroadcastOptions;")
    getDeliveryGroupMatchingKey = JavaMethod("()Ljava/lang/String;")
    clearDeliveryGroupMatchingKey = JavaMethod("()V")
    toBundle = JavaMethod("()Landroid/os/Bundle;")
    fromBundle = JavaStaticMethod("(Landroid/os/Bundle;)Landroid/app/BroadcastOptions;")