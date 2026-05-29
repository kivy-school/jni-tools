from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ManagedSubscriptionsPolicy"]

class ManagedSubscriptionsPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/ManagedSubscriptionsPolicy"
    __javaconstructor__ = [("(I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_ALL_MANAGED_SUBSCRIPTIONS = JavaStaticField("I")
    TYPE_ALL_PERSONAL_SUBSCRIPTIONS = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPolicyType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")