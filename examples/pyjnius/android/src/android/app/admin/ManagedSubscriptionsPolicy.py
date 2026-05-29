from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ManagedSubscriptionsPolicy"]

class ManagedSubscriptionsPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/ManagedSubscriptionsPolicy"
    __javaconstructor__ = [("(I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_ALL_MANAGED_SUBSCRIPTIONS = JavaStaticField("I")
    TYPE_ALL_PERSONAL_SUBSCRIPTIONS = JavaStaticField("I")
    getPolicyType = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")