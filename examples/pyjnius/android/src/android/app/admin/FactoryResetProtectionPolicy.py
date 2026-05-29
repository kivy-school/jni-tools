from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FactoryResetProtectionPolicy"]

class FactoryResetProtectionPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/FactoryResetProtectionPolicy"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFactoryResetProtectionAccounts = JavaMethod("()Ljava/util/List;")
    isFactoryResetProtectionEnabled = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/admin/FactoryResetProtectionPolicy/Builder"
        __javaconstructor__ = [("()V", False)]
        setFactoryResetProtectionAccounts = JavaMethod("(Ljava/util/List;)Landroid/app/admin/FactoryResetProtectionPolicy$Builder;")
        setFactoryResetProtectionEnabled = JavaMethod("(Z)Landroid/app/admin/FactoryResetProtectionPolicy$Builder;")
        build = JavaMethod("()Landroid/app/admin/FactoryResetProtectionPolicy;")