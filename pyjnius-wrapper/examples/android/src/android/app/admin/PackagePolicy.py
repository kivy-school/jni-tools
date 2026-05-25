from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PackagePolicy"]

class PackagePolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/PackagePolicy"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PACKAGE_POLICY_ALLOWLIST = JavaStaticField("I")
    PACKAGE_POLICY_ALLOWLIST_AND_SYSTEM = JavaStaticField("I")
    PACKAGE_POLICY_BLOCKLIST = JavaStaticField("I")
    getPolicyType = JavaMethod("()I")
    getPackageNames = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")