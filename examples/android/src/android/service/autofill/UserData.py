from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserData"]

class UserData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/UserData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFieldClassificationAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFieldClassificationAlgorithmForCategory = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getMaxUserDataSize = JavaStaticMethod("()I")
    getMaxFieldClassificationIdsSize = JavaStaticMethod("()I")
    getMaxCategoryCount = JavaStaticMethod("()I")
    getMinValueLength = JavaStaticMethod("()I")
    getMaxValueLength = JavaStaticMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/UserData/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
        setFieldClassificationAlgorithm = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)Landroid/service/autofill/UserData$Builder;")
        setFieldClassificationAlgorithmForCategory = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/service/autofill/UserData$Builder;")
        add = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/service/autofill/UserData$Builder;")
        build = JavaMethod("()Landroid/service/autofill/UserData;")