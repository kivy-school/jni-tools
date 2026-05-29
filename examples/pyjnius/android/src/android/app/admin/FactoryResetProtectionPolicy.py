from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FactoryResetProtectionPolicy"]

class FactoryResetProtectionPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/FactoryResetProtectionPolicy"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getFactoryResetProtectionAccounts = JavaMethod("()Ljava/util/List;")
    isFactoryResetProtectionEnabled = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/admin/FactoryResetProtectionPolicy$Builder"
        __javaconstructor__ = [("()V", False)]
        setFactoryResetProtectionEnabled = JavaMethod("(Z)Landroid/app/admin/FactoryResetProtectionPolicy$Builder;")
        setFactoryResetProtectionAccounts = JavaMethod("(Ljava/util/List;)Landroid/app/admin/FactoryResetProtectionPolicy$Builder;")
        build = JavaMethod("()Landroid/app/admin/FactoryResetProtectionPolicy;")