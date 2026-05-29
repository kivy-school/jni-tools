from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrainingExamplesOutput"]

class TrainingExamplesOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesOutput"
    getTrainingExampleRecords = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesOutput/Builder"
        __javaconstructor__ = [("()V", False)]
        setTrainingExampleRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/TrainingExamplesOutput$Builder;")
        addTrainingExampleRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/TrainingExampleRecord;)Landroid/adservices/ondevicepersonalization/TrainingExamplesOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingExamplesOutput;")