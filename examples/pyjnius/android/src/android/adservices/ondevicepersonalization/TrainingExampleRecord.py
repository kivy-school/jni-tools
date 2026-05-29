from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrainingExampleRecord"]

class TrainingExampleRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExampleRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getResumptionToken = JavaMethod("()[B")
    getTrainingExample = JavaMethod("()[B")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExampleRecord$Builder"
        __javaconstructor__ = [("()V", False)]
        setResumptionToken = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/TrainingExampleRecord$Builder;", varargs=True)
        setTrainingExample = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/TrainingExampleRecord$Builder;", varargs=True)
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingExampleRecord;")