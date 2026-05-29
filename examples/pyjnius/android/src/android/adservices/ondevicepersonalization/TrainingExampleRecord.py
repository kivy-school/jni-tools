from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrainingExampleRecord"]

class TrainingExampleRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExampleRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTrainingExample = JavaMethod("()[B")
    getResumptionToken = JavaMethod("()[B")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExampleRecord/Builder"
        __javaconstructor__ = [("()V", False)]
        setTrainingExample = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/TrainingExampleRecord$Builder;", varargs=True)
        setResumptionToken = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/TrainingExampleRecord$Builder;", varargs=True)
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingExampleRecord;")